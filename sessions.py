from flask import Blueprint, jsonify, request, current_app
from flask_pymongo import ObjectId, PyMongo
from app import mongo
from datetime import datetime
session_blueprint = Blueprint('session', __name__)



@session_blueprint.route('/session', methods=['GET'])
def get_sessions():
    # mongo = current_app.config['MONGO_URI']
    sessions = mongo.db.session.find()
    result = []
    for session in sessions:
        session['_id'] = str(session['_id'])
        result.append(session)
    return jsonify(result)

@session_blueprint.route('/session', methods=['POST'])
def create_session():
    data = request.get_json()
    data['created_time'] = datetime.now()
    data['updated_time'] = datetime.now()
    result = mongo.db.session.insert_one(data)
    return jsonify({'message': 'Session created successfully', 'id': str(result.inserted_id)})

# @session_blueprint.route('/session/<session_id>', methods=['GET'])
# def get_session(session_id):
#     session = mongo.db.session.find_one({'_id': ObjectId(session_id)})
#     if session:
#         session['_id'] = str(session['_id'])
#         return jsonify(session)
#     else:
#         return jsonify({'message': 'Session not found'})

@session_blueprint.route('/session/<session_id>', methods=['PUT'])
def update_session(session_id):
    data = request.get_json()
    data.pop("_id", None)
    data['updated_time'] = datetime.now()
    result = mongo.db.session.update_one({'_id': ObjectId(session_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Session with ID {session_id} updated successfully'})
    else:
        return jsonify({'message': 'Session not found'})

@session_blueprint.route('/session/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    result = mongo.db.session.delete_one({'_id': ObjectId(session_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Session with ID {session_id} deleted successfully'})
    else:
        return jsonify({'message': 'Session not found'})

@session_blueprint.route('/session/<user_id>', methods=['GET'])
def get_session_by_user_id(user_id):
    session = mongo.db.session.find_one({'user_id': user_id})
    if session:
        session['_id'] = str(session['_id'])
        return jsonify(session)
    else:
        return jsonify({'message': 'Session not found'})