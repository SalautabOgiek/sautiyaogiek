import os
from dotenv import load_dotenv

from sms_api import send_messages, fetch_messages

# variables
username = "sandbox"
sender = "25037"

load_dotenv()
api_key = os.getenv('SAND_API')

# test sending feature
send_test = send_messages(username, api_key, ["+254722123123"], "Sandbox!!!", sender)

print("SEND TEST:")
print(send_test)

# test fetch feature
fetch_test = fetch_messages(username, api_key)

print("\nFETCH TEST")
print(fetch_test)