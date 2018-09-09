import datetime
from flask import jsonify, request, Blueprint, json
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validation import FieldValidation
from app.models import Question, Answer, Comment
from app.db.dbFunctions import post_new_question, is_question_exist, get_user_by_username, get_all_questions, \
    get_single_question, get_all_answers_to_question, delete_question, get_question_by_id, is_answer_exist, \
    post_new_answer, update_answer, get_answer_details, accept_answer, get_answer_by_id, get_all_user_questions, \
    truncate_answers

validate = FieldValidation()
question_blueprint = Blueprint("question_blueprint", __name__)


class PostQuestion(MethodView):
    """class for posting new question"""

    @jwt_required
    def post(self):
        try:
            data = request.get_json()

            search_keys = ("title", "question")

            if all(key in data.keys() for key in search_keys):
                now = datetime.datetime.now()

                loggedin_user = get_jwt_identity()
                user = get_user_by_username(user_name=loggedin_user)

                qstn_owner = user["username"]
                title = data.get("title").strip()
                question = data.get("question").strip()
                date = now.strftime("%Y-%m-%d %H:%M")

                validation = validate.validate_question(title, question)
                if validation:
                    return validation

                does_qstn_exist = is_question_exist(question)
                if does_qstn_exist:
                    return jsonify({"message":"Question already exists, check it out for an answer"}), 409

                post_new_question(title=title, question=question, qstn_owner=qstn_owner, date=date)

                new_question = Question(title=title, question=question, qstn_owner=qstn_owner, date=date)
                return jsonify({"New Question Posted": new_question.__dict__}), 201
            # return jsonify({"message": "a 'key(s)' is missing in your question body"}), 400
        except:
            return jsonify({"message": "All fields are required"}), 400


post_question_view = PostQuestion.as_view("post_question_view")

question_blueprint.add_url_rule("/api/v1/questions", view_func=post_question_view, methods=["POST"])