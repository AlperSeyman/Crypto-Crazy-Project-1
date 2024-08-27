import requests



url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"

def crypto_data():
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    
crypto_response = crypto_data()     

def crypto_currency():
    for coin in crypto_response:
        print(coin["currency"])


coin_name = input("Enter a 'coin' name: ")
for coin in crypto_response:
    if coin_name == coin["currency"]:
        print(coin["price"])
    