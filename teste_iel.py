import requests

url = "https://carreiras.iel.org.br/PA"

resposta = requests.get(
    url,
    timeout=20,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:", resposta.status_code)
print()
print(resposta.text[:5000])
