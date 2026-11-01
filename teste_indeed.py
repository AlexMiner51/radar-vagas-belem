import requests
import re

url = (
    "https://br.indeed.com/jobs"
    "?q=estagio"
    "&l=Bel%C3%A9m%2C+PA"
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

padroes = [
    "__NEXT_DATA__",
    "_initialData",
    "jobKey",
    "jobkey",
    "results",
    "application/ld+json",
    "indeed_apply",
    "mosaic-provider-jobcards"
]

for p in padroes:
    print(f"{p}: {p.lower() in html.lower()}")
