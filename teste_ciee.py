import requests
import re

url = "https://portal.ciee.org.br/quero-uma-vaga/estagio/"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
).text

apis = re.findall(
    r'https://[^"\']+',
    html
)

print("TOTAL APIS:", len(apis))

for item in sorted(set(apis)):
    print(item)
