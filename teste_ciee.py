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

for vaga in dados:

    cidade = str(
        vaga.get("cidade", "")
    )

    uf = str(
        vaga.get("uf", "")
    )

    if (
        "bel" in cidade.lower()
        or "anan" in cidade.lower()
        or uf == "PA"
    ):

        contador += 1

        print()

        print(
            "EMPRESA:",
            vaga.get("nomeEmpresa")
        )

        print(
            "CIDADE:",
            cidade
        )

        print(
            "UF:",
            uf
        )

        print(
            "TIPO:",
            vaga.get("tipoVaga")
        )

print()

print(
    "TOTAL ENCONTRADAS:",
    contador
)
