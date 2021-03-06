from flask import json
from tests.base_test import BaseTestCase


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
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(
                                      dict(title="What", question="What is your question?"), )
                                  )
        response3 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        self.assertEqual(response3.status_code, 201)

    def test_post_short_answer(self):
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
        reply3 = json.loads(response3.data)
        self.assertEqual(reply3.get("message"), "Answer has to be at least 10 characters long")
        self.assertEqual(response3.status_code, 400)

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
        response4 = self.app.post("/api/v1/questions/1/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "Such an answer is already given for this same question, please try "
                                                "with another one ")
        self.assertEqual(response4.status_code, 409)

    def test_posting_answer_wrong_id(self):
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
        response3 = self.app.post("/api/v1/questions/2/answers",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        self.assertEqual(response3.status_code, 404)

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
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
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
                                  headers=dict(Authorization='Bearer ' + reply3['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.put("/api/v1/questions/1/answers/1",
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply3['access_token']),
                                 data=json.dumps(dict(answer="Do you have a question?"), )
                                 )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "Answer successfully updated")
        self.assertEqual(response4.status_code, 200)

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
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
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
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        response4 = self.app.put("/api/v1/questions/1/answers/2",
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply3['access_token']),
                                 data=json.dumps(dict(answer="Do you have a question?"), )
                                 )
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "No such answer exists")
        self.assertEqual(response4.status_code, 404)

    def test_get_answer_as_answer_owner(self):
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
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
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
                                  headers=dict(Authorization='Bearer ' + reply3['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        reply4 = json.loads(response3.data)
        response5 = self.app.get("/api/v1/questions/1/answers/1", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply3['access_token']))
        reply5 = json.loads(response5.data)
        self.assertEqual(response5.status_code, 200)

    def test_get_non_existing_answer(self):
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
                                  data=json.dumps(dict(answer="What is your answer?"), )
                                  )

        reply4 = json.loads(response3.data)
        response4 = self.app.get("/api/v1/questions/1/answers/2", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2['access_token']))
        reply5 = json.loads(response4.data)
        self.assertEqual(reply5.get("message"), "Answer does not exist")
        self.assertEqual(response4.status_code, 404)

    def test_get_all_answers(self):
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
                                  data=json.dumps(dict(answer="What is your answer?"), )
                                  )
        response4 = self.app.get("/api/v1/questions/1/answers", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2['access_token']))
        self.assertEqual(response4.status_code, 200)

    def test_get_all_answers_not(self):
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
        response3 = self.app.get("/api/v1/questions/1/answers", content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + reply2['access_token']))
        reply = json.loads(response3.data)
        self.assertEqual(reply.get("message"), "Answer does not exist")
        self.assertEqual(response3.status_code, 404)

    def test_delete_answer(self):
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
                                  data=json.dumps(dict(answer="What is your answer?"), )
                                  )
        response4 = self.app.delete("/api/v1/questions/1/answers/1", content_type='application/json',
                                    headers=dict(Authorization='Bearer ' + reply2['access_token']))
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "Answer successfully deleted")
        self.assertEqual(response4.status_code, 200)

    def test_delete_answer_wrong_id(self):
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
                                  data=json.dumps(dict(answer="What is your answer?"), )
                                  )
        response4 = self.app.delete("/api/v1/questions/1/answers/2", content_type='application/json',
                                    headers=dict(Authorization='Bearer ' + reply2['access_token']))
        reply4 = json.loads(response4.data)
        self.assertEqual(reply4.get("message"), "Answer does not exist")
        self.assertEqual(response4.status_code, 404)

    def test_posting_answer_wrong_url(self):
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
        response3 = self.app.post("/api/v1/questions/2/answer",
                                  content_type='application/json',
                                  headers=dict(Authorization='Bearer ' + reply2['access_token']),
                                  data=json.dumps(dict(answer="What is your question?"), )
                                  )
        self.assertEqual(response3.status_code, 404)
