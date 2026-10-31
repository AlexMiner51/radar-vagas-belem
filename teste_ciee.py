import requests

for pagina in range(1, 21):

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

    print()
    print("=" * 50)
    print("PÁGINA", pagina)
    print("=" * 50)

    encontrou = False

    for vaga in dados["content"]:

        local = vaga.get("local")

        if not local:
            continue

        uf = local.get(
            "uf",
            ""
        )

        cidade = local.get(
            "cidade",
            ""
        )

        if uf == "PA":

            encontrou = True

            print(
                cidade,
                "-",
                vaga.get(
                    "areaProfissional"
                )
            )

    if encontrou:

        print(
            "\nACHOU VAGA(S) DO PARÁ!"
        )
