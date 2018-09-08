from .base_test import BaseTestCase
from flask import jsonify, json


class TestAuth(BaseTestCase):

    def test_registration(self):
        """ Test for successful user register """
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(
                                     dict(username="angule", email="angule@gmail.com", password="mathias"), )
                                 )
        self.assertEquals(response.status_code, 201)