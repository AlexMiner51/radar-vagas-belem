import requests
import re

url = (
    "https://br.fashionjobs.com/"
    "city/bel%25c3%25a9m.html"
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
    r'href="([^"]+)"',
    html
)

print("TOTAL LINKS:", len(links))

for link in links:

    link_lower = link.lower()

    if (
        "job" in link_lower
        or "emploi" in link_lower
        or "emprego" in link_lower
        or "vaga" in link_lower
        or "offre" in link_lower
    ):

        print(link)
