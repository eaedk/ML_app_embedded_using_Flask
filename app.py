from flask import Flask, request, render_template
from wtforms import Form, validators, StringField
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

    class PredictorsForm(Form):
        """
        This is a form class to retrieve the input from user through form
        Inherits: request.form class
        """
        p_class = StringField(u'P Class (Valid Values: 1, 2, 3)', validators=[validators.input_required()])
        sex = StringField(u'Sex (0: Female and 1: Male)', validators=[validators.input_required()])
        age = StringField(u'Age (For eg.: 24)', validators=[validators.input_required()])
        sibsp = StringField(u'Siblings and Spouse Count (For eg.: 3)', validators=[validators.input_required()])
        parch = StringField(u'Parch (Valid Values: 0, 1, 2, 3, 4, 5, 6)', validators=[validators.input_required()])
        fare = StringField(u'Fare (For eg.: 100)', validators=[validators.input_required()])
        embarked = StringField(u'Embarked (Valid Values: 0, 1, 2)', validators=[validators.input_required()])

    @app.route('/predict', methods=['GET', 'POST'])
    def predict():
        form = PredictorsForm(request.form)
        
        # Checking if user submitted the form and the values are valid
        if request.method == 'POST' and form.validate():
            # Now save all values passed by user into variables
            p_class = form.p_class.data
            sex = form.sex.data
            age = form.age.data
            sibsp = form.sibsp.data
            parch = form.parch.data
            fare = form.fare.data
            embarked = form.embarked.data

            # # Creating input for model for predictions
            # predict_request = [int(p_class), int(sex), float(age), int(sibsp), int(parch), float(fare), int(embarked)]
            # predict_request = np.array(predict_request).reshape(1, -1)

            # # Class predictions from the model
            # # # prediction = model.predict(predict_request)
            # prediction = str(prediction[0])

            # # Survival Probability from the model
            # predict_prob = model.predict_proba(predict_request)
            # predict_prob = str(predict_prob[0][1])

            # # Passing the predictions to new view(template)
            # return render_template('titanic/predictions.html', prediction=prediction, predict_prob=predict_prob)

        return render_template('titanic/predict.html', form=form)

    # return the object
    return app


# Running the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
