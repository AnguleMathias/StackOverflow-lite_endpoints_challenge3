from base_test import BaseTestCase
from flask import json


class TestViewQuestion(BaseTestCase):

    def test_viewing_questions_with_db(self):
        """ Test viewing questions """
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@email.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", password="mathias"))
                                 )
        reply2 = json.loads(response.data.decode())

        response3 = self.app.get("/api/v1/questions", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2[1]['token']))
        reply = json.loads(response3.data)
        self.assertEqual(reply.get("message"), "No questions posted yet")
        self.assertEqual(response3.status_code, 404)

    def test_viewing_all_questions(self):
        """ Test viewing questions """
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
        response3 = self.app.get("/api/v1/questions", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2[1]['token']))
        self.assertEqual(response3.status_code, 200)

    def test_viewing_single_question(self):
        """ Test viewing questions """
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
                                      dict(title="Life", question="Are there so many questions about life?"), )
                                  )
        response3 = self.app.get("/api/v1/questions/1", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2[1]['token']), data={"qstn_id": "1"})
        self.assertEqual(response3.status_code, 200)

    def test_deleting_a_questions(self):
        """ Test deleting questions """
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
                                      dict(title="Life", question="Are there so many questions about life?"), )
                                  )
        response3 = self.app.delete("/api/v1/questions/1", content_type='application/json',
                                    headers=dict(Authorization='Bearer ' + reply2[1]['token']))

        reply = json.loads(response3.data)
        self.assertEqual(reply.get("message"), "Question successfully deleted")
        self.assertEqual(response3.status_code, 200)

    def test_deleting_a_questions_with_improper_id(self):
        """ Test deleting questions """
        response1 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@email.com", password="mathias"), )
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
                                      dict(title="Life", question="Are there so many questions about life?"), )
                                  )
        response3 = self.app.delete("/api/questions/q", content_type='application/json',
                                    headers=dict(Authorization='Bearer ' + reply2[1]['token']))

        reply = json.loads(response3.data)
        self.assertEqual(reply.get("message"), "Id should be an interger")
        self.assertEqual(response3.status_code, 400)

    def test_viewing_all_user_questions_(self):
        """ Test viewing questions """
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
        response3 = self.app.get("/api/v1/questions/user_questions", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2[1]['token']),
                                 data={"qstn_owner": "angule"})
        reply = json.loads(response3.data.decode())
        self.assertEqual(reply.get("message"), "user has no questions")
        self.assertEqual(response3.status_code, 404)
