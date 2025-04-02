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

    # call request and return json response
    response = requests.post(url, json=payload, headers=header)
    return response.json()

def fetch_sms(api_key, username, lastReceivedId=None):
    return ""

