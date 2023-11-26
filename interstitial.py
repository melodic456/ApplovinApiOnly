from flask import Blueprint, jsonify, request, current_app
from flask_pymongo import ObjectId
# from flask_pymongo import PyMongo
from app import mongo
from datetime import datetime

interstitial_blueprint = Blueprint('interstitial', __name__)



# Assuming you have initialized the Flask-PyMongo instance as 'mongo'

# #########################Interstitial#########################################

@interstitial_blueprint.route('/interstitial', methods=['GET'])
def get_interstitials():
    # mongo = current_app.config['MONGO_URI']
    interstitials = mongo.db.interstitials.find()
    # result = []
    for interstitial in interstitials:
        interstitial['_id'] = str(interstitial['_id'])
        # result.append(interstitial)
        return jsonify(interstitial)

@interstitial_blueprint.route('/interstitial', methods=['POST'])
def create_interstitial():
    data = request.get_json()
    result = mongo.db.interstitials.insert_one(data)
    return jsonify({'message': 'Interstitial ad created successfully', 'id': str(result.inserted_id)})

@interstitial_blueprint.route('/interstitial/<interstitial_id>', methods=['GET'])
def get_interstitial(interstitial_id):
    interstitial = mongo.db.interstitials.find_one({'_id': ObjectId(interstitial_id)})
    if interstitial:
        interstitial['_id'] = str(interstitial['_id'])
        return jsonify(interstitial)
    else:
        return jsonify({'message': 'Interstitial ad not found'})

@interstitial_blueprint.route('/interstitial/<interstitial_id>', methods=['PUT'])
def update_interstitial(interstitial_id):
    data = request.get_json()
    result = mongo.db.interstitials.update_one({'_id': ObjectId(interstitial_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Interstitial ad with ID {interstitial_id} updated successfully'})
    else:
        return jsonify({'message': 'Interstitial ad not found'})

@interstitial_blueprint.route('/interstitial/<interstitial_id>', methods=['DELETE'])
def delete_interstitial(interstitial_id):
    result = mongo.db.interstitials.delete_one({'_id': ObjectId(interstitial_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Interstitial ad with ID {interstitial_id} deleted successfully'})
    else:
        return jsonify({'message': 'Interstitial ad not found'})


# #########################Interstitial Ends#########################################

# #########################Interstitial_loads#########################################


# Assuming you have initialized the Flask-PyMongo instance as 'mongo'

@interstitial_blueprint.route('/interstitial_loads', methods=['POST'])
def create_interstitial_load():
    data = request.get_json()
    data['created_time'] = datetime.now().isoformat() 
    result = mongo.db.interstitial_loads.insert_one(data)
    return jsonify({'message': 'Interstitial load created successfully', 'id': str(result.inserted_id)})

@interstitial_blueprint.route('/interstitial_loads/<load_id>', methods=['GET'])
def get_interstitial_load(load_id):
    interstitial_load = mongo.db.interstitial_loads.find_one({'_id': ObjectId(load_id)})
    if interstitial_load:
        interstitial_load['_id'] = str(interstitial_load['_id'])
        return jsonify(interstitial_load)
    else:
        return jsonify({'message': 'Interstitial load not found'})

@interstitial_blueprint.route('/interstitial_loads/<load_id>', methods=['PUT'])
def update_interstitial_load(load_id):
    data = request.get_json()
    result = mongo.db.interstitial_loads.update_one({'_id': ObjectId(load_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Interstitial load with ID {load_id} updated successfully'})
    else:
        return jsonify({'message': 'Interstitial load not found'})

@interstitial_blueprint.route('/interstitial_loads/<load_id>', methods=['DELETE'])
def delete_interstitial_load(load_id):
    result = mongo.db.interstitial_loads.delete_one({'_id': ObjectId(load_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Interstitial load with ID {load_id} deleted successfully'})
    else:
        return jsonify({'message': 'Interstitial load not found'})

@interstitial_blueprint.route('/interstitial_clicks', methods=['POST'])
def create_interstitial_click():
    data = request.get_json()
    data['created_time'] = datetime.now().isoformat() 
    result = mongo.db.interstitial_clicks.insert_one(data)
    return jsonify({'message': 'Interstitial click created successfully', 'id': str(result.inserted_id)})

@interstitial_blueprint.route('/interstitial_clicks/<click_id>', methods=['GET'])
def get_interstitial_click(click_id):
    interstitial_click = mongo.db.interstitial_clicks.find_one({'_id': ObjectId(click_id)})
    if interstitial_click:
        interstitial_click['_id'] = str(interstitial_click['_id'])
        return jsonify(interstitial_click)
    else:
        return jsonify({'message': 'Interstitial click not found'})

@interstitial_blueprint.route('/interstitial_clicks/<click_id>', methods=['PUT'])
def update_interstitial_click(click_id):
    data = request.get_json()
    result = mongo.db.interstitial_clicks.update_one({'_id': ObjectId(click_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': f'Interstitial click with ID {click_id} updated successfully'})
    else:
        return jsonify({'message': 'Interstitial click not found'})

@interstitial_blueprint.route('/interstitial_clicks/<click_id>', methods=['DELETE'])
def delete_interstitial_click(click_id):
    result = mongo.db.interstitial_clicks.delete_one({'_id': ObjectId(click_id)})
    if result.deleted_count > 0:
        return jsonify({'message': f'Interstitial click with ID {click_id} deleted successfully'})
    else:
        return jsonify({'message': 'Interstitial click not found'})

# #########################Interstitial_loads Ends#########################################