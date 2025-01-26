import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.precision", 5)

DATA_URL = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/"

df = pd.read_csv(DATA_URL + "telecom_churn.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True))
print(df["Churn"].mean())

sns.countplot(x="International plan", hue="Churn", data=df)
plt.show()