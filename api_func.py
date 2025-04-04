import africastalking

def send_message(username, api_key, recipients, message, sender):

    africastalking.initialize(
        username = username,
        api_key = api_key
    )

    sms = africastalking.SMS

    try:
        response = sms.send(message, recipients, sender)
        return response
    except Exception as e:
        print(f'ERROR: {e}')
        return ""
