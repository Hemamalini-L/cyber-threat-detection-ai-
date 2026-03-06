from flask import Blueprint, request, jsonify
import pandas as pd

upload_route = Blueprint("upload_route", __name__)

@upload_route.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    df = pd.read_csv(file)

    return jsonify({
        "rows": len(df),
        "columns": list(df.columns)
    })
