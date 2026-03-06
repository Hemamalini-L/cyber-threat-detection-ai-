from flask import Blueprint, request, jsonify
from utils.preprocessing import preprocess_data
from services.anomaly_detector import detect_anomaly
from utils.threat_levels import get_threat_level
from services.alert_system import generate_alert

detect_route = Blueprint("detect_route", __name__)

@detect_route.route("/detect", methods=["POST"])
def detect():

    file = request.files["file"]

    df = preprocess_data(file)

    predictions = detect_anomaly(df)

    results = []

    for p in predictions:

        threat = get_threat_level(p)
        alert = generate_alert(threat)

        results.append({
            "prediction": int(p),
            "threat_level": threat,
            "alert": alert
        })

    return jsonify(results)
