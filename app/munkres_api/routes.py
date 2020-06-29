from app.munkres_api import munkres_bp
from munkres import Munkres
import json
from flask import request, jsonify
import sys


@munkres_bp.route("/process-matrix", methods=["POST"])
def process_matrix():
    """
    This api takes a list of lists and returns a list of coordinates. The list of list represents an n x m matrix of numbers. This function finds the path
    through the matrix that returns the highest value
    :return:
    """
    matrix = json.loads(request.data).get("matrix")
    cost_matrix = [[sys.maxsize - col for col in row] for row in matrix]
    m = Munkres()
    indexes = m.compute(cost_matrix)
    return jsonify(indexes)
