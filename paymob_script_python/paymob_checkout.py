import requests
import json
import os
from dotenv import load_dotenv
import webbrowser

# Load variables from .env
load_dotenv()

# Get values from .env
secret_key = os.getenv("PAYMOB_SECRET_KEY")
public_key = os.getenv("PAYMOB_PUBLIC_KEY")
integration_id = int(os.getenv("PAYMOB_INTEGRATION_ID"))
notification_url = os.getenv("PAYMOB_NOTIFICATION_URL")

url = "https://accept.paymob.com/v1/intention/"

payload = {
    "amount": 1000,  # in cents EGP * 100
    "currency": "EGP",
    "payment_methods": [integration_id],  # Integration ID from .env file
    "items": [
        {
            "name": "Item name 1",
            "amount": 1000,
            "description": "Watch",
            "quantity": 1
        }
    ],
    "billing_data": {
        "apartment": "NA",
        "email": "AmmarSadek@gmail.com",
        "floor": "NA",
        "first_name": "Ammar",
        "last_name": "Sadek",
        "street": "938, Al-Jadeed Bldg",
        "building": "939",
        "phone_number": "+201234567890",
        "shipping_method": "PKG",
        "postal_code": "NA",
        "city": "Cairo",
        "country": "EG",
        "state": "Cairo"
    },
    "extras": {
        "ee": 22
    },

    "expiration": 3600,
    "notification_url": notification_url,
    "redirection_url": "https://www.google.com/"
}

# Taking the secret Key from .env file
headers = {
    "Authorization": f"Token {secret_key}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=payload)

data = response.json()
client_secret = data.get("client_secret")
checkout_url = f"https://accept.paymob.com/unifiedcheckout/?publicKey={public_key}&clientSecret={client_secret}"

print("HTTPS Status Codes: ", response.status_code)
print(data)
print("Client Secret:", client_secret)
print("Checkout URL:", checkout_url)

webbrowser.open(checkout_url)
