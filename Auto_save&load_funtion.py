
# Step 1: Saving data to a file
def save_data(filename, data):
    import pickle
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Step 2: Loading data from a file
def load_data(filename):
    import pickle
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        # Handle the case where the file doesn't exist (initial run)
        return None