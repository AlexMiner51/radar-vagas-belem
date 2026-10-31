import requests
import re

url = "https://carreiras.iel.org.br/PA"

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", resposta.status_code)
print()

apis = re.findall(r'https://[^"\']+', resposta.text)

for api in apis:
    print(api)
