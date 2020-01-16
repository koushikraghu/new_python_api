from flask import Blueprint
from flask import jsonify
from flask import request
from controller.deletion_controller import Deletion_function
# Blueprint obj
bp = Blueprint(__name__,"deletion")

# Deletion_function obj
dc = Deletion_function()

@bp.route("/deletion",method = ["POST"])
def deletion():
    '''deleting a record'''
    data = request.get_json()
    name = data["name"]
    address = data["addr"]
    result = dc.delete(name,address)
    return jsonify(result)

