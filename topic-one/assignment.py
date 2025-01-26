import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 100)

DATA_URL = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/"

data = pd.read_csv(DATA_URL + "adult.data.csv")
print(data.head())

print(data["sex"].value_counts())
print(data[data["sex"] == "Female"]["age"].mean())
print(float((data["native-country"] == "Germany").sum()) / data.shape[0])

ages1 = data[data["salary"] == ">50K"]["age"]
ages2 = data[data["salary"] == "<=50K"]["age"]
print(
    "The average age of the rich: {0} +- {1} years, poor - {2} +- {3} years.".format(
        round(ages1.mean()),
        round(ages1.std(), 1),
        round(ages2.mean()),
        round(ages2.std(), 1),
    )
)

print(data[data["salary"] == ">50K"]["education"].unique())

for (race, sex), sub_df in data.groupby(["race", "sex"]):
    print("Race: {0}, sex: {1}".format(race, sex))
    print(sub_df["age"].describe())

data[(data["sex"] == "Male")
     & (data["marital-status"].str.startswith("Married"))][
    "salary"
].value_counts(normalize=True)

data[
    (data["sex"] == "Male")
    & ~(data["marital-status"].str.startswith("Married"))
]["salary"].value_counts(normalize=True)

max_load = data["hours-per-week"].max()
print("Max time - {0} hours./week.".format(max_load))

num_workaholics = data[data["hours-per-week"] == max_load].shape[0]
print("Total number of such hard workers {0}".format(num_workaholics))

rich_share = (
    float(
        data[(data["hours-per-week"] == max_load) & (data["salary"] == ">50K")].shape[0]
    ) / num_workaholics
)
print("Percentage of rich among them {0}%".format(int(100 * rich_share)))