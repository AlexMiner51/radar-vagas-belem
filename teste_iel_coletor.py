import requests
import re
import json

URL = "https://carreiras.iel.org.br/PA"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

links = sorted(set(re.findall(
    r'https://carreiras\.iel\.org\.br/PA/vaga/[^\s"<]+',
    html
)))

print("TOTAL DE VAGAS:", len(links))
print()

for link in links[:10]:

    try:

        pagina = requests.get(
            link,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        ).text

        titulo = re.search(
            r'"title":"([^"]+)"',
            pagina
        )

        cidade = re.search(
            r'"addressLocality":"([^"]+)"',
            pagina
        )

        print("=" * 60)

        print(
            titulo.group(1)
            if titulo else
            "SEM TITULO"
        )

        print(
            cidade.group(1)
            if cidade else
            "SEM CIDADE"
        )

        print(link)

    except Exception as erro:

        print("ERRO:", erro)
