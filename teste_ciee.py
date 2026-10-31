import requests
import re

url = "https://portal.ciee.org.br/"

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = resposta.text

print("STATUS:", resposta.status_code)
print("TAMANHO:", len(html))

links = re.findall(
    r'href="([^"]+)"',
    html
)

print("QUANTIDADE DE LINKS:", len(links))

for link in links[:50]:
    print(link)
