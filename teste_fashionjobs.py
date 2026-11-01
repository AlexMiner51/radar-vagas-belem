import requests
import re

url = (
    "https://br.fashionjobs.com/"
    "city/bel%C3%A9m.html"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9"
}

html = requests.get(
    url,
    headers=headers,
    timeout=30
).text

links = re.findall(
    r'https://br\.fashionjobs\.com/trabalho/[^"]+',
    html
)

print(
    "TOTAL VAGAS:",
    len(set(links))
)

for vaga in sorted(set(links)):

    print(vaga)
