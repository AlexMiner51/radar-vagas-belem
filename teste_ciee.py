import requests
import re

url = "https://portal.ciee.org.br/quero-uma-vaga/"

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = resposta.text

links = re.findall(
    r'href="([^"]+)"',
    html
)

print("TOTAL LINKS:", len(links))

for link in links:

    link = link.lower()

    if (
        "vaga" in link
        or "estagio" in link
        or "estágio" in link
        or "aprendiz" in link
    ):
        print(link)
