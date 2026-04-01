from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

patients = []

def get_priority(data):
    age = int(data["age"])
    severity = int(data["severity"])
    symptom = data["symptom"]
    duration = int(data["duration"])

    if symptom == "chest pain" and age > 40:
        return 3, "Chest pain + age risk"
    elif severity >= 8:
        return 3, "High severity"
    elif symptom == "fever" and duration > 3:
        return 2, "Prolonged fever"
    else:
        return 1, "Normal condition"

@app.route("/add", methods=["POST"])
def add_patient():
    data = request.json

    priority, reason = get_priority(data)

    patient = {
        "name": data["name"],
        "priority": priority,
        "reason": reason
    }

    patients.append(patient)

    # sort by priority
    patients.sort(key=lambda x: x["priority"], reverse=True)

    return jsonify(patients)

if __name__ == "__main__":
    app.run(debug=True)