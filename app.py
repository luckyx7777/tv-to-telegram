from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "ТВОЙ_ТОКЕН"
TELEGRAM_CHAT_ID = "ТВОЙ_CHAT_ID"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", str(data))
    
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(telegram_url, data=payload)
    
    return "ok", 200

if __name__ == '__main__':
    app.run()
