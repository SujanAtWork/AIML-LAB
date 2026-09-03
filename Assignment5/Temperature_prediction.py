# ============================================================
# AIML LAB ASSIGNMENT
# TEMPERATURE PREDICTION USING MULTIPLE LINEAR REGRESSION
#
# Input  : Year and Month Number
# Output : Predicted Average Temperature
#
# Features:
# 1. Data Cleaning
# 2. Missing Value Handling
# 3. Invalid Data Removal
# 4. Impossible Temperature Removal
# 5. Outlier Handling using IQR
# 6. Multiple Linear Regression
# 7. Model Evaluation
# 8. Actual vs Predicted Graph
# 9. Monthly Average Temperature Bar Graph
# 10. Future Temperature Prediction
# 11. Future Prediction Graph
# ============================================================


# ------------------------------------------------------------
# IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)


# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

file_path = "dataset/temperatures.csv"

df = pd.read_csv(file_path)

print("\n========================================")
print("        DATASET LOADED")
print("========================================")

print("Dataset shape:", df.shape)


# ------------------------------------------------------------
# 2. DISPLAY BASIC INFORMATION
# ------------------------------------------------------------

print("\nFirst 5 records:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 3. SELECT REQUIRED COLUMNS
# ------------------------------------------------------------

month_columns = [
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
]

required_columns = ["YEAR"] + month_columns

temperature_data = df[required_columns].copy()


# ------------------------------------------------------------
# 4. CONVERT YEAR AND TEMPERATURE COLUMNS TO NUMERIC
# ------------------------------------------------------------

temperature_data["YEAR"] = pd.to_numeric(
    temperature_data["YEAR"],
    errors="coerce"
)

for month in month_columns:

    temperature_data[month] = pd.to_numeric(
        temperature_data[month],
        errors="coerce"
    )


# ------------------------------------------------------------
# 5. REMOVE DUPLICATE RECORDS
# ------------------------------------------------------------

before_duplicates = len(temperature_data)

temperature_data = temperature_data.drop_duplicates()

after_duplicates = len(temperature_data)

duplicates_removed = (
    before_duplicates - after_duplicates
)

print("\nDuplicate records removed:",
      duplicates_removed)


# ------------------------------------------------------------
# 6. CONVERT WIDE FORMAT TO LONG FORMAT
# ------------------------------------------------------------

data_long = pd.melt(
    temperature_data,
    id_vars=["YEAR"],
    value_vars=month_columns,
    var_name="MONTH",
    value_name="TEMPERATURE"
)


# ------------------------------------------------------------
# 7. CONVERT MONTH NAMES TO MONTH NUMBERS
# ------------------------------------------------------------

month_mapping = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12
}

data_long["MONTH"] = data_long["MONTH"].map(
    month_mapping
)


# ------------------------------------------------------------
# 8. REMOVE MISSING VALUES
# ------------------------------------------------------------

before_missing = len(data_long)

data_long = data_long.dropna(
    subset=[
        "YEAR",
        "MONTH",
        "TEMPERATURE"
    ]
)

after_missing = len(data_long)

missing_removed = (
    before_missing - after_missing
)

print(
    "Rows removed because of missing values:",
    missing_removed
)


# ------------------------------------------------------------
# 9. REMOVE INVALID YEARS
# ------------------------------------------------------------

before_invalid_year = len(data_long)

data_long = data_long[
    (data_long["YEAR"] >= 1900) &
    (data_long["YEAR"] <= 2100)
]

after_invalid_year = len(data_long)

invalid_years_removed = (
    before_invalid_year - after_invalid_year
)

print(
    "Invalid year records removed:",
    invalid_years_removed
)


# ------------------------------------------------------------
# 10. REMOVE INVALID MONTHS
# ------------------------------------------------------------

before_invalid_month = len(data_long)

data_long = data_long[
    (data_long["MONTH"] >= 1) &
    (data_long["MONTH"] <= 12)
]

after_invalid_month = len(data_long)

invalid_months_removed = (
    before_invalid_month - after_invalid_month
)

print(
    "Invalid month records removed:",
    invalid_months_removed
)


# ------------------------------------------------------------
# 11. REMOVE IMPOSSIBLE TEMPERATURE VALUES
# ------------------------------------------------------------
#
# These limits are deliberately broad.
# They are intended to remove clearly invalid
# data-entry values rather than normal weather variation.
#
# If your dataset represents an extremely unusual climate,
# these limits can be adjusted.
# ------------------------------------------------------------

