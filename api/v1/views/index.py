#!/usr/bin/python3
"""Create an endpoint that retrieves the
number of each objects by type"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def r_json():
    """a route for return JSON status """
    return jsonify(status='OK')
