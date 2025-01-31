def read_api_key():
    with open("../helius_api.txt", "r") as file:
        return file.read().strip()


HELIUS_KEY = read_api_key()