before_impossible = len(data_long)

data_long = data_long[
    (data_long["TEMPERATURE"] >= -90) &
    (data_long["TEMPERATURE"] <= 60)
]

after_impossible = len(data_long)

impossible_removed = (
    before_impossible - after_impossible
)

print(
    "Impossible temperature records removed:",
    impossible_removed
)


# ------------------------------------------------------------
# 12. HANDLE OUTLIERS USING MONTH-WISE IQR
# ------------------------------------------------------------
#
# Temperature is seasonal.
#
# Therefore, January values should be compared with
# other January values, February with February, etc.
#
# We use the IQR method separately for each month.
# ------------------------------------------------------------

before_outliers = len(data_long)


def remove_month_outliers(group):

    Q1 = group["TEMPERATURE"].quantile(0.25)

    Q3 = group["TEMPERATURE"].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR

    upper_bound = Q3 + 1.5 * IQR

    return group[
        (group["TEMPERATURE"] >= lower_bound) &
        (group["TEMPERATURE"] <= upper_bound)
    ]


data_long = (
    data_long
    .groupby("MONTH", group_keys=False)
    .apply(remove_month_outliers)
    .reset_index(drop=True)
)


after_outliers = len(data_long)

outliers_removed = (
    before_outliers - after_outliers
)

print(
    "Outlier records removed:",
    outliers_removed
)


# ------------------------------------------------------------
# 13. SORT DATA
# ------------------------------------------------------------

data_long = data_long.sort_values(
    ["YEAR", "MONTH"]
).reset_index(drop=True)


# ------------------------------------------------------------
# 14. DISPLAY CLEANED DATA
# ------------------------------------------------------------

print("\n========================================")
print("        CLEANED DATASET")
print("========================================")

print(
    data_long.head(15)
)

print(
    "\nFinal dataset shape:",
    data_long.shape
)


# ------------------------------------------------------------
# 15. DISPLAY CLEANING SUMMARY
# ------------------------------------------------------------

print("\n========================================")
print("        DATA CLEANING SUMMARY")
print("========================================")

print(
    "Original records:",
    len(df) * 12
)

print(
    "Final records:",
    len(data_long)
)

print(
    "Total records removed:",
    (len(df) * 12) - len(data_long)
)


# ------------------------------------------------------------
# 16. CREATE SEASONAL FEATURES
# ------------------------------------------------------------
#
# MONTH_SIN and MONTH_COS allow the model to understand
# the cyclic nature of months.
#
# December and January are treated as close to each other.
# ------------------------------------------------------------

data_long["MONTH_SIN"] = np.sin(
    2 * np.pi * data_long["MONTH"] / 12
)

data_long["MONTH_COS"] = np.cos(
    2 * np.pi * data_long["MONTH"] / 12
)


# ------------------------------------------------------------
# 17. DEFINE FEATURES AND TARGET
# ------------------------------------------------------------

X = data_long[
    [
        "YEAR",
        "MONTH_SIN",
        "MONTH_COS"
    ]
]

y = data_long["TEMPERATURE"]


# ------------------------------------------------------------
# 18. TIME-BASED TRAIN/TEST SPLIT
# ------------------------------------------------------------
#
# Instead of randomly splitting the data, we use older years
# for training and newer years for testing.
#
# This is more suitable for future prediction.
# ------------------------------------------------------------

unique_years = sorted(
    data_long["YEAR"].unique()
)

number_of_years = len(unique_years)

split_index = int(
    number_of_years * 0.80
)

train_years = unique_years[:split_index]

test_years = unique_years[split_index:]


X_train = data_long[
    data_long["YEAR"].isin(train_years)
][
    [
        "YEAR",
        "MONTH_SIN",
        "MONTH_COS"
    ]
]

y_train = data_long[
    data_long["YEAR"].isin(train_years)
]["TEMPERATURE"]


X_test = data_long[
    data_long["YEAR"].isin(test_years)
][
    [
        "YEAR",
        "MONTH_SIN",
        "MONTH_COS"
    ]
]

y_test = data_long[
    data_long["YEAR"].isin(test_years)
]["TEMPERATURE"]


