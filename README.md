# Introduction

This is a project funded by Mozilla Technology Fund under Lusike Mukhongo, Chad Edwards, Autumn Edwards, Cynthia Klekar-Cunningham and Winston Mano, and assisted by Cody Thornell and Khang Nguyen with the goal of creating a proof of concept for an AI-enhanced SMS system for the Ogiek community in Mau forest to send SMS messages to a number and get a chatbot response about their history, forest conservation, legal rulings and more. The project selected feature phones for developing an AI-enhanced messaging system as they can be used without access to the Internet, their phone battery lasts longer, and the phones are affordable, thereby making them more accessible to communities.

## Get Started

### General
- Clone the repository
- In terminal run:
```bash
pip install -r requirements.txt
```

### Test SMS
1. Follow the steps under General
2. Generate Africa Talking api key, phone number shortcode, language id (0 for english, 1 for swahili) and place into a .env file
```
AT_API=xxxxxxxxxxxxxxxxxxxx
SEND_ID=xxxxx
LANG_ID=x
```
3. Launch simulator: https://developers.africastalking.com/simulator
4. Run `app.py` and message short code

### Test RAG
1. Install local mode, example using mannix/llamax3-8b-alpaca:latest model:
```
ollama pull mannix/llamax3-8b-alpaca:latest
```
2. Make a folder name 'data' within the root folder.
3. Place all documents you want the model tofetch information from into `/data` folder
4. In terminal run (Re-run this every time you add new files):
```
python update_database.py
```
4. In terminal run and insert your chat to the model here
```
python query_data [insert_chat_here]
```
5. Or through sms connection, choose number 9 on sms menu for generative response
