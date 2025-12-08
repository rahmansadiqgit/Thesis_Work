import pickle

data = {
    "name": "Sadiq",
    "score": 95,
    "status": "active"
}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

print("data.pkl created successfully!")

