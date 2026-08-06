import os
import re
import pandas as pd
from dotenv import load_dotenv
from google import genai

from predict import predict_inflation



# ==========================
# Gemini API
# ==========================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    print("API key missing")
    exit()


client = genai.Client(
    api_key=API_KEY
)



# ==========================
# Load Dataset
# ==========================

FILE_PATH = "dataset/inflation interest unemployment.csv"


df = pd.read_csv(FILE_PATH)


print("Dataset loaded successfully!")



# ==========================
# Chatbot
# ==========================


print("\n===================================")
print(" Economic Data AI Chatbot ")
print(" Ask about inflation, interest, unemployment ")
print(" Type exit to quit ")
print("===================================")



while True:


    user = input("\nYou: ")



    if user.lower() in ["exit","bye"]:

        print(
            "Bot: Goodbye!"
        )

        break



    # ==================================
    # Future prediction detection
    # ==================================


    future_words = [
        "predict",
        "future",
        "forecast",
        "will be",
        "expected"
    ]


    is_prediction = False


    for word in future_words:

        if word in user.lower():

            is_prediction = True
            break



    if is_prediction:


        # Find year

        years = re.findall(
            r"\b\d{4}\b",
            user
        )


        if len(years) == 0:

            print(
                "Bot: Please provide a future year."
            )

            continue


        future_year = int(years[0])



        # Country detection


        country = None


        for c in df["country"].unique():

            if c.lower() in user.lower():

                country = c
                break



        # Country aliases

        if "india" in user.lower():

            country = "India"


        if "usa" in user.lower():

            country = "United States"



        if country is None:

            print(
                "Bot: Country not found."
            )

            continue



        prediction = predict_inflation(
            country,
            future_year
        )



        if prediction is None:

            print(
                "Bot: Prediction cannot be generated."
            )

        else:

            print(
                f"Bot: Predicted inflation for {country} in {future_year} is approximately {prediction:.2f}%"
            )


        continue




    # ==================================
    # Historical dataset questions
    # ==================================


    search_data = df.copy()



    # Country filtering

    country = None


    for c in df["country"].unique():

        if c.lower() in user.lower():

            country = c
            break



    if country:

        search_data = search_data[
            search_data["country"] == country
        ]



    # Year filtering


    years = re.findall(
        r"\b\d{4}\b",
        user
    )


    if len(years):

        year = int(years[0])

        search_data = search_data[
            search_data["year"] == year
        ]



    search_data = search_data.head(10)



    dataset_info = search_data.to_string(
        index=False
    )



    prompt = f"""

Answer only using this dataset.

Dataset:

{dataset_info}


Question:

{user}

"""


    try:


        response = client.models.generate_content(

            model="gemini-3.6-flash",

            contents=prompt

        )


        print(
            "Bot:",
            response.text
        )


    except Exception as e:

        print(
            "Error:",
            e
        )