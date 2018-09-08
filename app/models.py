class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Question:
    def __init__(self, title, question, qstn_owner, date):
        self.title = title
        self.question = question
        self.qstn_owner = qstn_owner
        self.date = date

    def to_json(self):
        question = dict(
            title=self.title,
            question=self.question,
            qstn_owner=self.qstn_owner,
            date=self.date
        )
        return question

    # method to display class objects as dictionaries
    def __repr__(self):
        return repr(self.__dict__)
