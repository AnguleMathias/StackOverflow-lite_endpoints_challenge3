from .base_test import BaseTestCase
from flask import json


class TestAuth(BaseTestCase):

    def test_registration(self):
        """ Test for successful user register """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                 )
        self.assertEqual(response.status_code, 201)

    def test_registration_with_empty_user_name(self):
        """ Test for empty username validation """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username=" ", email="angule@gmail.com", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "username is missing")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_empty_password(self):
        """ Test for empty password validation """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", email="angule@gmail.com", password=""), )
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "password is missing")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_empty_email(self):
        """ Test for empty email validation """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", email=" ", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "email is missing")
        self.assertEquals(response.status_code, 400)
