# Introduction

This is a project funded by Mozilla Technology Fund under Lusike Mukhongo, Chad Edwards, Autumn Edwards and Cynthia Klekar-Cunningham and assisted by Cody Thornell and Khang Nguyen with the goal of creating a proof of concept for an AI-enhanced SMS system for the Ogiek community in Mau forest to send SMS messages to a number and get a chatbot response about their history, forest conservation, legal rulings and more. The project selected feature phones for developing an AI-enhanced messaging system as they can be used without access to the Internet, their phone battery lasts longer, and the phones are affordable, thereby making them more accessible to communities.

## Get Started

### General
- Clone the repository
- In terminal run:
```bash
pip install -r requirements.txt
```

### Test SMS
1. Follow the steps under General
2. Generate Sanbox api key and place into a .env file
```
SAND_API=xxxxxxxxxxxxxxx
```
3. Generate short code and place into `app.py` variables (SENDER_ID)
4. Launch simulator: https://developers.africastalking.com/simulator
5. Run `app.py` and message short code

### Test RAG
- Follow steps under General
- Install local mode, example using mannix/llamax3-8b-alpaca:latest model:
```
ollama pull mannix/llamax3-8b-alpaca:latest
```
- In terminal run (Re-run this every time you added new docx. files to "data" folder too):
```
python update_database.py
```
- In terminal run and insert your chat to the model here
```
python query_data [insert_chat_here]
```
