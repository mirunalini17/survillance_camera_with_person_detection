from twilio.rest import Client

# =========================
# TWILIO CREDENTIALS
# =========================

account_sid = "SID"
auth_token = "TOKEN"

client = Client(account_sid, auth_token)

# =========================
# SEND SMS
# =========================

message = client.messages.create(

    body="Message sent",

    from_="+1xxxxxxxxx",   # Twilio number

    to="+91xxxxxxxxxx"     # Your phone number
)

print("SMS SENT")
print(message.sid)