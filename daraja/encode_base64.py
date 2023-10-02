import base64
import keys

def generate_password(date):
    # Convert keys.LIPANAMPESA_PASSKEY and keys.BUSINESS_SHORT_CODE to strings
    passkey = str(keys.LIPANAMPESA_PASSKEY)
    business_short_code = str(keys.BUSINESS_SHORT_CODE)
    
    data_to_encode = passkey + date + business_short_code
    
    encoded_string = base64.b64encode(data_to_encode.encode())
    
    encoded_password = encoded_string.decode("utf-8")
    
    return encoded_password
