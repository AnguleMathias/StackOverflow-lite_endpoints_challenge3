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
        self.assertEqual(reply["message"], "password is missing")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_empty_email(self):
        """ Test for empty email validation """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", email=" ", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "email is missing")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_wrong_username_format(self):
        """ Test for empty contact validation """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="@@$#%^&", email="angule@gmail.com", password="angule"), )
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "wrong username format entered, Please try again")
        self.assertEqual(response.status_code, 400)

    def test_registration_with_wrong_email_format(self):
        """ Test for empty contact validation """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", email="angulemathias", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "wrong email entered, Please try again")
        self.assertEqual(response.status_code, 400)

    def test_user_exists(self):
        """ Test for username exist """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                 )
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username already exists")
        self.assertEqual(response.status_code, 409)

    def test_email_exists(self):
        """ Test for email exist """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                 )
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="angulem", email="angule@gmail.com", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Email already exists")
        self.assertEqual(response.status_code, 409)

    def test_registration_with_no_keys(self):
        """ test_registration_with-no_keys """
        response = self.app.post("/api/v1/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(email="angule@gmail.com", password="mathias"), )
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply.get("message"), "a 'key(s)' is missing in your registration body")
        self.assertEquals(response.status_code, 400)

    def test_user_login_successful(self):
        """ Test for successful login """
        response2 = self.app.post("/api/v1/auth/register",
                                  content_type='application/json',
                                  data=json.dumps(
                                      dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                  )
        response = self.app.post("/api/v1/auth/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="angule", password="mathias"))
                                 )
        reply = json.loads(response.data)
        self.assertEquals(response.status_code, 200)
