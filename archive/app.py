# better for prod, but not available for sandbox, need to use polling instead :(
import os
from flask import Flask, request, abort
from dotenv import load_dotenv

from sms_api import send_messages
from menu import get_preset

# loading credentials
load_dotenv()
USERNAME = "sandbox"
API_KEY = os.getenv("SAND_API")  
SENDER_ID = "25037"         

app = Flask(__name__)

# storing temp sessions here for now
sessions = {}

def get_menu_text():
    return (
        "SMS Test:\n"
        "1. Option A\n"
        "2. Option B\n"
        "3. Option C\n"
        "4. Enter custom input"
    )

# monitor inbound sms
@app.route("/sms/inbound", methods=["POST"])
def inbound_sms():
    data = request.values
    from_number = data.get("from")
    text = data.get("text", "").strip()

    if not from_number or not text:
        abort(400)

    stage = sessions.get(from_number, "NEW")

    if stage == "NEW":
        reply = get_menu_text()
        sessions[from_number] = "AWAITING_CHOICE"

    # menu response handling
    elif stage == "AWAITING_CHOICE":
        # presets
        if text in ("1", "2", "3"):
            reply = get_preset(text)
            sessions.pop(from_number, None)
        # custom
        elif text == "4":
            reply = "Type what you'd like and send it back:"
            sessions[from_number] = "AWAITING_INPUT"
        else:
            reply = "Invalid option.\n" + get_menu_text()

    elif stage == "AWAITING_INPUT":
        # echo free text
        reply = f"You said: {text}"
        sessions.pop(from_number, None)

    else:
        # fallback to menu
        reply = get_menu_text()
        sessions[from_number] = "AWAITING_CHOICE"

    # send reply
    send_messages(USERNAME, API_KEY, [from_number], reply, SENDER_ID)
    return "", 200

# launch on local server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1738)
