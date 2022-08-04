import pandas as pd
import pickle, os

def encode_age(df):
    df.Age = df.Age.fillna(-0.5)
    bins = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
    categories = pd.cut(df.Age, bins, labels=False)
    df.Age = categories
    return df


def encode_fare(df):
    df.Fare = df.Fare.fillna(-0.5)
    bins = (-1, 0, 8, 15, 31, 1000)
    categories = pd.cut(df.Fare, bins, labels=False)
    df.Fare = categories
    return df


def encode_df(df):
    df = encode_age(df)
    df = encode_fare(df)
    sex_mapping = {"male": 0, "female": 1}
    df = df.replace({"Sex": sex_mapping})
    embark_mapping = {"S": 1, "C": 2, "Q": 3}
    df = df.replace({"Embarked": embark_mapping})
    df.Embarked = df.Embarked.fillna(0)
    df["Company"] = 0
    df.loc[(df["SibSp"] > 0), "Company"] = 1
    df.loc[(df["Parch"] > 0), "Company"] = 2
    df.loc[(df["SibSp"] > 0) & (df["Parch"] > 0), "Company"] = 3
    df = df[
        [
            "PassengerId",
            "Pclass",
            "Sex",
            "Age",
            "Fare",
            "Embarked",
            "Company",
            "Survived",
        ]
    ]
    return df

DIRPATH = os.path.dirname(os.path.relpath(__file__))
model_path = os.path.join(DIRPATH, "..", "ml", "titanic", "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)


def predict_survival(passenger_class, sex, age, company, fare, embark_point):
    if passenger_class is None or embark_point is None:
        return None
    df = pd.DataFrame.from_dict(
        {
            "Pclass": [passenger_class + 1],
            "Sex": [sex], # 0 if is_male else 1
            "Age": [age],
            "Company": [
                (1 if "Sibling" in company else 0) + (2 if "Child" in company else 0)
            ],
            "Fare": [fare],
            "Embarked": [embark_point + 1],
        }
    )
    df = encode_age(df)
    df = encode_fare(df)
    # pred = model.predict_proba(df)[0]
    # {"Perishes": float(pred[0]), "Survives": float(pred[1])}
    
    # # Class predictions from the model
    prediction = model.predict(df)
    prediction = str(prediction[0])

    # Survival Probability from the model
    predict_prob = model.predict_proba(df)
    predict_prob = str(predict_prob[0][1])

    return prediction, predict_prob