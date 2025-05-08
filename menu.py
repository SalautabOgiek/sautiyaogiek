
# preloaded
english_presets = {
            '1': "The Ogiek are working to secure their ancestral Mau Forest lands through legal action and advocacy. Recent court rulings support their rights, but continued efforts are essential for lasting protection. Key areas of focus include:\n● Legal Cases: Pursuing court cases to defend land rights and prevent forced evictions.\n● Community Advocacy: Mobilizing support to strengthen Ogiek claims to their land.\n● Updates and Involvement: Stay informed about the latest developments and find ways to support Ogiek land rights efforts.\nFor more details, consult local leaders or community representatives actively involved in these initiatives",
            '2': "The Ogiek are dedicated to preserving their unique cultural practices, including traditional hunting, gathering, and beekeeping. Efforts to protect Ogiek heritage include:\n● Workshops and Training: Programs to teach traditional skills like forest-based beekeeping and medicinal plant use.\n● Youth Programs: Initiatives to pass down Ogiek language, stories, and practices to younger generations.\n● Community Events: Annual gatherings and cultural festivals to celebrate and share Ogiek customs.\nFor more information on joining these programs or attending events, reach out to local cultural leaders or community representatives",
            '3': "The Ogiek actively protect the Mau Forest through sustainable practices that balance conservation with community needs. Current efforts include:\n● Sustainable Practices: Using traditional knowledge to harvest forest resources without harming the ecosystem.\n● Reforestation: Planting indigenous trees to restore forest cover and biodiversity.\n● Advocacy: Promoting policies that recognize the Ogiek’s role in protecting the environment.\nThe Ogiek’s traditional connection to the forest positions them as guardians of this critical ecosystem. For more ways to get involved, speak with local conservation advocates.",
            '4': "The Ogiek have legal resources to defend their rights and secure justice in land disputes. Key support includes:\n● Court Representation: Help with cases addressing land rights and forced evictions.\n● Legal Advice: Guidance on understanding and asserting legal rights.\n● Advocacy Support: Assistance in voicing Ogiek concerns at national and international levels.\nEngage with trusted organizations and community leaders to access these resources and protect Ogiek rights.",
            '5': "The Ogiek are involved in sustainable income-generating activities, such as:\n● Beekeeping: Combining traditional and modern practices to boost honey production and sales.\n● Eco-tourism: Sharing Ogiek culture and natural heritage with visitors to generate income.\n● Sustainable Forest Use: Harvesting forest resources like herbs and crafts responsibly for trade.\nThese programs help improve livelihoods while preserving the Mau Forest. Learn how to join or support these initiatives through community networks",
            '6': "Support for the Ogiek community includes:\n● Healthcare Access: Clinics and mobile health units addressing physical health needs.\n● Mental Health Services: Counseling for trauma and stress caused by evictions and displacement.\n● Nutrition Assistance: Food programs to combat malnutrition and promote healthy diets.\n● Community Support: Groups and programs focused on social and emotional well-being.\nThese services aim to improve overall health and resilience within the community. Seek guidance from local leaders to access these resources.",
            '7': "The Ogiek play a key role in managing the Mau Forest through collaboration with conservation authorities. Efforts include:\n● Community Decision-Making: Involvement in policies affecting forest use and protection.\n● Sustainable Practices: Balancing forest preservation with community needs.\n● Training Programs: Opportunities to learn about forest conservation and management techniques.\nThese efforts ensure the Ogiek’s voice is heard and their role as guardians of the forest is upheld. Engage with local forest committees to participate.",
            '8': "1. Ogiek Peoples’ Development Program (OPDP): +254 742 602 044\n2. Koibatek Ogiek Women and Youth Network (KOWYN): +254 726 335 732\n3. Kenya National Commission on Human Rights (KNCHR): +254 51 2213803\n4. Ogiek Welfare Council: +254 726 335 732\nThese numbers connect you to organizations that support the Ogiek community in areas like land rights, legal aid, cultural preservation, and social welfare."
        }

swahili_presets = {}

# handle preset responses
def get_preset(option, lang):
    if lang == 1: # swahili
        return swahili_presets.get(option, "Invalid option selected.")
    else: # default engilsh
        return english_presets.get(option, "Invalid option selected.")

# TODO handle error messages
# error 0: invalid menu option
def display_error(error, lang):
    if lang == 1: # swahili
        if error == 0:
            return "" #TODO
        else:
            return ""
    else: # default engilsh
        if error == 0: 
            return "Invalid option.\n"
        else:
            return ""

# TODO fix newline char issue, currently talking with AT support regarding this (maybe simulator doesnt support?), 5/8 update: still no help from support so far
# handle displaying menu
def display_menu(lang):
    if lang == 1: # swahili
        return ""
    else: # default engilsh
        return "Select number:\n1. Land Rights,\n2. Cultural Preservation,\n3. Environmental Conservation,\n4. Legal Support,\n5. Income Programs,\n6. Health and Social Support,\n7. Participatory Forest Management,\n8. Important Contacts,\n9. Custom Request"
