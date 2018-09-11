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


def get_user_by_username(user_name, password):
    query = ("""SELECT * from users where username = '{}' and password = '{}'""".format(user_name, password))
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
        """INSERT INTO questions (title, question, qstn_owner, date) 
        VALUES ('{}', '{}', '{}', '{}')""".format(title, question, qstn_owner, date))
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


def delete_answer(qstn_id, ans_id):
    try:
        query = ("""DELETE FROM answers WHERE qstn_id = '{}' and ans_id = '{}'""".format(qstn_id, ans_id))
        cursor.execute(query)
        delete = cursor.rowcount

        if int(delete) > 0:
            return jsonify({"message": "Answer successfully deleted"}), 200
        else:
            return jsonify({"message": "Answer not deleted, or doesn't exist"}), 400

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


def is_answer_exist(qstn_id, answer):
    # check answer to question existence
    query = ("""SELECT * FROM answers WHERE qstn_id = '{}' and answer = '{}'""".format(qstn_id, answer))
    cursor.execute(query)
    answer = cursor.fetchone()
    if answer:
        return True
    return False


def is_comment_exist(ans_id, comment):
    # check answer to question existence
    query = ("""SELECT * FROM comments WHERE ans_id = '{}' and comment = '{}'""".format(ans_id, comment))
    cursor.execute(query)
    comment = cursor.fetchone()
    if comment:
        return True
    return False


def get_question_by_id(qstn_id):
    # check question existence
    query = ("""SELECT * FROM questions where qstn_id = '{}'""".format(qstn_id))
    cursor.execute(query)
    question = cursor.fetchone()
    if question:
        return True
    return False


def get_answer_by_id(ans_id, qstn_id):
    # check answer existence
    query = ("""SELECT * FROM answers where ans_id = '{}' and qstn_id = '{}'""".format(ans_id, qstn_id))
    cursor.execute(query)
    answer = cursor.fetchone()
    return answer


def post_new_answer(answer, ans_owner, qstn_id, vote, status, date):
    # post a new answer
    query = (
        """INSERT INTO answers (answer, ans_owner, qstn_id, votes, status, date) 
        VALUES ('{}', '{}', '{}','{}', '{}', '{}')""".format(answer, ans_owner, qstn_id, vote, status, date))
    cursor.execute(query)


def post_new_comment(comment, comment_owner, ans_id, date):
    # post a new answer
    query = (
        """INSERT INTO comments (comment, comment_owner, ans_id, date) 
        VALUES ('{}', '{}', '{}', '{}')""".format(comment, comment_owner, ans_id, date))
    cursor.execute(query)


def update_answer(answer, ans_id, qstn_id):
    try:
        query = ("""UPDATE answers SET answer = '{}' where ans_id = '{}' and qstn_id = '{}'""".format(
            answer, ans_id, qstn_id))
        cursor.execute(query)
        count = cursor.rowcount
        if int(count) > 0:
            return "Answer successfully updated"
        else:
            return "Answer not updated, or doesn't exist"

    except Exception as exception:
        return jsonify({"message": str(exception)}), 400


def accept_answer(status, qstn_id, ans_id):
    try:
        query = ("""UPDATE answers SET status = '{}' where ans_id = '{}' and qstn_id = '{}'""".format(
            status, ans_id, qstn_id))
        cursor.execute(query)
        count = cursor.rowcount
        if int(count) > 0:
            return "Answer successfully accepted"
        else:
            return "Failed to accept answer, or it doesn't exist"

    except Exception as exception:
        return jsonify({"message": str(exception)}), 400


def get_answer_details(qstn_id, ans_id):
    cursor.execute("""SELECT * FROM answers WHERE qstn_id = '{}' and ans_id = '{}'""".format(qstn_id, ans_id))
    row = cursor.fetchone()
    return row


def get_all_user_questions(user_name):
    # Query to get questions posted by a specific user
    cursor.execute("SELECT * FROM questions WHERE qstn_owner = '{}'".format(user_name))
    questions = cursor.fetchall()
    return questions
