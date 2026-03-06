def get_threat_level(prediction):

    if prediction == 0:
        return "Normal Traffic"

    elif prediction == 1:
        return "Low Risk Threat"

    elif prediction == 2:
        return "Medium Risk Attack"

    else:
        return "Critical Intrusion"
