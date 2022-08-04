from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import Form, validators, StringField, IntegerField, SelectField, DecimalField, RadioField 
from wtforms.validators import ValidationError 
import pandas as pd
import joblib, os
from utils.titanic import predict_survival

class TitanicForm(Form):
    """
    This is a form class to retrieve the input from user through form
    Inherits: request.form class
    """
    p_class = IntegerField(u'P Class (Valid Values: 1, 2, 3)', validators=[validators.input_required()])
    # sex = StringField(u'Sex (0: Female and 1: Male)', validators=[validators.input_required()])
    # Select = SelectField("gender", choices=[('female','female'), ('male','male')], validators=[validators.input_required()], coerce='str']
    sex = RadioField('Gender',
                       choices=[(1, 'Female'), (0, 'Male'), ],
                       validators=[validators.input_required()])

    # age = StringField(u'Age (For eg.: 24)', validators=[validators.input_required()])
    age = IntegerField('Age',validators=[validators.input_required()])
    has_sibsp = RadioField('Travelling with Siblings and/or Spouse',
                       choices=[("Sibling", 'Yes'), ("no", 'No'), ],
                       validators=[validators.input_required()])
    has_children = RadioField('Travelling with Children',
                       choices=[("Child", 'Yes'), ("no", 'No'), ],
                       validators=[validators.input_required()])
    fare = DecimalField(u'Fare (For eg.: 100)', validators=[validators.input_required()])
    embarked = RadioField('Embarked',coerce=int,
                       choices=[(0, "S"), (1, "C"), (2, "Q"), ],)


    def validate_age(form, field):
        if (field.data < 0) or (field.data > 110) :
            raise ValidationError("We're sorry, age must be in this range: [0, 110]")


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


    @app.route('/predict', methods=['GET', 'POST'])
    def predict():
        form = TitanicForm(request.form)
        
        # Checking if user submitted the form and the values are valid
        if request.method == 'POST' and form.validate():
            # Now save all values passed by user into variables
            p_class = form.p_class.data
            sex = int(form.sex.data)
            age = form.age.data
            has_sibsp = form.has_sibsp.data
            has_children = form.has_children.data

            fare = float(form.fare.data)
            embarked = form.embarked.data
            print([p_class, sex, age, [has_sibsp, has_children], fare, embarked])
            # Prediction
            prediction, predict_prob = predict_survival(passenger_class=p_class, sex=sex, age=age, company=[has_sibsp, has_children], fare=fare, embark_point=embarked)
            # print([int(p_class), int(sex), float(age), [has_sibsp, has_children], float(fare), int(embarked)])
            # # Creating input for model for predictions
            # predict_request = [int(p_class), int(sex), float(age), int(sibsp), int(parch), float(fare), int(embarked)]
            # predict_request = np.array(predict_request).reshape(1, -1)
            # # Passing the predictions to new view(template)
            return render_template('titanic/predictions.html', prediction=prediction, predict_prob=predict_prob)

        return render_template('titanic/predict.html', form=form)

    # return the object
    return app


# Running the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
