def threat_level(prediction):

    if prediction == "normal":
        return "NORMAL"

    elif prediction in ["neptune","smurf"]:
        return "CRITICAL"

    elif prediction in ["satan","ipsweep","nmap"]:
        return "HIGH"

    else:
        return "MEDIUM"
