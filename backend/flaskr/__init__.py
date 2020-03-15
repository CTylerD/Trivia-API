import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from flask_cors import CORS
import random
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, all_qs):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [q.format() for q in all_qs]
    current_qs = questions[start:end]
    return current_qs


def retrieve_categories():
    category_query = Category.query.all()
    categories = {}
    for c in category_query:
        categories[c.id] = c.type
    return categories


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')

        return response

    @app.route('/categories', methods=['GET'])
    def get_categories():
        try:
            categories = retrieve_categories()
            return jsonify({
                            'success': True,
                            'categories': retrieve_categories()
            })
        except Exception as ex:
            abort(422)

    @app.route('/questions', methods=['GET'])
    def get_questions():
        try:
            all_questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, all_questions)
            if len(current_questions) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(all_questions),
                'categories': retrieve_categories(),
                'current_category': None
            })
        except Exception as ex:
            abort(404)

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter_by(id=question_id).first()

            if not question:
                abort(404)

            question.delete()
            all_questions = Question.query.all()
            current_questions = paginate_questions(request, all_questions)
            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(all_questions),
                'categories': retrieve_categories(),
                'current_category': None
            })

        except Exception as ex:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)
        search_terms = body.get('searchTerm', None)

        try:
            if search_terms:
                if search_terms != '':
                    results = Question.query.filter(
                              Question.question.ilike('%{}%'.format(
                                                      search_terms)))
                else:
                    results = Question.query.all()

                current_questions = paginate_questions(request, results)
                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(results.all()),
                    'current_category': None
                })

            else:
                question = Question(question=new_question,
                                    answer=new_answer,
                                    difficulty=new_difficulty,
                                    category=new_category)
                question.insert()

                return jsonify({
                    'success': True
                })
        except Exception as ex:
            abort(422)

    @app.route('/categories/<int:category_id>/questions/')
    def get_questions_by_category(category_id):
        try:
            category_questions = Question.query.filter(
                                 Question.category == category_id).all()

            if not category_questions:
                abort(404)

            current_questions = paginate_questions(request, category_questions)

            return jsonify({
                    'questions': current_questions,
                    'total_questions': len(category_questions),
                    'current_category': category_id
                })
        except Exception as ex:
            abort(404)

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            data = request.get_json()
            prev_questions = data['previous_questions']
            category_id = data["quiz_category"]["id"]
            if category_id == 0:
                if prev_questions is not None:
                    questions = Question.query.filter(
                                Question.id.notin_(prev_questions)).all()
                else:
                    questions = Question.query.all()
            else:
                category = Category.query.get(category_id)
                if prev_questions is not None:
                    questions = Question.query.filter(
                                Question.id.notin_(prev_questions),
                                Question.category == category.id).all()
                else:
                    questions = Question.query.filter(
                                Question.category == category.id).all()
            next_question = random.choice(questions).format()

            if next_question is None:
                next_question = False
            return jsonify({
                'success': True,
                'question': next_question
            })

        except Exception as ex:
            abort(422)

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(405)
    def resource_not_found(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                'success': False,
                'error': 422,
                'message': 'unprocessable'
        }), 422

    @app.errorhandler(500)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    return app
