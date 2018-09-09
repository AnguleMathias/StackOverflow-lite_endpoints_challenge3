from base_test import BaseTestCase
from flask import json


class TestPostQuestion(BaseTestCase):

    def test_posting_new_question(self):
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
                                      dict(title="What", question="What is your question?"), )
                                  )
        reply3 = json.loads(response2.data.decode())
        self.assertIn("What is your question?", reply3.get("New Question Posted").values())
        self.assertEqual(response2.status_code, 201)
