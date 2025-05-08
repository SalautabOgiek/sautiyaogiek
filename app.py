# polling process, would be more efficient to switch to webhook system for production, but sandbox doesn't support webhooks (looking into for future)
import os
import threading
import time
from flask import Flask
from dotenv import load_dotenv

from sms_api import send_messages, fetch_messages
from menu import get_preset, display_menu, display_error
from configfile import load_last_id, save_last_id
from query_data import query_rag

# load presets
load_dotenv()
USERNAME  = "sandbox"
API_KEY   = os.getenv("SAND_API")
SENDER_ID = "25037"
LANG_ID = 0 # 0 for english, 1 for swahili

# flask backend setup
app = Flask(__name__)
sessions = {} # temp store convos in here for now (need long term storage?)
last_id = load_last_id()

# logic for processing messages
def handle_inbound(from_number, text):
    stage = sessions.get(from_number, "NEW")

    if stage == "NEW":
        reply = display_menu(LANG_ID)
        sessions[from_number] = "AWAITING_CHOICE"

    elif stage == "AWAITING_CHOICE":
        if text in ("1","2","3","4","5","6","7","8"):
            reply = get_preset(text, LANG_ID)
            sessions.pop(from_number, None)
        elif text == "9":
            reply = "Enter your custom question:"
            sessions[from_number] = "AWAITING_INPUT"
        else:
            reply = display_error(0, LANG_ID) + display_menu(LANG_ID)

    elif stage == "AWAITING_INPUT":
        reply = query_rag(text)
        #reply = f"You said: {text}"
        sessions.pop(from_number, None)

    else:
        reply = display_menu()
        sessions[from_number] = "AWAITING_CHOICE"

    send_messages(USERNAME, API_KEY, [from_number], reply, SENDER_ID)

# threaded process for monitoring incoming messages
def poll_inbound():
    global last_id
    while True:
        data = fetch_messages(USERNAME, API_KEY, last_id)
        msgs = data.get("SMSMessageData", {}).get("Messages", [])
        for m in msgs:
            handle_inbound(m["from"], m["text"].strip())
            last_id = max(last_id, m["id"])
            save_last_id(last_id)
        time.sleep(5)  # currently 5 second wait

if __name__ == "__main__":
    # kick off polling process
    t = threading.Thread(target=poll_inbound, daemon=True)
    t.start()

    # launch flask app
    app.run(host="0.0.0.0", port=1738)
