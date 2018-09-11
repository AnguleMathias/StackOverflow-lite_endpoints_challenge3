import datetime

from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.db.dbFunctions import get_user_by_username, get_answer_by_id, is_comment_exist, \
    post_new_comment, get_question_by_id
from app.models import Comment
from app.validation import FieldValidation

validate = FieldValidation()
comment_blueprint = Blueprint("comment_blueprint", __name__)


class PostCommentToAnswer(MethodView):
    """class to post an answer to a question"""

    @jwt_required
    def post(self, ans_id, qstn_id):
        try:
            data = request.get_json()
            if "comment" in data.keys():
                comment = data.get("comment").strip()
                now = datetime.datetime.now()
                date = now.strftime("%Y-%m-%d %H:%M")

                loggedin_user = get_jwt_identity()
                user = get_user_by_username(user_name=loggedin_user["username"], password=loggedin_user["password"])
                comment_owner = user["username"]
                id_validation = validate.validate_entered_id(ans_id)
                if id_validation:
                    return id_validation
                comment_validation2 = validate.validate_comment(comment)
                if comment_validation2:
                    return comment_validation2
                comment_validation = validate.validate_characters(comment)
                if not comment_validation:
                    return jsonify({"message": "wrong comment format entered, Please try again"}), 400
                does_qstn_exist = get_question_by_id(qstn_id=qstn_id)
                if not does_qstn_exist:
                    return jsonify({"message": " No such question exists"}), 404
                does_ans_exist = get_answer_by_id(ans_id=ans_id, qstn_id=qstn_id)
                if not does_ans_exist:
                    return jsonify({"message": " No such answer exists"}), 404
                does_comment_exist = is_comment_exist(ans_id=ans_id, comment=comment)
                if does_comment_exist:
                    return jsonify({"message": "Such a comment is already given for this same answer, please try "
                                               "with another one "
                                    }), 409

                post_new_comment(comment=comment, qstn_id=qstn_id,
                                 comment_owner=comment_owner, ans_id=ans_id, date=date)
                new_comment = Comment(comment=comment, qstn_id=qstn_id,
                                      comment_owner=comment_owner, ans_id=ans_id, date=date)

                return jsonify({"Comment added successfully": new_comment.__dict__}), 201
            return jsonify({"message": "a 'key' is missing in your answer body"}), 400
        except Exception as exception:
            return jsonify({"message": exception}), 400


post_comment_view = PostCommentToAnswer.as_view("post_comment_view")

comment_blueprint.add_url_rule("/api/v1/questions/<qstn_id>/answers/<ans_id>/comments", view_func=post_comment_view,
                               methods=["POST"])
