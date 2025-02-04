import requests
import json

# Rota sorgulama için gerekli parametreler
params = {
    'token_in_address': 'So11111111111111111111111111111111111111112',
    'token_out_address': '7EYnhQoR9YM3N7UoaKRoA44Uy8JeaZV3qyouov87awMs',
    'in_amount': '100000000',  # 0.1 SOL
    'from_address': '2kpJ5QRh16aRQ4oLZ5LnucHFDAZtEFz6omqWWMzDSNrx',
    'slippage': 10
}

# Rota sorgulama isteği
response = requests.get('https://gmgn.ai/defi/router/v1/sol/tx/get_swap_route', params=params)
data = response.json()

# İşlem verisini al
raw_tx = data['data']['raw_tx']['swapTransaction']

# raw_tx'i çöz, deserialize et, yerel cüzdanla imzala ve tekrar base64 olarak kodla
# Bu adımlar cüzdan entegrasyonunuza bağlıdır ve burada detaylandırılmamıştır




# API Endpoint (İmzalanmış işlemi gönderme)
submit_url = "https://gmgn.ai/defi/router/v1/sol/tx/submit_signed_transaction"


# JSON verisini hazırla
payload = json.dumps({"signed_tx": raw_tx})

# HTTP Başlıkları
headers = {
    "Content-Type": "application/json"
}

# API'ye POST isteği gönder
response = requests.post(submit_url, data=payload, headers=headers)

# Yanıtı yazdır
print("Status Code:", response.status_code)
print("Response:", response.text)
# İmzalanmış işlemi gönder
print(response.json()['data'])
print(type(response))

# İşlem durumunu kontrol et
tx_signature = response.json()['data']["hash"]
status_response = requests.get('https://gmgn.ai/defi/router/v1/sol/tx/status', params={'hash': tx_signature})
status_data = status_response.json()

print(status_data)

