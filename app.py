from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# معلومات حساب Twilio (ضع بياناتك هنا)
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# رقم المرسل وأرقام المستلمين
twilio_phone_number = '+201278567468'  # رقم Twilio
to_phone_number = '+18788677033'    # رقمك المستلم

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    message_body = f"تم استلام الموقع:\nخط العرض: {latitude}\nخط الطول: {longitude}"
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=to_phone_number
    )
    
    print(f"SMS sent: {message.sid}")
    return "تم ارسال الرسالة بنجاح"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
