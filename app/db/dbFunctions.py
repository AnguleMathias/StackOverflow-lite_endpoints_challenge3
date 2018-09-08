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
