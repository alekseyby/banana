from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")
    # Write message in flask
    return str(resp)

@app.route("/test")
def test_flask():
    return 'Hello World!'


# CD to env folder and run .\Scripts\activate.bat
# -> run.py -> open http://localhost:5000/sms

if __name__ == "__main__":
    app.run(debug=True)
