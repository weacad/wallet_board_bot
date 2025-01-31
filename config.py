def read_api_key(filepath):
    with open(filepath, "r") as file:
        return file.read().strip()


HELIUS_KEY = read_api_key("../helius_api.txt")
