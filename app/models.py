"""models"""
from flask_bcrypt import Bcrypt


class User:
    """model for user"""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode('utf-8')


class Question:
    """model for questions"""
    def __init__(self, title, question, qstn_owner, date):
        self.title = title
        self.question = question
        self.qstn_owner = qstn_owner
        self.date = date

    def to_json(self):
        """function to jsonify"""
        question = dict(
            title=self.title,
            question=self.question,
            qstn_owner=self.qstn_owner,
            date=self.date
        )
        return question

    """method to display class objects as dictionaries"""
    def __repr__(self):
        return repr(self.__dict__)


class Answer:
    """model for answer"""
    def __init__(self, answer, ans_owner, qstn_id, vote, status, date):
        self.answer = answer
        self.ans_owner = ans_owner
        self.qstn_id = qstn_id
        self.vote = vote
        self.status = status
        self.date = date


class Comment:
    """model for comments"""
    def __init__(self, comment, comment_owner, qstn_id, ans_id, date):
        self.comment = comment
        self.comment_owner = comment_owner
        self.qstn_id = qstn_id
        self.ans_id = ans_id
        self.date = date
