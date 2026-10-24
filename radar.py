import os
import requests
import feedparser
from datetime import datetime

BUSCAS = [
    "site:gupy.io estágio tecnologia Belém",
    "site:gupy.io estágio TI Belém",
    "site:gupy.io estágio ciência da computação Belém",
    "site:gupy.io estágio sistemas de informação Belém",
    "site:gupy.io estágio desenvolvimento software Belém",

    "site:linkedin.com/jobs estágio tecnologia Belém",
    "site:linkedin.com/jobs estágio TI Belém",
    "site:linkedin.com/jobs estágio computação Belém",

    "site:indeed.com estágio tecnologia Belém",
    "site:indeed.com estágio TI Belém",

    "site:ciee.org.br estágio Belém tecnologia",
    "site:iel-pa.org.br estágio Belém",

    "site:gupy.io estágio moda Belém",
    "site:gupy.io estágio design de moda Belém",

    "site:linkedin.com/jobs estágio moda Belém",
    "site:linkedin.com/jobs estágio design de moda Belém"
]

PALAVRAS_BELEM = [
    "belém",
    "belem"
]

PALAVRAS_ESTAGIO = [
    "estágio",
    "estagio",
    "estagiário",
    "estagiario",
    "intern"
]

PALAVRAS_BLOQUEADAS = [
    "home office",
    "remoto",
    "remote",
    "são paulo",
    "sao paulo",
    "rio de janeiro",
    "curitiba",
    "porto alegre",
    "bangkok",
    "thailand",
    "africa",
    "south africa"
]


def vaga_valida(texto):

    texto = texto.lower()

    if not any(p in texto for p in PALAVRAS_BELEM):
        return False

    if not any(p in texto for p in PALAVRAS_ESTAGIO):
        return False

    if any(p in texto for p in PALAVRAS_BLOQUEADAS):
        return False

    return True


def buscar_vagas():

    vagas_encontradas = []
    links_vistos = set()

    for busca in BUSCAS:

        try:

            url = (
                "https://news.google.com/rss/search?q="
                + busca.replace(" ", "+")
            )

            feed = feedparser.parse(url)

            for item in feed.entries:

                titulo = item.title.strip()
                link = item.link.strip()

                texto = titulo + " " + link

                if not vaga_valida(texto):
                    continue

                if link in links_vistos:
                    continue

                links_vistos.add(link)

                vagas_encontradas.append(
                    {
                        "titulo": titulo,
                        "link": link
                    }
                )

        except Exception as erro:

            print("Erro na busca:", erro)

    return vagas_encontradas


def enviar_telegram(texto):

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": chat_id,
            "text": texto[:4000]
        },
        timeout=30
    )


def main():

    vagas = buscar_vagas()

    cabecalho = (
        f"📢 Radar de Estágios - Belém/PA\n"
        f"{datetime.now().strftime('%d/%m/%Y')}\n\n"
    )

    if not vagas:

        mensagem = (
            cabecalho
            + "Nenhuma vaga compatível encontrada hoje."
        )

    else:

        linhas = []

        for vaga in vagas[:15]:

            linhas.append(
                f"• {vaga['titulo']}\n{vaga['link']}"
            )

        mensagem = cabecalho + "\n\n".join(linhas)

    enviar_telegram(mensagem)


if __name__ == "__main__":
    main()
