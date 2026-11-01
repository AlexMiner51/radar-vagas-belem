import requests
import re


def buscar_vagas_fashionjobs():

    vagas = []

    url = (
        "https://br.fashionjobs.com/"
        "city/bel%C3%A9m.html"
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

    try:

        html = requests.get(
            url,
            headers=headers,
            timeout=30
        ).text

        vagas_encontradas = re.findall(
            r'<a class="extended-link".*?href="(https://br\.fashionjobs\.com/trabalho/[^"]+)".*?title="([^"]+)"',
            html,
            re.DOTALL
        )

               vistos = set()

        for link, titulo in vagas_encontradas:

            if link in vistos:
                continue

            vistos.add(link)

            titulo_normalizado = titulo.lower()

            if any(
                palavra in titulo_normalizado
                for palavra in PALAVRAS_BLOQUEADAS_FASHION
            ):
                continue

            vagas.append(
                {
                    "titulo":
                        f"[FashionJobs] {titulo}",
                    "link":
                        link
                }
            )
    except Exception as erro:

        print(
            "Erro FashionJobs:",
            erro
        )

    print(
        "Vagas FashionJobs:",
        len(vagas)
    )

    return vagas
