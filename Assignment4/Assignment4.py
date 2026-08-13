# ============================================================
# AIML Laboratory - Data Preparation
# Dataset: heart.csv
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split


# ============================================================
# 1. READ THE DATASET
# ============================================================

df = pd.read_csv("heart.csv")

print("\n==============================================")
print("DATASET LOADED SUCCESSFULLY")
print("==============================================")

print("\nFirst 8 rows of the dataset:")
print(df.head(8))


# 2. FIND SHAPE OF DATA

print("\n==============================================")
print("1. SHAPE OF DATA")
print("==============================================")

print("Shape of data:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])



# 3. FIND MISSING VALUES

print("\n==============================================")
print("2. MISSING VALUES")
print("==============================================")

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())

# 4. FIND DATA TYPE OF EACH COLUMN

print("\n==============================================")
print("3. DATA TYPE OF EACH COLUMN")
print("==============================================")

print(df.dtypes)

print("\nDetailed dataset information:")
df.info()

# 5. FIND NUMBER OF ZEROS IN EACH COLUMN


print("\n==============================================")
print("4. NUMBER OF ZEROS")
print("==============================================")

zero_count = (df == 0).sum(axis=0)

print("Number of zeros in each column:")
print(zero_count)

# 6. FIND MEAN AGE OF PATIENTS

print("\n==============================================")
print("5. MEAN AGE OF PATIENTS")
print("==============================================")

mean_age = df["age"].mean()

print("Mean age of patients:", mean_age)


# 7. EXTRACT AGE, SEX, CP, TRTBPS, CHOL

print("\n==============================================")
print("6. FEATURE EXTRACTION")
print("==============================================")

df2 = df[["age", "sex", "cp", "trtbps", "chol"]]

print("\nSelected columns:")
print(df2.head())

print("\nShape of selected data:")
print(df2.shape)



# 8. DIVIDE DATA INTO TRAINING AND TESTING
#    Training = 75%
#    Testing  = 25%


print("\n==============================================")
print("7. TRAINING AND TESTING DATA")
print("==============================================")

train_data, test_data = train_test_split(
    df2,
    test_size=0.25,
    random_state=42
)

print("\nTraining data:")
print(train_data.head())

print("\nTesting data:")
print(test_data.head())

print("\nTraining data shape:", train_data.shape)
print("Testing data shape:", test_data.shape)



# 9. DISPLAY COMPLETE TRAINING AND TESTING DATA


print("\n==============================================")
print("TRAINING DATA")
print("==============================================")

print(train_data)


print("\n==============================================")
print("TESTING DATA")
print("==============================================")

print(test_data)



# 10. FINAL SUMMARY


print("\n==============================================")
print("FINAL SUMMARY")
print("==============================================")

print("Original dataset shape :", df.shape)
print("Total missing values   :", df.isnull().sum().sum())
print("Mean age               :", mean_age)
print("Selected columns       :", list(df2.columns))
print("Training data shape    :", train_data.shape)
print("Testing data shape     :", test_data.shape)

print("\nData preparation completed successfully!")