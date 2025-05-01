# import os
# from dotenv import load_dotenv

# from sms_api import send_messages, fetch_messages

# sandbox connection
# username = "sandbox"
# sender = "25037"

# load_dotenv()
# api_key = os.getenv('SAND_API')

# preset responses
def get_preset(option):
    preset = {
        '1': "You selected Option 1",
        '2': "You selected Option 2",
        '3': "You selected Option 3",
        '4': "You selected Option 4",
        '5': "You selected Option 5",
        '6': "You selected Option 6",
        '7': "You selected Option 7",
        '8': "You selected Option 8",
    }
    return preset.get(option, "Invalid option selected.")

# def get_input():
#     user_input = input("Enter your question: ")
#     return user_input

def display_menu():
    return "Select number:\n\n1. Land Rights\n2. Cultural Preservation\n3. Environmental Conservation\n4. Legal Support\n5. Income Programs\n6. Health and Social Support\n7. Participatory Forest Management\n8. Important Contacts\n9. Custom Request"

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
