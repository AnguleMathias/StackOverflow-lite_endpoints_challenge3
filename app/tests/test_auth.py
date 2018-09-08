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
