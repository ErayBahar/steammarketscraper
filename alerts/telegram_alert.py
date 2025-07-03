import requests

def send_telegram_alert(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id":chat_id,
        "text":message
    }
    response = requests.post(url,data=data)
    if response.status_code !=200:
        print("❌ Telegram alert failed.")
