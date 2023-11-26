from bson import ObjectId, Regex
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
# from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://melodichoq:Melodic1890-@cluster0.tggka0v.mongodb.net/apploving?retryWrites=true&w=majority"
mongo = PyMongo(app)
app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)


@app.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    serialized_users = []
    
    for user in users:
        serialized_user = {}
        for key, value in user.items():
            if isinstance(value, ObjectId):
                serialized_user[key] = str(value)  # Convert ObjectId to string
            else:
                serialized_user[key] = value
        serialized_users.append(serialized_user)
    
    return jsonify(serialized_users)


@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    user['_id'] = str(user['_id']) 
    print(user)
    return jsonify(user)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    mongo.db.users.insert_one(data)
    return jsonify({"message": "User created successfully"})


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    data.pop("_id", None)
    data["date_updated"] = datetime.now()
    print(data)
    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "User updated successfully"})


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    mongo.db.users.delete_one({"id": id})
    return jsonify({"message": "User deleted successfully"})


# @app.route("/register", methods=["POST"])
# def register():
#     username = request.json.get("username")
#     password = request.json.get("password")
#     user = mongo.db.users.find_one({"username": username})
#     if user:
#         return jsonify({"message": "Username already exists"})
#     else:
#         new_user = {
#             "username": username,
#             "password": password,
#             "status": None,
#             "Interstitial_ads_loaded_total": None,
#             "rewarded_ads_loaded": None,
#             "rewarded_ads_clicked": None,
#             "Interstitial_ad_limit": None,
#             "rewarded_ads_limit": None,
#             "session_interstitial_clicks": None,
#             "session_rewarded_clicks": None,
#             "total_sessions": None,
#             "date_created": datetime.now(),
#             "date_updated": datetime.now()
#         }
#         mongo.db.users.insert_one(new_user)
#         return jsonify({"message": "User registered successfully"})

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    user = mongo.db.users.find_one({"username": username})
    if user:
        return jsonify({"message": "Username already exists"})
    else:
        new_user = {
            "username": username,
            "password": password,
            "status": None,
            "interstitial_ad_clicked_total": None,
            "interstitial_ad_clicked_session": None,
            "interstitial_ad_clicked_limit": 1,
            "rewarded_ad_clicked_limit": 1,
            "rewarded_clicked_limit": 10,
            "rewarded_limit": 10,
            "Interstitial_ads_loaded_total": None,
            "rewarded_ads_loaded": None,
            "rewarded_ads_clicked": None,
            "Interstitial_ad_limit": 10,
            "rewarded_ads_limit": 10,
            "session_interstitial_clicks": None,
            "session_rewarded_clicks": None,
            "total_sessions": None,
            "rewarded_loaded_total": None,
            "rewarded_clicked": None,
            "rewarded_ad_clicked_session": None,
            "rewarded_ad_clicked_total": None,
            "rewarded_ad_clicked_session_limit": 10,
            "date_created": datetime.now(),
            "date_updated": datetime.now()
        }
        mongo.db.users.insert_one(new_user)
        return jsonify({"message": "User registered successfully"})


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    user = mongo.db.users.find_one({"username": username, "password": password})
    if user:
        access_token = create_access_token(identity=str(user['_id']))
        jsondata = {'token': access_token, 'user_id': str(user['_id'])}
        print(jsondata)
        return jsonify(jsondata)
    else:
        return jsonify({'message': 'Invalid username or password'})


@app.route("/protected", methods=["GET"])
@jwt_required
def protected():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": user_id})
    return jsonify({"message": f"Welcome, {user['username']}"})


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)