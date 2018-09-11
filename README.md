# StackOverflow-lite_API_v1
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Badges
[![Build Status](https://travis-ci.org/AnguleMathias/StackOverflow-lite_endpoints_challenge3.svg?branch=develop)](https://travis-ci.org/AnguleMathias/StackOverflow-lite_endpoints_challenge3)
[![Coverage Status](https://coveralls.io/repos/github/AnguleMathias/StackOverflow-lite_endpoints_challenge3/badge.svg?branch=develop)](https://coveralls.io/github/AnguleMathias/StackOverflow-lite_endpoints_challenge3?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/7038ca41e9952afc5ece/maintainability)](https://codeclimate.com/github/AnguleMathias/StackOverflow-lite_endpoints_challenge3/maintainability)


## Features

* Users can: 
    1. Create an account and log in.
    2. Can view questions
    3. Post questions.
    4. Delete the questions they post
    5. Post answers
    6. Accept an answer out of all the answers to his/her queston as they preferred answer
    7. Upvote or downvote an answer.
    8. Comment on an answer.
    9. Fetch all questions he/she has ever asked on the platform
   10. Search for questions on the platform
    
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
GET | `/api/v1/questions/?q={'search_string'}` | Search a questions
GET | `/api/v1/questions/<question_id>` | Retrieve a question
PUT | `/api/v1/questions/>question_id>` | Edit a question of a logged in user
DELETE | `/api/v1/questions/<question_id>` | Delete a question of a logged in user

#### Answers Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/<question_id>/answers` | Add an answer
PUT | `/api/v1/questions/answers` | Update an answer


## Deployment


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