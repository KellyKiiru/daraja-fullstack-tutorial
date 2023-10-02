import requests
import base64
from datetime import datetime

from . import keys

unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")




def lipanampesa():
    access_token = "access-token"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.BUSINESS_SHORT_CODE,
        "Password": "<PASSWORD>",
        "Timestamp": "1588835661",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA":keys.PARTY_A,
        "PartyB":keys.BUSINESS_SHORT_CODE,
        "PhoneNumber":"",
        "CallBackUrl":"http://127.0.0.1:8000/",
        "AccountReference":"ID-number",
        "TransactionDesc":"",
    }

    response = requests.post(api_url, headers=headers, json=request)

    print(response.json())