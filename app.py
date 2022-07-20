from flask import Flask, request, render_template
import pandas as pd
import joblib, os

# from utils import __required_classes_and_functions__


# Unpickle the ML model
estimator = joblib.load(os.path.join("ml", "__the_model__.pkl"))


# Declare a Flask app
app = Flask(__name__)

# Presentation page of the app
@app.route("/", methods=["GET", "POST"])
def home():

    return render_template(
        "homepage.html",
    )


@app.route("/demo", methods=["GET", "POST"])
def demo():

    # If a form is submitted
    if request.method == "POST":

        # Get values through input bars
        height = request.form.get("height")
        weight = request.form.get("weight")

        # Put inputs to dataframe
        X = pd.DataFrame([[height, weight]], columns=["Height", "Weight"])

        # Get predictions
        prediction = estimator.predict(X)[0]

    else:
        prediction = ""

    return render_template("demo.html", output=prediction)


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
