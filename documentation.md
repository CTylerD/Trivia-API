# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup.

The backend code follows the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

### Tests

In order to run tests navigate to the backend folder and run the following commands:

    dropdb trivia_test
    createdb trivia_test
    psql trivia_test < trivia.psql
    python3 test_flaskr.py

The first time you run the tests, omit the dropdb command.

All tests are kept in that file and should be maintained as updates are made to app functionality.

# API Reference

## Getting Started

Welcome! This API will provide all of the necessary information for accessing information in the Udacitrivia web application.

The base URL for this project is the local host, http://127.0.0.1:5000/

Authentication: This version of the application does not require authentication or API keys.

## Error Handling

### HTTP response codes in use:

- 200 - OK
- 400 - Bad Request
- 404 - Not Found
- 405 - Method Not Allowed
- 422 - Unprocessable Entity
- 500 - Internal Server Error

### Error Formatting

Error messages will be returned in the following format:

'''python
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
'''
            
## Endpoint Library

### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns:
    - A dictionary that contains id:category_string key:value pairs of

'''
http://localhost:5000/categories
'''

'''python
{
    '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"
}
'''

### GET '/questions'
- Fetches a dictionary containing information about all of the questions in the database.
- Request Arguments: None
- Returns a dictionary containing the following:
    - Success status, if successful
    - An array containing all of the questions in the database
    - The total number of questions in the database
    - A dictionary that contains all of the possible categories
    - The current category, which should return None

'''
curl http://localhost:5000/questions
'''

'''python
{
    "success": True,
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    },  
    "questions": [
        {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 5, 
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 6, 
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer's original name is Cassius Clay?"
        }
    ],
    "total_questions": 20,
    "current_category": null
}
'''

### DELETE '/questions/<int:question_id>'
- Deletes the question with the provided id
- Request Arguments: 
    - question_id (int)
- Returns a dictionary containing the following:
    - Success status, if successful
    - The ID of the deleted question
    - A list containing the current page of questions
    - The total number of questions in the database
    - A dictionary that contains all of the possible categories
    - The current category, which should return None

'''
curl -u delete http://localhost:5000/questions/10
'''

'''python
{
    "success": True,
    "deleted": 10,
    "questions": [
        {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 5, 
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 6, 
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer's original name is Cassius Clay?"
        }
    ],
    "total_questions": 20,
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    },
    "current_category": null
}
'''

### POST '/questions'
- Adds new question
- Request Arguments:
    - question (string)
    - answer (string)
    - difficulty (int)
    - category (int)
- Returns a dictionary containing the following:
    - Success status, if successful

'''
curl http://127.0.0.1:5000/questions?page -X POST -H "Content-Type: application/json" -d '{"question":"question", "answer":"answer", "difficulty":1, "category":1}'
'''

'''python
{
    'success': True
}
'''

### GET '/categories/<int:category_id>/questions/'
- Retrieves all questions in the provided category
- Request Arguments:
    - category_id (int)
- Returns a dictionary containing the following:
    - A list containing the current page of questions
    - The total number of questions in this category
    - The current category, which should return category_id

'''
curl http://127.0.0.1:5000/categories/1/questions/
'''

'''python
{
    "questions": [
        {
            "answer": "The Liver", 
            "category": 1, 
            "difficulty": 4, 
            "id": 20, 
            "question": "What is the heaviest organ in the human body?"
        }, 
        {
            "answer": "Alexander Fleming", 
            "category": 1, 
            "difficulty": 3, 
            "id": 21, 
            "question": "Who discovered penicillin?"
        }, 
        {
            "answer": "Blood", 
            "category": 1, 
            "difficulty": 4, 
            "id": 22, 
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ], 
    "total_questions": 3,
    "current_category": 1
}
'''

### POST '/quizzes'
- Returns a new question from the database by taking in the category and previous questions that have already been asked during the quiz
- Request Arguments:
    - previous_questions (array)
    - quiz_category (int)
- Returns a dictionary containing the following:
    - Success status, if successful
    - The next question to be shown in the quiz

'''
curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category":1}'
'''

'''python
{
    'success': True,
    'question': {
        "answer": "The Liver", 
        "category": 1, 
        "difficulty": 4, 
        "id": 20, 
        "question": "What is the heaviest organ in the human body?"
    }
}
'''

## Authors
Tyler Dennis
Caryn McCarthy and the  fine folks at Udacity who developed the Full-Stack Developer nanodegree

## Acknowledgements
You, dear reader, for making this all possible
