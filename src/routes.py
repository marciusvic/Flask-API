# routes.py
from flask import jsonify, make_response, request

def configure_routes(app):
    @app.route('/users', methods=['GET'])
    def get_all_users():
        try:
            users = User.query.all()
            if len(users):
                return jsonify([user.json() for user in users])
            else:
                return make_response(jsonify({'message': 'no users found'}), 404)
        except Exception as e:
            print(f"Error getting users: {e}")
            return make_response(jsonify({'message': 'internal error getting users'}), 500)

    @app.route('/users/<int:id>', methods=['GET'])
    def get_user_by_id(id):
        try:
            user = User.query.filter_by(id=id).first()
            if user:
                return jsonify(user.json())
            return make_response(jsonify({'message': 'user not found'}), 404)
        except Exception as e:
            print(f"Error getting users: {e}")
            return make_response(jsonify({'message': 'internal error getting user'}), 500)

    @app.route('/users', methods=['POST'])
    def create_user():
        try:
            data = request.get_json()
            new_user = User(username=data['username'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return make_response(jsonify({'message':'user created'}), 201)
        except Exception as e:
            print(f"Error getting users: {e}")
            return make_response(jsonify({'message':'internal error creating user'}), 500)

    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user(id):
        try:
            user = User.query.filter_by(id=id).first()
            if user:
                data = request.get_json()
                user.username = data['username']
                user.email = data['email']
                db.session.commit()
                return make_response(jsonify({'message':'user updated'}), 200)
            return make_response(jsonify({'message': 'user not found'}), 404)
        except Exception as e:
            print(f"Error getting users: {e}")
            return make_response(jsonify({'message': 'internal error getting user'}), 500)

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        try:
            user = User.query.filter_by(id=id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return make_response(jsonify({'message':'user deleted'}), 200)
            return make_response(jsonify({'message': 'user not found'}), 404)
        except Exception as e:
            print(f"Error getting users: {e}")
            return make_response(jsonify({'message': 'internal error getting user'}), 500)
