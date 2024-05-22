import requests

bot_token = "6401646362:AAGC1GCu778u9YSj1Q1IiV117GmfrBePFm4"
chat_id = "2075341659"
message = "Olá, esta é uma mensagem enviada pelo bot do Telegram!"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Falha ao enviar mensagem: {response.status_code}")

# import requests

# bot_token = "6401646362:AAGC1GCu778u9YSj1Q1IiV117GmfrBePFm4"

# # Obtenha as atualizações recentes
# url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
# response = requests.get(url)
# updates = response.json()

# print(updates)