import requests
import re

URL = "https://carreiras.iel.org.br/PA"

CIDADES_ACEITAS = [
    "belém",
    "belem",
    "ananindeua"
]


def cidade_valida(cidade):

    if not cidade:
        return False

    return cidade.lower() in CIDADES_ACEITAS


html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

links = sorted(set(re.findall(
    r'https://carreiras\.iel\.org\.br/PA/vaga/[^\s"<]+',
    html
)))

vagas = []

for link in links:

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

        titulo = (
            titulo.group(1)
            if titulo else
            ""
        )

        cidade = (
            cidade.group(1)
            if cidade else
            ""
        )

        if not cidade_valida(cidade):
            continue

        vagas.append(
            {
                "titulo": titulo,
                "cidade": cidade,
                "link": link
            }
        )

    except Exception as erro:

        print("ERRO:", erro)

print()

print("TOTAL FILTRADAS:", len(vagas))

print()

for vaga in vagas:

    print("=" * 60)
    print(vaga["titulo"])
    print(vaga["cidade"])
    print(vaga["link"])
