# Introduction

This is a project under Dr.Chad Edwards assisted by Cody George Thornell and Khang Nguyen with the goal of creating a proof of concept for a solution that allow English and Swahili speakers to send SMS messages to a number and get a chatbot response in SMS about the Ogiek community, their history and more.

## Get Started

### General
- Clone the repository
- In terminal run:
```bash
pip install -r requirements.txt
```

### Test SMS
1. Follow the steps under General
2. Launch simulator: https://developers.africastalking.com/simulator
3. TBD

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
- In terminal run and Insert Your Chat to the Model Here
```
python query_data [insert_chat_here]
```
