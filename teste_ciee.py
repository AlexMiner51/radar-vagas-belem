import requests

url = (
    "https://api.ciee.org.br/vagas/"
    "vitrine-vaga/publicadas?page=1"
)

dados = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
).json()

contador = 0

for vaga in dados["content"]:

    cidade = vaga["local"]["cidade"]
    uf = vaga["local"]["uf"]

    if uf == "PA":

        contador += 1

        print()
        print("EMPRESA:", vaga["nomeEmpresa"])
        print("CIDADE:", cidade)
        print("UF:", uf)
        print("AREA:", vaga["areaProfissional"])
        print("CODIGO:", vaga["codigoVaga"])

print()

print(
    "TOTAL PARA:",
    contador
)
