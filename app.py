from flask import Flask, request, render_template

app = Flask(__name__)

patients = []

def get_priority(age, symptom, severity, duration):
    age = int(age)
    severity = int(severity)
    duration = int(duration)
    symptom = symptom.lower()

    if symptom in ["chest pain", "heart pain"]:
        return 3, "Critical: chest pain, Dr.Ajjenkya pawar,Cardiologist"

    if symptom in ["breathing problem", "shortness of breath"]:
        return 3, "Critical: breathing issue, Dr.Suman Jadhav,Pulmonologist"

    if severity >= 8:
        return 3, "High severity, ICU Recomandation"
    
    if age < 8:
        return 3, "Emergency, Dr.Aaditi Mestry,Pediatrician"

    if symptom in ["fever"] and duration > 3:
        return 2, "Prolonged fever,Dr.Chandan Pardeshi,General physician"

    if symptom in ["vomiting", "dizziness"]:
        return 2, "Moderate risk symptoms,Dr.Manisha Pardeshi,General physician"

    if age > 60 and severity > 5:
        return 2, "Age risk, Dr.Balaji Rupnar,Geriatrician"
    
    

    return 1, "Stable condition, OPD Recomadition"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        symptom = request.form["symptom"]
        severity = request.form["severity"]
        duration = request.form["duration"]

        priority, reason = get_priority(age, symptom, severity, duration)

        patient = {
            "name": name,
            "priority": priority,
            "reason": reason
        }

        patients.append(patient)
        patients.sort(key=lambda x: x["priority"], reverse=True)

    return render_template("index.html", patients=patients)

if __name__ == "__main__":
    app.run(debug=True)