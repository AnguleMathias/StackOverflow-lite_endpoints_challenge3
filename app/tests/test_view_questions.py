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
        self.assertEquals(reply.get("message"), "No questions posted yet")
        self.assertEquals(response3.status_code, 404)
