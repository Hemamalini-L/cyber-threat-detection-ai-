def generate_alert(threat):

    if threat == "Critical Intrusion":
        return "🚨 DEFENCE ALERT: Possible Cyber Attack Detected"

    elif threat == "Medium Risk Attack":
        return "⚠️ Suspicious Activity Detected"

    elif threat == "Low Risk Threat":
        return "⚡ Minor Network Anomaly"

    else:
        return "✅ Network Safe"
