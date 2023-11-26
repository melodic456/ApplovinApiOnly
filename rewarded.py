from flask import Blueprint, jsonify, request, current_app
from flask_pymongo import ObjectId, PyMongo
from app import mongo
from datetime import datetime

rewarded_blueprint = Blueprint('rewarded', __name__)


@rewarded_blueprint.route('/rewarded', methods=['GET'])
def get_rewarded():
    # mongo = current_app.config['MONGO_URI']
    rewarded = mongo.db.rewarded.find()
    result = []
    for reward in rewarded:
        reward['_id'] = str(reward['_id'])
        result.append(reward)
    return jsonify(result)

@rewarded_blueprint.route('/rewarded', methods=['POST'])
def create_rewarded():
    data = request.get_json()
    result = mongo.db.rewarded.insert_one(data)
    return jsonify({'message': 'Reward created successfully', 'id': str(result.inserted_id)})

@rewarded_blueprint.route('/rewarded/<rewarded_id>', methods=['GET'])
def get_rewarded_by_id(rewarded_id):
    reward = mongo.db.rewarded.find_one({'_id': ObjectId(rewarded_id)})
    if reward:
        reward['_id'] = str(reward['_id'])
        return jsonify(reward)
    else:
        return jsonify({'message': 'Reward not found'})

@rewarded_blueprint.route('/rewarded/<rewarded_id>', methods=['PUT'])
def update_rewarded(rewarded_id):
    data = request.get_json()
    result = mongo.db.rewarded.update_one({'_id': ObjectId(rewarded_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Reward with ID {rewarded_id} updated successfully'})
    else:
        return jsonify({'message': 'Reward not found'})

@rewarded_blueprint.route('/rewarded/<rewarded_id>', methods=['DELETE'])
def delete_rewarded(rewarded_id):
    result = mongo.db.rewarded.delete_one({'_id': ObjectId(rewarded_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Reward with ID {rewarded_id} deleted successfully'})
    else:
        return jsonify({'message': 'Reward not found'})

@rewarded_blueprint.route('/rewarded_loads', methods=['POST'])
def create_rewarded_load():
    data = request.get_json()
    data['created_time'] = datetime.now().isoformat() 
    result = mongo.db.rewarded_loads.insert_one(data)
    return jsonify({'message': 'Reward load created successfully', 'id': str(result.inserted_id)})

@rewarded_blueprint.route('/rewarded_loads/<load_id>', methods=['GET'])
def get_rewarded_load(load_id):
    reward_load = mongo.db.rewarded_loads.find_one({'_id': ObjectId(load_id)})
    if reward_load:
        reward_load['_id'] = str(reward_load['_id'])
        return jsonify(reward_load)
    else:
        return jsonify({'message': 'Reward load not found'})

@rewarded_blueprint.route('/rewarded_loads/<load_id>', methods=['PUT'])
def update_rewarded_load(load_id):
    data = request.get_json()
    result = mongo.db.rewarded_loads.update_one({'_id': ObjectId(load_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Reward load with ID {load_id} updated successfully'})
    else:
        return jsonify({'message': 'Reward load not found'})

@rewarded_blueprint.route('/rewarded_loads/<load_id>', methods=['DELETE'])
def delete_rewarded_load(load_id):
    result = mongo.db.rewarded_loads.delete_one({'_id': ObjectId(load_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Reward load with ID {load_id} deleted successfully'})
    else:
        return jsonify({'message': 'Reward load not found'})

@rewarded_blueprint.route('/rewarded_clicks', methods=['POST'])
def create_rewarded_click():
    data = request.get_json()
    data['created_time'] = datetime.now().isoformat() 
    result = mongo.db.rewarded_clicks.insert_one(data)
    return jsonify({'message': 'Reward click created successfully', 'id': str(result.inserted_id)})

@rewarded_blueprint.route('/rewarded_clicks/<click_id>', methods=['GET'])
def get_rewarded_click(click_id):
    reward_click = mongo.db.rewarded_clicks.find_one({'_id': ObjectId(click_id)})
    if reward_click:
        reward_click['_id'] = str(reward_click['_id'])
        return jsonify(reward_click)
    else:
        return jsonify({'message': 'Reward click not found'})

@rewarded_blueprint.route('/rewarded_clicks/<click_id>', methods=['PUT'])
def update_rewarded_click(click_id):
    data = request.get_json()
    result = mongo.db.rewarded_clicks.update_one({'_id': ObjectId(click_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Reward click with ID {click_id} updated successfully'})
    else:
        return jsonify({'message': 'Reward click not found'})

@rewarded_blueprint.route('/rewarded_clicks/<click_id>', methods=['DELETE'])
def delete_rewarded_click(click_id):
    result = mongo.db.rewarded_clicks.delete_one({'_id': ObjectId(click_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Reward click with ID {click_id} deleted successfully'})
    else:
        return jsonify({'message': 'Reward click not found'})