from flask import Flask, request, render_template

app = Flask(__name__)

patients = []

def get_priority(age, symptom, severity, duration):
    age = int(age)
    severity = int(severity)
    duration = int(duration)
    symptom = symptom.lower()

    if symptom in ["chest pain"]:
        return 3, "Emergency", "Dr.Ajeenkya Pawar,Cardiologist"

    if symptom in ["breathing problem"]:
        return 3, "Emergency", "Dr.chandan pardeshi,Pulmonologist"

    if severity >= 8:
        return 3, "Emergency", "Dr.Aaditi Mestry, Emergency Specialist"

    if symptom == "fever" and duration > 3:
        return 2, "Urgent", "Dr.Manisha Pardeshi, General Physician"

    if symptom in ["vomiting", "dizziness"]:
        return 2, "Urgent", "Dr.Suman Jadhav, General Physician"

    if age > 60 and severity > 5:
        return 2, "Urgent", "Dr.Balaji Rupnar, Geriatric Specialist"

    return 1, "Normal", "Dr.Rahul More, General Physician"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        symptom = request.form["symptom"]
        severity = request.form["severity"]
        duration = request.form["duration"]
        
        priority, level, doctor = get_priority(age, symptom, severity, duration)

        patient = {
            "name": name,
            "priority": priority,
            "level": level,
            "doctor": doctor
}

        patients.append(patient)
        patients.sort(key=lambda x: x["priority"], reverse=True)

    return render_template("index.html", patients=patients)

if __name__ == "__main__":
    app.run(debug=True)