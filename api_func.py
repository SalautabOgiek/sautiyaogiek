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

# flask fetch example
# @app.route('/incoming-messages', methods=['POST'])
# def incoming_messages():
#    data = request.get_json(force=True)
#    print(f'Incoming message...\n ${data}')
#    return Response(status=200)
def fetch_messages(username, api_key, last_id=0):

    africastalking.initialize(
        username = username,
        api_key = api_key
    )

    sms = africastalking.SMS

    try:
        response = sms.fetch_messages(last_id)
        return response
    except Exception as e:
        print(f'ERROR: {e}')
        return ""