from app.db.dbManager import DBConnection

connect = DBConnection()
cursor = connect.dict_cursor


def add_new_user(user_name, email, password):
    query = (
        """INSERT INTO users (username, email, password) VALUES ('{}', '{}', '{}')""".format(user_name, email,
                                                                                             password))
    cursor.execute(query)