print("\n========================================")
print("        TRAIN / TEST SPLIT")
print("========================================")

print(
    "Training years:",
    min(train_years),
    "to",
    max(train_years)
)

print(
    "Testing years:",
    min(test_years),
    "to",
    max(test_years)
)

print(
    "Training samples:",
    len(X_train)
)

print(
    "Testing samples:",
    len(X_test)
)


# ------------------------------------------------------------
# 19. CREATE LINEAR REGRESSION MODEL
# ------------------------------------------------------------

model = LinearRegression()


# ------------------------------------------------------------
# 20. TRAIN MODEL
# ------------------------------------------------------------

model.fit(
    X_train,
    y_train
)

print(
    "\nLinear Regression model trained successfully!"
)


# ------------------------------------------------------------
# 21. DISPLAY MODEL PARAMETERS
# ------------------------------------------------------------

print("\n========================================")
print("        MODEL PARAMETERS")
print("========================================")

print(
    "Intercept:",
    model.intercept_
)

print(
    "Year coefficient:",
    model.coef_[0]
)

print(
    "Month SIN coefficient:",
    model.coef_[1]
)

print(
    "Month COS coefficient:",
    model.coef_[2]
)


# ------------------------------------------------------------
# 22. PREDICT TEST DATA
# ------------------------------------------------------------

y_pred = model.predict(
    X_test
)


# ------------------------------------------------------------
# 23. MODEL EVALUATION
# ------------------------------------------------------------

mse = mean_squared_error(
    y_test,
    y_pred
)

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    y_pred
)


print("\n========================================")
print("        MODEL PERFORMANCE")
print("========================================")

print(
    f"Mean Squared Error (MSE)  : {mse:.4f}"
)

print(
    f"Mean Absolute Error (MAE) : {mae:.4f}"
)

print(
    f"Root Mean Squared Error   : {rmse:.4f}"
)

print(
    f"R-Square (R²)             : {r2:.4f}"
)

print("========================================")


# ------------------------------------------------------------
# 24. ACTUAL VS PREDICTED DATA
# ------------------------------------------------------------

test_results = data_long[
    data_long["YEAR"].isin(test_years)
][
    [
        "YEAR",
        "MONTH",
        "TEMPERATURE"
    ]
].copy()

test_results[
    "PREDICTED_TEMPERATURE"
] = y_pred

test_results = test_results.sort_values(
    ["YEAR", "MONTH"]
)


print("\n========================================")
print("        ACTUAL VS PREDICTED")
print("========================================")

print(
    test_results.to_string(index=False)
)


# ------------------------------------------------------------
# 25. GRAPH 1
# ACTUAL VS PREDICTED TEMPERATURE
# ------------------------------------------------------------

plt.figure(
    figsize=(10, 6)
)

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)


# Perfect prediction line

min_value = min(
    y_test.min(),
    y_pred.min()
)

max_value = max(
    y_test.max(),
    y_pred.max()
)

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--",
    color="red",
    label="Perfect Prediction"
)


plt.xlabel(
    "Actual Temperature (°C)"
)

plt.ylabel(
    "Predicted Temperature (°C)"
)

