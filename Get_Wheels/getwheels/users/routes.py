from flask import url_for, Blueprint, jsonify
from getwheels.users.user import User, UserSchema

users = Blueprint('users', __name__)

@users.route('/get_users', methods=['GET', 'POST'])
def get_users():
	users = User.query.all()
	user_schema = UserSchema(many=True)
	output = user_schema.dump(users).data
	return jsonify({'users': output})