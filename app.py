from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST" ,"GET"])
def predict():

    age = request.form["age"]

    return render_template(
        "result.html",
        name=age
    )


if __name__ == "__main__":
    app.run(debug=True)