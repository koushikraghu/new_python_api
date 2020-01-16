from flask import Blueprint
from flask import request
from flask import jsonify
from controller.updation_controller import Updation_controller

#creating blue print obj
bp = Blueprint(__name__,"updation")

#creating Updation_controller obj
uc = Updation_controller()

@bp.route("/updation",method = ["POST"])
def updation():
    '''updating record'''
    data = request.get_json()
    name = data["name"]
    address = data["addr"]
    result = uc.update(name,address)
    return jsonify(result)

