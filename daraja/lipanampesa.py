import requests
import base64
from datetime import datetime

import keys
from encode_base64 import generate_password
from access_token import generate_access_token



def lipanampesa():
    access_token = generate_access_token()
    # print(f'access token:  {access_token}')
    
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    # print(f"formatted time: {formatted_time}")
    
    encoded_password = generate_password(formatted_time)
    # print(f"encoded password: {encoded_password}")
    
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    # print(f"headers: {headers}")

    request = {
        "BusinessShortCode": keys.BUSINESS_SHORT_CODE,
        "Password": encoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA":keys.PHONE_NUMBER,
        "PartyB":keys.BUSINESS_SHORT_CODE,
        "PhoneNumber":keys.PHONE_NUMBER,
        "CallBackURL":"https://cartera-sable.vercel.app/",
        "AccountReference":"ID-number",
        "TransactionDesc":"mpesa trial",
    }

    response = requests.post(api_url, headers=headers, json=request)

    print(response.text)
    
lipanampesa()