import requests

for pagina in range(1, 51):

    url = (
        "https://api.ciee.org.br/vagas/"
        f"vitrine-vaga/publicadas?page={pagina}"
    )

    dados = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    ).json()

    for vaga in dados["content"]:

        local = vaga.get("local")

        if not local:
            continue

        cidade = str(
            local.get("cidade", "")
        ).lower()

        if (
            "belém" in cidade
            or "belem" in cidade
            or "ananindeua" in cidade
        ):

            print()
            print("PÁGINA:", pagina)
            print("CIDADE:", cidade)
            print(
                "ÁREA:",
                vaga.get(
                    "areaProfissional"
                )
            )
            print(
                "EMPRESA:",
                vaga.get(
                    "nomeEmpresa"
                )
            )
