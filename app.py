# polling process, would be more efficient to switch to webhook system for production, but sandbox doesn't support webhooks (looking into for future)
import os
import threading
import time
from flask import Flask
from dotenv import load_dotenv

from sms_api import send_messages, fetch_messages
from menu import get_preset, display_menu

# load presets
load_dotenv()
USERNAME  = "sandbox"
API_KEY   = os.getenv("SAND_API")
SENDER_ID = "25037"

# flask backend setup
app = Flask(__name__)
sessions = {} # temp store convos in here for now (need long term storage?)
last_id = 0

# logic for processing messages
def handle_inbound(from_number, text):
    stage = sessions.get(from_number, "NEW")

    if stage == "NEW":
        reply = display_menu()
        sessions[from_number] = "AWAITING_CHOICE"

    elif stage == "AWAITING_CHOICE":
        if text in ("1","2","3"):
            reply = get_preset(text)
            sessions.pop(from_number, None)
        elif text == "4":
            reply = "Test input:"
            sessions[from_number] = "AWAITING_INPUT"
        else:
            reply = "Invalid option.\n" + display_menu()

    elif stage == "AWAITING_INPUT":
        reply = f"You said: {text}"
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
        time.sleep(5)  # set to 5 secondsß

if __name__ == "__main__":
    # kick off polling process
    t = threading.Thread(target=poll_inbound, daemon=True)
    t.start()

    # launch flask app
    app.run(host="0.0.0.0", port=1738)