plt.title(
    "Actual vs Predicted Temperature"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 26. GRAPH 2
# AVERAGE TEMPERATURE FOR EACH MONTH
# ACROSS ALL YEARS
# ------------------------------------------------------------

monthly_average = (
    data_long
    .groupby("MONTH")["TEMPERATURE"]
    .mean()
)


month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


plt.figure(
    figsize=(12, 6)
)

plt.bar(
    month_names,
    monthly_average.values
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Average Temperature (°C)"
)

plt.title(
    "Average Temperature of Each Month Across All Years"
)

plt.xticks(
    rotation=45
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 27. FUTURE PREDICTION FUNCTION
# ------------------------------------------------------------

def predict_temperature(
    year,
    month
):

    month_sin = np.sin(
        2 * np.pi * month / 12
    )

    month_cos = np.cos(
        2 * np.pi * month / 12
    )

    input_data = pd.DataFrame({
        "YEAR": [year],
        "MONTH_SIN": [month_sin],
        "MONTH_COS": [month_cos]
    })

    prediction = model.predict(
        input_data
    )[0]

    return prediction


# ------------------------------------------------------------
# 28. FUTURE TEMPERATURE PREDICTIONS
# ------------------------------------------------------------
#
# This creates predictions for every month from the year
# after the dataset ends up to 2030.
#
# Change future_end_year if you want another year.
# ------------------------------------------------------------

max_year = int(
    data_long["YEAR"].max()
)

min_year = int(
    data_long["YEAR"].min()
)

future_start_year = max_year + 1

future_end_year = 2030

future_results = []


for year in range(
    future_start_year,
    future_end_year + 1
):

    for month in range(1, 13):

        predicted_temperature = (
            predict_temperature(
                year,
                month
            )
        )

        future_results.append({

            "YEAR": year,

            "MONTH": month,

            "PREDICTED_TEMPERATURE":
                predicted_temperature
        })


future_df = pd.DataFrame(
    future_results
)


# ------------------------------------------------------------
# 29. DISPLAY FUTURE PREDICTIONS
# ------------------------------------------------------------

print("\n========================================")
print("        FUTURE PREDICTIONS")
print("========================================")

print(
    future_df.to_string(index=False)
)


# ------------------------------------------------------------
# 30. GRAPH 3
# FUTURE MONTHLY TEMPERATURE
# ------------------------------------------------------------

plt.figure(
    figsize=(14, 6)
)

plt.plot(
    range(len(future_df)),
    future_df["PREDICTED_TEMPERATURE"],
    linewidth=1.5
)

plt.xlabel(
    "Future Months"
)

plt.ylabel(
    "Predicted Temperature (°C)"
)

plt.title(
    f"Future Monthly Temperature Prediction "
    f"({future_start_year}-{future_end_year})"
)

plt.grid(True)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 31. USER INPUT
# PREDICT TEMPERATURE FOR A SPECIFIC YEAR AND MONTH
# ------------------------------------------------------------

print("\n========================================")
print("     TEMPERATURE PREDICTION SYSTEM")
print("========================================")

print(
    f"Historical data available from "
    f"{min_year} to {max_year}."
)

print(
    "You can enter a future year."
)

print(
    "Example: 2020, 2025, 2030, 2040, etc."
)


try:

    # --------------------------------------------------------
    # USER ENTERS YEAR
    # --------------------------------------------------------

    year = int(
        input(
            "\nEnter year to predict: "
        )
    )


    # --------------------------------------------------------
    # USER ENTERS MONTH
    # --------------------------------------------------------

    month = int(
        input(
            "Enter month number (1-12): "
        )
    )


    # --------------------------------------------------------
    # VALIDATE YEAR
    # --------------------------------------------------------

    if year < min_year:

        print(
            "\nInvalid year!"
        )

        print(
            f"Please enter a year greater than "
            f"or equal to {min_year}."
        )


    # --------------------------------------------------------
    # VALIDATE MONTH
    # --------------------------------------------------------

    elif month < 1 or month > 12:

        print(
            "\nInvalid month!"
        )

        print(
            "Please enter a number between 1 and 12."
        )


    # --------------------------------------------------------
    # MAKE PREDICTION
    # --------------------------------------------------------

    else:

        predicted_temperature = (
            predict_temperature(
                year,
                month
            )
        )


        # ----------------------------------------------------
        # DISPLAY RESULT
        # ----------------------------------------------------

        print("\n========================================")
        print("        PREDICTION RESULT")
        print("========================================")

        print(
            f"Year              : {year}"
        )

        print(
            f"Month             : "
            f"{month} ({month_names[month - 1]})"
        )

        print(
            f"Predicted Average : "
            f"{predicted_temperature:.2f} °C"
        )

        print("========================================")


        # ----------------------------------------------------
        # INDICATE FUTURE PREDICTION
        # ----------------------------------------------------

        if year > max_year:

            print(
                f"\nThis is a FUTURE prediction."
            )

            print(
                f"The historical dataset ends at "
                f"{max_year}."
            )

            print(
                f"The model predicted the average "
                f"temperature for "
                f"{month_names[month - 1]} {year}."
            )

        else:

            print(
                f"\nThis year is within the historical "
                f"dataset range."
            )


# ------------------------------------------------------------
# 32. HANDLE INVALID USER INPUT
# ------------------------------------------------------------

except ValueError:

    print(
        "\nInvalid input!"
    )

    print(
        "Please enter numbers only."
    )
