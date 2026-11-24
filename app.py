
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained ML pipeline
model = joblib.load("models/diabetes_prediction_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None

    if request.method == "POST":

        try:
            pregnancies = float(request.form["Pregnancies"])
            glucose = float(request.form["Glucose"])
            blood_pressure = float(request.form["BloodPressure"])
            skin_thickness = float(request.form["SkinThickness"])
            insulin = float(request.form["Insulin"])
            bmi = float(request.form["BMI"])
            diabetes_pedigree = float(request.form["DiabetesPedigreeFunction"])
            age = float(request.form["Age"])

            input_data = np.array([[
                pregnancies,
                glucose,
                blood_pressure,
                skin_thickness,
                insulin,
                bmi,
                diabetes_pedigree,
                age
            ]])

            result = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1] * 100

            if result == 1:
                prediction = "Higher predicted diabetes risk"
            else:
                prediction = "Lower predicted diabetes risk"

        except (ValueError, KeyError):
            prediction = "Please enter valid numeric values."

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)

