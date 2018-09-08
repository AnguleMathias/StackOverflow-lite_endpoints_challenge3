from flask import jsonify
from app.db.dbManager import DBConnection

connect = DBConnection()
cursor = connect.dict_cursor


def add_new_user(user_name, email, password):
    query = (
        """INSERT INTO users (username, email, password) VALUES ('{}', '{}', '{}')""".format(user_name, email,
                                                                                             password))
    cursor.execute(query)


def is_user_exist(user_name):
    # check for username existence.
    query = ("""SELECT * FROM users where username = '{}'""".format(user_name))
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False


def get_user_by_username(user_name):
    query = ("""SELECT * from users where username = '{}'""".format(user_name))
    cursor.execute(query)
    user_name = cursor.fetchone()
    return user_name


def is_email_exist(email):
    # check for email existence.
    query = ("""SELECT * FROM users where email = '{}'""".format(email))
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False


def post_new_question(title, question, qstn_owner, date):
    query = (
        """INSERT INTO questions (title, question, qstn_owner, date) VALUES ('{}', '{}', '{}', '{}')""".
            format(title, question, qstn_owner, date))
    cursor.execute(query)


def is_question_exist(question):
    query = ("""SELECT * FROM questions where question = '{}'""".format(question))
    cursor.execute(query)
    question = cursor.fetchone()
    if question:
        return True
    return False


def get_single_question(qstn_id):
    # Query to fetch details of a question
    cursor.execute("SELECT * FROM questions WHERE qstn_id = '{}'".format(qstn_id))
    row = cursor.fetchone()
    return row


def get_all_questions():
    # Query to fetch all posted questions
    cursor.execute("SELECT * from questions")
    all_questions = cursor.fetchall()
    return all_questions


def get_all_answers_to_question(qstn_id):
    # Query to fetch all answers to a question
    query = ("""SELECT * from answers where qstn_id = '{}'""".format(qstn_id))
    cursor.execute(query)
    answers = cursor.fetchall()
    return answers


def delete_question(qstn_id, user_name):
    # Query to delete a specific question
    try:
        query = ("""DELETE FROM questions WHERE qstn_id = '{}' and qstn_owner = '{}'""".format(qstn_id, user_name))
        cursor.execute(query)
        delete = cursor.rowcount

        if int(delete) > 0:
            return jsonify({"message": "Question successfully deleted"}), 200
        else:
            return jsonify({"message": "Question not deleted, or doesn't exist"}), 400

    except Exception as exception:
        return jsonify({"message": str(exception)}), 400


def truncate_answers(qstn_id):
    # function to delete question inside answers table, but not the table itself
    try:
        query = ("""DELETE FROM answers WHERE qstn_id = '{}'""".format(qstn_id))
        cursor.execute(query)
        delete = cursor.rowcount

        if int(delete) > 0:
            return True
        else:
            return False

    except Exception as exception:
        return jsonify({"message": str(exception)}), 400


