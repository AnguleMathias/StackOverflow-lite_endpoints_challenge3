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
        self.assertEquals(response3.status_code, 201)
