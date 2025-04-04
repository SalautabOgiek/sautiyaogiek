import os
from dotenv import load_dotenv

from api_func import send_message, fetch_messages

# preset
username = "sandbox"
sender = "25037"

load_dotenv()
api_key = os.getenv('SAND_API')

send_test = send_message(username, api_key, ["+254722123123"], "Sandbox!!!", sender)

print("SEND TEST:")
print(send_test)

fetch_test = fetch_messages(username, api_key)

print("\nFETCH TEST")
print(fetch_test)