import os
import requests

token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{token}/sendMessage"

resposta = requests.post(
    url,
    data={
        "chat_id": chat_id,
        "text": "✅ Integração GitHub + Telegram funcionando!"
    },
    timeout=30
)

print(resposta.text)
