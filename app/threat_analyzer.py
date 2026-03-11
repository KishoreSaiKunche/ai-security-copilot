def detect_threat(log):

    if "failed login" in log["event"].lower():
        if log["count"] > 20:
            return "Possible Brute Force Attack"

    if "port" in log["event"].lower():
        return "Possible Port Scanning"

    return "Normal Activity"