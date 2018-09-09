from base_test import BaseTestCase
from flask import json


class TestPostAnswer(BaseTestCase):

    def test_posting_answer(self):
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
        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        self.assertEqual(response3.status_code, 201)

    def test_updating_answer_as_answer_owner(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )

        response1 = self.app.post("/api/auth/register",
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
        _response = self.app.post("/api/v1/auth/login",
                                  content_type='application/json',
                                  data=json.dumps(dict(username="angule", password="araali"))
                                  )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.put("/api/questions/1/answers/1",
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                 data=json.dumps(dict(answer="Do you have a question?"), )
                                 )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "Answer successfully updated")
        self.assertEqual(response4.status_code, 200)

    def test_updating_answer_as_question_owner(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )

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
        _response = self.app.post("/api/v1/auth/login",
                                  content_type='application/json',
                                  data=json.dumps(dict(username="angule", password="mathias"))
                                  )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.put("/api/questions/1/answers/1",
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                 data=json.dumps(dict(answer="Do you have any question?"), )
                                 )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "Answer successfully accepted")
        self.assertEqual(response4.status_code, 200)

    def test_updating_nonexistant_answer_as_answer_owner(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )

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
        _response = self.app.post("/api/v1/auth/login",
                                  content_type='application/json',
                                  data=json.dumps(dict(username="angule", password="mathias"))
                                  )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.put("/api/v1/questions/1/answers/2",
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                 data=json.dumps(dict(answer="Do you have a question?"), )
                                 )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "No such answer exists")
        self.assertEqual(response4.status_code, 404)

    def test_update_nonexistant_answer_as_question_owner(self):
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )

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
        _response = self.app.post("/api/v1/auth/login",
                                  content_type='application/json',
                                  data=json.dumps(dict(username="angule", password="mathias"))
                                  )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.put("/api/v1/questions/2/answers/1",
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply3[1]['token']),
                                 data=json.dumps(dict(answer="Do you have a question?"), )
                                 )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "No such question exists any more")
        self.assertEqual(response4.status_code, 404)
