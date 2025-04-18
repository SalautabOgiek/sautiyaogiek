import os
from dotenv import load_dotenv

from sms_api import send_messages, fetch_messages

# sandbox connection
username = "sandbox"
sender = "25037"

load_dotenv()
api_key = os.getenv('SAND_API')

# menu logic
def get_preset(option):
    preset = {
        '1': "You selected Option A",
        '2': "You selected Option B",
        '3': "You selected Option C"
    }
    return preset.get(option, "Invalid option selected.")

def get_input():
    user_input = input("Enter your question: ")
    return user_input

def display_menu():
    # print("1. Option A")
    # print("2. Option B")
    # print("3. Option C")
    # print("4. User Input")
    return "SMS:\n1. Option A\n3. Option C\n4. User Input\n"

# menu test
# display_menu()
# selection = input("Please select an option (1-4): ")

# if selection in ['1', '2', '3']:
#     response = get_preset(selection)
#     print(response)
# elif selection == '4':
#     response = get_input()
#     print(response)
# else:
#     print("invalid option")

