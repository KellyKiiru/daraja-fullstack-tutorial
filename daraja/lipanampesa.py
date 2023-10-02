import requests

access_token = "access-token"
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = {"Authorization": "Bearer %s" % access_token}

request = {
    "BusinessShortCode": "601718",
    "Password": "<PASSWORD>",
    "Timestamp": "1588835661",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA":"",
    "PartyB":"",
    "PhoneNumber":"",
    "CallBackUrl":"http://127.0.0.1:8000/",
    "AccountReference":"ID-number",
    "TransactionDesc":"",
}

response = requests.post(api_url, headers=headers, json=request)

print(response.json())