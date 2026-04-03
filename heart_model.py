import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("../data/heart.csv")

X = data.drop("target", axis=1)
y = data["target"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("heart.pkl", "wb"))

print("Heart model saved!")