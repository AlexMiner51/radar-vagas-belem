import requests

url = "https://carreiras.iel.org.br/PA/vaga/vagas-destinadas-a-aprendizagem-de-cursos/32679/vaga-de-estagio-para-ti-benevides"

resposta = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", resposta.status_code)
print()
print(resposta.text[:20000])
