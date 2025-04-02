import requests

# Send Bulk SMS
# https://developers.africastalking.com/docs/sms/sending/bulk
def send_bulk_sms(api_key, username, message, senderId, phoneNumbers, maskedNumber=None, telco=None):

    # prep request (url, header, payload)
    url = "https://api.africastalking.com/version1/messaging/bulk"

    header = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "apiKey": api_key
    }

    payload = {
        "username": username,
        "message": message,
        "senderId": senderId,
        "phoneNumbers": phoneNumbers,
    }

    # optional payload params
    if maskedNumber:
        payload["maskedNumber"] = maskedNumber
    if telco:
        payload["telco"] = telco

    # call bulk sms request and return json status response
    response = requests.post(url, json=payload, headers=header)
    return response.json()

# Fetch SMS
# https://developers.africastalking.com/docs/sms/fetch_messages
def fetch_sms(api_key, username, lastReceivedId=None):

    # prep request (url, header, param)
    url = "https://api.sandbox.africastalking.com/version1/messaging"

    header = {
        "Accept": "application/json",
        "apiKey": api_key
    }

    param = {"username": username}

    # optional param
    if lastReceivedId is not None:
        param["lastReceivedId"] = lastReceivedId
    else:
        param["lastReceivedId"] = 0

    # call fetch sms request and return json message response
    response = requests.get(url, headers=header, params=param)
    return response.json()


