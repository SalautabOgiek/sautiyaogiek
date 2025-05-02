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
    presets = {
        '1': """The Ogiek are working to secure their ancestral Mau Forest lands through legal action and advocacy. Recent court rulings support their rights, but continued efforts are essential for lasting protection. Key areas of focus include:
● Legal Cases: Pursuing court cases to defend land rights and prevent forced evictions.
● Community Advocacy: Mobilizing support to strengthen Ogiek claims to their land.
● Updates and Involvement: Stay informed about the latest developments and find ways to support Ogiek land rights efforts.
For more details, consult local leaders or community representatives actively involved in these initiatives""",
        '2': """The Ogiek are dedicated to preserving their unique cultural practices, including traditional hunting, gathering, and beekeeping. Efforts to protect Ogiek heritage include:
● Workshops and Training: Programs to teach traditional skills like forest-based beekeeping and medicinal plant use.
● Youth Programs: Initiatives to pass down Ogiek language, stories, and practices to younger generations.
● Community Events: Annual gatherings and cultural festivals to celebrate and share Ogiek customs.
For more information on joining these programs or attending events, reach out to local cultural leaders or community representatives""",
        '3': """The Ogiek actively protect the Mau Forest through sustainable practices that balance conservation with community needs. Current efforts include:
● Sustainable Practices: Using traditional knowledge to harvest forest resources without harming the ecosystem.
● Reforestation: Planting indigenous trees to restore forest cover and biodiversity.
● Advocacy: Promoting policies that recognize the Ogiek’s role in protecting the environment.
The Ogiek’s traditional connection to the forest positions them as guardians of this critical ecosystem. For more ways to get involved, speak with local conservation advocates.""",
        '4': """The Ogiek have legal resources to defend their rights and secure justice in land disputes. Key support includes:
● Court Representation: Help with cases addressing land rights and forced evictions.
● Legal Advice: Guidance on understanding and asserting legal rights.
● Advocacy Support: Assistance in voicing Ogiek concerns at national and international levels.
Engage with trusted organizations and community leaders to access these resources and protect Ogiek rights.""",
        '5': """The Ogiek are involved in sustainable income-generating activities, such as:
● Beekeeping: Combining traditional and modern practices to boost honey production and sales.
● Eco-tourism: Sharing Ogiek culture and natural heritage with visitors to generate income.
● Sustainable Forest Use: Harvesting forest resources like herbs and crafts responsibly for trade.
These programs help improve livelihoods while preserving the Mau Forest. Learn how to join or support these initiatives through community networks""",
        '6': """Support for the Ogiek community includes:
● Healthcare Access: Clinics and mobile health units addressing physical health needs.
● Mental Health Services: Counseling for trauma and stress caused by evictions and displacement.
● Nutrition Assistance: Food programs to combat malnutrition and promote healthy diets.
● Community Support: Groups and programs focused on social and emotional well-being.
These services aim to improve overall health and resilience within the community. Seek guidance from local leaders to access these resources.""",
        '7': """The Ogiek play a key role in managing the Mau Forest through collaboration with conservation authorities. Efforts include:
● Community Decision-Making: Involvement in policies affecting forest use and protection.
● Sustainable Practices: Balancing forest preservation with community needs.
● Training Programs: Opportunities to learn about forest conservation and management techniques.
These efforts ensure the Ogiek’s voice is heard and their role as guardians of the forest is upheld. Engage with local forest committees to participate.""",
        '8': """1. Ogiek Peoples’ Development Program (OPDP): +254 742 602 044
2. Koibatek Ogiek Women and Youth Network (KOWYN): +254 726 335 732
3. Kenya National Commission on Human Rights (KNCHR): +254 51 2213803
4. Ogiek Welfare Council: +254 726 335 732

These numbers connect you to organizations that support the Ogiek community in areas like land rights, legal aid, cultural preservation, and social welfare."""
    }
    return presets.get(option, "Invalid option selected.")


# def get_input():
#     user_input = input("Enter your question: ")
#     return user_input

def display_menu():
    return "Select number: 1. Land Rights, 2. Cultural Preservation, 3. Environmental Conservation, 4. Legal Support, 5. Income Programs, 6. Health and Social Support, 7. Participatory Forest Management, 8. Important Contacts, 9. Custom Request"

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
