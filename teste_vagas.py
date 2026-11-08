import requests
import re

url = "https://www.vagas.com.br"

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

links = re.findall(
    r'href="([^"]+)"',
    html
)

print("TOTAL LINKS:", len(links))
print()

for link in links[:150]:

    print(link)
