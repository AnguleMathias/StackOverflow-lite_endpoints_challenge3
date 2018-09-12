# StackOverflow-lite_API_v1
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Badges
[![Build Status](https://travis-ci.org/AnguleMathias/StackOverflow-lite_endpoints_challenge3.svg?branch=develop)](https://travis-ci.org/AnguleMathias/StackOverflow-lite_endpoints_challenge3)
[![Coverage Status](https://coveralls.io/repos/github/AnguleMathias/StackOverflow-lite_endpoints_challenge3/badge.svg?branch=develop)](https://coveralls.io/github/AnguleMathias/StackOverflow-lite_endpoints_challenge3?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/7038ca41e9952afc5ece/maintainability)](https://codeclimate.com/github/AnguleMathias/StackOverflow-lite_endpoints_challenge3/maintainability)


## Features

* Users can: 
    1. Create an account and log in
    2. Can view questions
    3. Post questions
    4. Delete the questions they post
    5. Post answers to questions
    6. View answers to questions
    7. Update answers to questions
    8. Delete answers to questions
    9. Accept an answer out of all the answers to his/her question as they preferred answer
    10. Comment on an answer
    11. Fetch all questions he/she has ever asked on the platform

## Endpoints

#### Users Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/register` | Add a user
POST | `/api/v1/auth/login` | Login a user

#### Questions Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question
GET | `/api/v1/questions` | Lists all questions
GET | `/api/v1/questions/<question_id>` | Retrieve a question
GET | `/api/v1/questions/user_questions` | Retrieve single user questions
PUT | `/api/v1/questions/>question_id>` | Edit a question of a logged in user
DELETE | `/api/v1/questions/<question_id>` | Delete a question of a logged in user

#### Answers Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/<question_id>/answers` | Add answer
GET | `/api/v1/questions/<question_id>/answers/<answer_id>` | View an answer
GET | `/api/v1/questions/<question_id>/answers` | View all answers to a question
PUT | `/api/v1/questions/<question_id>/answers/<answer_id>` | Update an answer 
DELETE | `/api/v1/questions/<question_id>/answers/<answer_id>` | Delete an answer
                             


#### Comment Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/<qstn_id>/answers/<ans_id>/comments` | Add a comment

## Deployment
Api [host](https://stack-overflow-lite-angule.herokuapp.com/api/v1/questions)

## Documentation
Api [documentation](https://stackoverflowliteapiv11.docs.apiary.io)

## Tools Used

* [Flask](http://flask.pocoo.org/) - Framework for Python
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - Tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - Package installer for Python


## Getting Started


* Clone the project into your local repository using this command:

            `git clone https://github.com/AnguleMathias/StackOverflow-lite_endpoints_challenge3.git`

* Change directory to the cloned folder using the following command for Windows, Linux and MacOS

            `cd StackOverflow-lite`

* If you do not have a virtual environment installed run the following command, else follow the next steps.

            `pip install virtualenv`
            
* Create a virtual environment(for Windows, Linux and MacOS)

            `virtualenv venv`

* Activate the virtual environment(Windows only)

            `source venv/Scripts/activate`

     and for Linux and MacOS

            `source venv/bin/activate`

* Install the app dependencies.(for Windows, Linux and MacOS)

            `pip install -r requirements.txt`

* Run the app(for Windows, Linux and MacOS)

            `python run.py`


## Running the tests

* Install pytest while the virtual environment is active

            `pip install pytest`

* Run the tests.

            `pytest`

:wink: