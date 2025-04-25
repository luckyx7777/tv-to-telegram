from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", str(data))

    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    
    response = requests.post(telegram_url, data=payload)
    print(f"Telegram response: {response.status_code} - {response.text}")
    
    return "ok", 200

# Опционально: чтобы GET-запрос на / не давал 404
@app.route("/", methods=["GET"])
def home():
    return "🤖 Бот активен и ждёт сигналы от TradingView", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
