import os
from dotenv import load_dotenv

from api_func import send_message

# preset
username = "sandbox"
sender = "25037"

load_dotenv()
api_key = os.getenv('SAND_API')

send_test = send_message(username, api_key, ["+254722123123"], "Sandbox!!!", sender)

print(send_test)