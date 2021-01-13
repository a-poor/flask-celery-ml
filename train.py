
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "model.pkl"

print("Loading data...")
X, y = load_iris(return_X_y=True)

print("Building & training model...")
model = LogisticRegression(max_iter=100_000)
model.fit(X,y)

print(f"Saving model to \"{MODEL_PATH}\"...")
with open(MODEL_PATH,"wb") as f:
    pickle.dump(model,f)

print("Done.")

