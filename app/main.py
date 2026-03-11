from fastapi import FastAPI
from app.log_parser import load_logs
from app.threat_analyzer import detect_threat

app = FastAPI()

@app.get("/investigate")
def investigate():

    logs = load_logs("data/sample_logs.json")

    results = []

    for log in logs:
        threat = detect_threat(log)

        results.append({
            "log": log,
            "threat": threat
        })

    return results