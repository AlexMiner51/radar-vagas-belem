import os
import requests
import feedparser
from datetime import datetime

BUSCAS = [
    "estágio tecnologia Belém PA",
    "estágio TI Belém PA",
    "estágio ciência da computação Belém PA",
    "estágio sistemas de informação Belém PA",
    "estágio desenvolvimento software Belém PA",
    "estágio moda Belém PA",
    "estágio design de moda Belém PA"
    "site:gupy.io estágio tecnologia Belém",
    "site:gupy.io estágio TI Belém",
    "site:gupy.io estágio ciência da computação Belém",

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


def buscar_vagas():
    vagas = []

    for busca in BUSCAS:

        url = (
            "https://news.google.com/rss/search?q="
            + busca.replace(" ", "+")
        )

        feed = feedparser.parse(url)

        for item in feed.entries[:10]:

            titulo = item.title
            link = item.link

            vagas.append(
                f"• {titulo}\n{link}"
            )

    return vagas


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

    texto = (
        f"📢 Radar de Estágios - Belém/PA\n"
        f"{datetime.now().strftime('%d/%m/%Y')}\n\n"
    )

    if vagas:
        texto += "\n\n".join(vagas[:20])
    else:
        texto += "Nenhuma vaga encontrada."

    enviar_telegram(texto)


if __name__ == "__main__":
    main()
