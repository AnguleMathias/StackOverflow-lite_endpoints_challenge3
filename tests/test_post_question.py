from tests.base_test import BaseTestCase
from flask import json


class TestPostQuestion(BaseTestCase):

    def test_post_new_question(self):
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
                                  headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )
        reply3 = json.loads(response2.data.decode())
        self.assertIn("What is your question?", reply3.get("New Question Posted").values())
        self.assertEqual(response2.status_code, 201)

    def test_post_existing_question(self):
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
                                  headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )
        response2 = self.app.post("/api/v1/questions",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )

        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "Question already exists, check it out for an answer")
        self.assertEqual(response2.status_code, 409)

    def test_post_empty_question(self):
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
                                  headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                  data=json.dumps(dict(title="What", question=" "), )
                                  )

        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "No question was given")
        self.assertEqual(response2.status_code, 400)

    def test_post_with_empty_title(self):
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
                                  headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                  data=json.dumps(dict(title=" ", question="What is your question?"), )
                                  )

        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "No question title was given")
        self.assertEqual(response2.status_code, 400)
