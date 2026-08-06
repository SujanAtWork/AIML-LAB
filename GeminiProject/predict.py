import pandas as pd
from sklearn.ensemble import RandomForestRegressor


# Dataset path

FILE_PATH = "dataset/inflation interest unemployment.csv"


# Load dataset once

df = pd.read_csv(FILE_PATH)



def predict_inflation(country, year):

    # Select country data

    data = df[
        df["country"].str.lower() == country.lower()
    ]


    # Remove missing inflation values

    data = data.dropna(
        subset=[
            "Inflation, consumer prices (annual %)"
        ]
    )


    if len(data) < 5:
        return None



    # Input feature

    X = data[["year"]]


    # Output value

    y = data[
        "Inflation, consumer prices (annual %)"
    ]



    # Train model

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )


    model.fit(X, y)



    # Future year

    future = pd.DataFrame(
        {
            "year":[year]
        }
    )


    prediction = model.predict(
        future
    )


    return prediction[0]



# Test when running directly

if __name__ == "__main__":

    result = predict_inflation(
        "India",
        2030
    )

    print(
        "Predicted inflation:",
        result
    )