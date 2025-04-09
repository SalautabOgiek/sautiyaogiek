import os
from dotenv import load_dotenv

from sms_api import send_messages, fetch_messages

# sandbox connection
username = "sandbox"
sender = "25037"

load_dotenv()
api_key = os.getenv('SAND_API')

# menu logic
