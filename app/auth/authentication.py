from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.validation import FieldValidation
from app.models import User
from app.db.dbFunctions import is_user_exist, add_new_user, get_user_by_username, is_email_exist

validate = FieldValidation()
auth_blueprint = Blueprint("auth_blueprint", __name__)


class RegisterUser(MethodView):
    def post(self):
        reg_info = request.get_json()

        search_keys = ("username", "email", "password")

        if all(key in reg_info.key() for key in search_keys):
            user_name = reg_info.get("username").strip()
            email = reg_info.get("email").strip()
            password = reg_info.get("password")

            validation_resp = validate.register_validation(user_name, email, password)

            if validation_resp:
                return validation_resp

        email_validation = validate.register_validation(email)
        if not email_validation:
            return jsonify({"message": "wrong email entered, Please try again"}), 400

        validate_username = validate.register_validation(user_name)
        if not validate_username:
            return jsonify({"message": "wrong username format entered, Please try again"}), 400
