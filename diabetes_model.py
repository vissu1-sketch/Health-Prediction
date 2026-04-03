import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("../data/diabetes.csv")

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

pickle.dump(model, open("diabetes.pkl", "wb"))

print("Diabetes model saved!")