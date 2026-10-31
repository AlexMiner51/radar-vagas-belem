import requests
import re

url = "https://carreiras.iel.org.br/PA/vaga/vagas-destinadas-a-aprendizagem-de-cursos/32679/vaga-de-estagio-para-ti-benevides"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

campos = [
    "addressLocality",
    "addressRegion",
    "datePosted",
    "title",
    "description",
]

for campo in campos:

    encontrados = re.findall(
        rf'"{campo}":"(.*?)"',
        html
    )

    print()
    print("CAMPO:", campo)

    for item in encontrados:
        print(item)
