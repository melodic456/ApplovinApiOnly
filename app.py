# pip install flask flask-pymongo

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime



app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://melodichoq:Melodic1890-@cluster0.tggka0v.mongodb.net/apploving?retryWrites=true&w=majority'
mongo = PyMongo(app)
app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
   username = request.json.get('username')
   password = request.json.get('password')
   status = request.json.get('status')

   existing_user = mongo.db.users.find_one({'username': username})
   if existing_user:
       return jsonify({'message': 'Username already exists'})

   new_user = {
       'username': username,
       'password': password,
       'status': 'active',
       'interstitial_total_loads': 0,
       'interstitial_total_clicks': 0,
       'rewarded_total_loads': 0,
       'rewarded_total_clicks': 0,
       'created_time': datetime.now(),
       'updated_time': datetime.now()
   }

   result = mongo.db.users.insert_one(new_user)
   data = {
        'user_id': str(result.inserted_id),
        'interstitial_load_session_total': 1,
        'interstitial_loads_this_session': 0,
        'interstitial_click_session_total': 1,
        'interstitial_clicks_this_session': 0,
        'rewarded_load_session_total': 1,
        'rewarded_loads_this_session': 0,
        'rewarded_click_session_total': 1,
        'rewarded_clicks_this_session': 0,
        'created_time': datetime.now(),
        'updated_time': datetime.now()
   }
   mongo.db.session.insert_one(data)
   return jsonify({'message': 'User registered successfully', 'id': str(result.inserted_id)})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = mongo.db.users.find_one({'username': username, 'password': password})
    if user:
        access_token = create_access_token(identity=str(user['_id']))
        jsondata = {'token': access_token, 'user_id': str(user['_id'])}
        print(jsondata)
        return jsonify(jsondata)
    else:
        return jsonify({'message': 'Invalid username or password'})

@app.route('/users', methods=['GET'])
def get_users():
   users = mongo.db.users.find()
   result = []
   for user in users:
       user['_id'] = str(user['_id'])
       result.append(user)
   return jsonify(result)

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
   user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
   if user:
       user['_id'] = str(user['_id'])
       return jsonify(user)
   else:
       return jsonify({'message': 'User not found'})

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
   user = request.get_json()
   if user:
    #    user['status'] = request.json.get('status')
       user.pop("_id", None)
       user['updated_time'] = datetime.now().isoformat() 
       mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user})
       return jsonify({'message': 'User updated successfully'})
   else:
       return jsonify({'message': 'User not found'})

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
   result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
   if result.deleted_count > 0:
       return jsonify({'message': 'User deleted successfully'})
   else:
       return jsonify({'message': 'User not found'})


if __name__ == '__main__':
    from interstitial import interstitial_blueprint
    from rewarded import rewarded_blueprint
    from sessions import session_blueprint
    app.register_blueprint(interstitial_blueprint)
    app.register_blueprint(rewarded_blueprint)
    app.register_blueprint(session_blueprint)
    app.run(debug=True, host="0.0.0.0", port=5000)