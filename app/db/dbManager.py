import psycopg2
import psycopg2.extras as extra
from app.config import app_config


class DBConnection:
    def __init__(self):
        if app_config["development"]:
            self.con = psycopg2.connect(database="stackoverflow", user="postgres", password="mathias",
                                        host="localhost", port="5432")
            self.con.autocommit = True
            self.cursor = self.con.cursor()
            self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)
        elif app_config["testing"]:
            self.con = psycopg2.connect(database="stackoverflow_tests", user="postgres", password="mathias",
                                        host="localhost", port="5432")
            self.con.autocommit = True
            self.cursor = self.con.cursor()
            self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)
