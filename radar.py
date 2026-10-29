import os
import json
import requests
import feedparser
from datetime import datetime

BUSCAS = [
    "site:gupy.io estágio tecnologia Belém Pará",
    "site:gupy.io estágio TI Belém Pará",
    "site:gupy.io estágio ciência da computação Belém Pará",
    "site:gupy.io estágio sistemas de informação Belém Pará",
    "site:gupy.io estágio desenvolvimento software Belém Pará",

    "site:linkedin.com/jobs estágio tecnologia Belém Pará",
    "site:linkedin.com/jobs estágio TI Belém Pará",
    "site:linkedin.com/jobs estágio computação Belém Pará",

    "site:indeed.com estágio tecnologia Belém Pará",
    "site:indeed.com estágio TI Belém Pará",

    "site:ciee.org.br estágio Belém Pará",
    "site:iel-pa.org.br estágio Belém Pará",

    "site:gupy.io estágio moda Belém Pará",
    "site:gupy.io estágio design de moda Belém Pará",

    "site:linkedin.com/jobs estágio moda Belém Pará",
    "site:linkedin.com/jobs estágio design de moda Belém Pará"
]

PALAVRAS_OBRIGATORIAS = [
    "belém",
    "pará"
]

PALAVRAS_ESTAGIO = [
    "estágio",
    "estagio",
    "estagiário",
    "estagiario",
    "intern"
]

PALAVRAS_BLOQUEADAS = [
    "guiné",
    "guinea",
    "guiné-bissau",
    "bissau",
    "africa",
    "south africa",
    "home office",
    "remoto",
    "remote",
    "são paulo",
    "sao paulo",
    "rio de janeiro",
    "curitiba",
    "porto alegre",
    "bangkok",
    "thailand"
]


def carregar_historico():

    try:
        with open("seen.json", "r", encoding="utf-8") as f:
            return set(json.load(f))
    except:
        return set()


def salvar_historico(historico):

    with open("seen.json", "w", encoding="utf-8") as f:
        json.dump(
            list(historico),
            f,
            ensure_ascii=False,
            indent=2
        )


def vaga_valida(texto):

    texto = texto.lower()

    if not all(p in texto for p in PALAVRAS_OBRIGATORIAS):
        return False

    if not any(p in texto for p in PALAVRAS_ESTAGIO):
        return False

    if any(p in texto for p in PALAVRAS_BLOQUEADAS):
        return False

    return True


def buscar_vagas():

    vagas = []

    historico = carregar_historico()

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

                texto = f"{titulo} {link}"

                if not vaga_valida(texto):
                    continue

                if link in historico:
                    continue

                historico.add(link)

                vagas.append(
                    {
                        "titulo": titulo,
                        "link": link
                    }
                )

        except Exception as erro:

            print("Erro:", erro)

    salvar_historico(historico)

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

    cabecalho = (
        f"📢 Radar de Estágios - Belém/PA\n"
        f"{datetime.now().strftime('%d/%m/%Y')}\n\n"
    )

    if not vagas:

        mensagem = (
            cabecalho
            + "Nenhuma nova vaga encontrada hoje."
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
