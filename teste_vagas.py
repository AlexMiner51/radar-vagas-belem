import requests
import re

url = "https://trabalheconosco.vagas.com.br/vagas"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    )
}

html = requests.get(
    url,
    headers=headers,
    timeout=30
).text

print("STATUS:", 200)
print()

padroes = re.findall(
    r'/vagas/[^\s"<>]+',
    html
)

print("TOTAL PADROES:", len(set(padroes)))
print()

for item in sorted(set(padroes))[:100]:

    print(item)
