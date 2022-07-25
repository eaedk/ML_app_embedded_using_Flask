from flask import Flask, request, render_template
import pandas as pd
import joblib, os
import utils


# Unpickle the ML model
# estimator = joblib.load(os.path.join("ml", "__the_model__.pkl"))


def create_app():
    """This function with return the flak app object

    Returns:
    -------
    app : Flask
    The the Flask object that will bind all the endpoints of the app.
    """

    # Declare a Flask app
    app = Flask(__name__)

    # Presentation page of the app
    @app.route("/", methods=["GET", "POST"])
    def home():

        return render_template(
            "homepage.html",
        )

    # Demo page of the app
    @app.route("/demo", methods=["GET", "POST"])
    def demo():

        prediction = ""

        # If a form is submitted
        if request.method == "POST":
            pass
            # Get values through input bars

            # Put inputs to dataframe

            # Apply the preprocessing
            utils.preprocessing

            # Apply the feature engineering
            utils.feature_engineering

            # Get predictions
            # estimator.predict

        return render_template("demo.html", output=prediction)

    # example: an example
    @app.route("/example", methods=["GET", "POST"])
    def example():

        # If a form is submitted
        if request.method == "POST":

            # Get values through input bars
            var_001 = request.form.get("__var_001__")
            var_002 = request.form.get("__var_002__")
            var_003 = request.form.get("__var_003__")

            # Put inputs to dataframe
            df = pd.DataFrame(
                [[var_001, var_002, var_003]], columns=["var_001", "var_002", "var_003"]
            )
        else:
            df = pd.DataFrame()

        return render_template(
            "example.html",
            tables=[df.to_html(classes="data")],
            titles=df.columns.values,
        )

    # return the object
    return app


# Running the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
