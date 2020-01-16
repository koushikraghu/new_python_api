from flask import Blueprint
from flask import request
from flask import jsonify
from controller.insertion_controller import Insertion_Controller

'''blueprint object'''
bp = Blueprint(__name__,"insertion")

#insertion controller object
ic = Insertion_Controller()

@bp.route("/insertion",methods=['POST'])
def insertion():
    data = request.get_json()
    name = data['name']
    address = data['addr']
    result = ic.insert(name,address)
    return jsonify(result)

