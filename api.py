from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("../feature of ML/Heart_Attack_Disease_Prediction.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        age = float(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])

        if age < 0:
            return render_template(
                "result.html",
                prediction="❌ Age cannot be negative.",
                confidence=0
            )

        if trestbps <= 0:
            return render_template(
                "result.html",
                prediction="❌ Invalid Blood Pressure.",
                confidence=0
            )

        if chol <= 0:
            return render_template(
                "result.html",
                prediction="❌ Invalid Cholesterol.",
                confidence=0
            )

        new_patient = [[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]]

        prediction = model.predict(new_patient)

        probability = model.predict_proba(new_patient)

        confidence = round(max(probability[0]) * 100, 2)

        if prediction[0] == 1:
            result = "❤️ Heart Disease Detected"
        else:
            result = "💚 No Heart Disease"

        return render_template(
            "result.html",
            prediction=result,
            confidence=confidence
        )

    except ValueError:

        return render_template(
            "result.html",
            prediction="❌ Invalid Input! Please enter valid numbers.",
            confidence=0
        )


if __name__ == "__main__":
    app.run(debug=True)