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

links = re.findall(
    r'https://carreiras\.iel\.org\.br/PA/vaga/[^\s"<]+',
    resposta.text
)

for link in sorted(set(links)):
    print(link)
