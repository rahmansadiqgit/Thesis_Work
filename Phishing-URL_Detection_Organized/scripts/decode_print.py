import pickle


with open("data.pkl", "rb") as f:  # 'rb' = read binary
    loaded_data = pickle.load(f)

print(loaded_data)
