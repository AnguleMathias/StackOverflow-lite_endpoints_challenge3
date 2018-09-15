from flask import json
from tests.base_test import BaseTestCase


class TestPostComment(BaseTestCase):

    def test_posting_comment_wrong_key(self):
        response1 = self.app.post("/api/v1/auth/register", content_type='application/json', data=json.dumps(
            dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login", content_type='application/json', data=json.dumps(
            dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/questions", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(title="What", question="What is your question?"), )
                                  )
        response3 = self.app.post("/api/v1/questions/1/answers", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )

        response_ = self.app.post("/api/v1/auth/login", content_type='application/json', data=json.dumps(
            dict(username="angule", password="mathias"))
                                 )
        reply2_ = json.loads(response.data.decode())
        response4 = self.app.post("/api/v1/questions/1/answers/1/comments", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comments="What is your question?"), )
                                  )

        reply3 = json.loads(response4.data)
        self.assertEqual(reply3.get("message"), "a 'key' is missing in your answer body")
        self.assertEqual(response4.status_code, 400)

    def test_posting_comment(self):
        response1 = self.app.post("/api/v1/auth/register", content_type='application/json', data=json.dumps(
            dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login", content_type='application/json', data=json.dumps(
            dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/questions", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(title="What", question="What is your question?"), )
                                  )

        response3 = self.app.post("/api/v1/questions/1/answers", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.post("/api/v1/questions/1/answers/1/comments", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comment="What is your question?"), )
                                  )
        self.assertEqual(response4.status_code, 201)

    def test_posting_comment_wrong_id(self):
        response1 = self.app.post("/api/v1/auth/register", content_type='application/json', data=json.dumps(
            dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login", content_type='application/json', data=json.dumps(
            dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/questions", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(title="What", question="What is your question?"), )
                                  )

        response3 = self.app.post("/api/v1/questions/1/answers", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.post("/api/v1/questions/1/answers/2/comments", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comment="What is your question?"), )
                                  )
        self.assertEqual(response4.status_code, 404)

    def test_post_short_comment(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/questions",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )
        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="Whath what whatt"), )
                                  )
        response4 = self.app.post("/api/v1/questions/1/answers/1/comments", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comment="Wh"), )
                                  )
        reply3 = json.loads(response4.data)
        self.assertEqual(reply3.get("message"), "Comment has to be at least 3 characters long")
        self.assertEqual(response4.status_code, 400)

    def test_post_existing_answer(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/questions",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )
        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.post("/api/v1/questions/2/answers/1/comments",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comment="What is your question?"), )
                                  )
        response5 = self.app.post("/api/v1/questions/2/answers/1/comments",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comment="What is your question?"), )
                                  )
        self.assertEqual(response5.status_code, 404)

    def test_post_comment_bad_url(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/questions",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )
        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="W?"), )
                                  )
        response4 = self.app.post("/api/v1/questions/1/answers/1/commen", content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(comment="What is this??"), )
                                  )
        self.assertEqual(response4.status_code, 404)
