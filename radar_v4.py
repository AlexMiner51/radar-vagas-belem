import os
import json
import requests
import feedparser
import re
from datetime import datetime

CIDADES_ACEITAS = [
    "belém",
    "belem",
    "ananindeua"
]

AREAS_INTERESSE = [
    "ti",
    "t.i",
    "tecnologia",
    "informatica",
    "informática",
    "computacao",
    "computação",
    "ciencia da computacao",
    "ciência da computação",
    "ads",
    "análise e desenvolvimento de sistemas",
    "analise e desenvolvimento de sistemas",
    "sistemas",
    "sistema",
    "software",
    "desenvolvimento",
    "programacao",
    "programação",
    "engenharia de software",
    "moda",
    "design",
    "design de moda",
    "marketing",
    "publicidade",
    "ux",
    "ui"
]


def carregar_historico():

    try:

        with open(
            "seen.json",
            "r",
            encoding="utf-8"
        ) as arquivo:

            return set(json.load(arquivo))

    except:

        return set()


def salvar_historico(historico):

    with open(
        "seen.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            list(historico),
            arquivo,
            ensure_ascii=False,
            indent=2
        )


def titulo_relevante(titulo):

    texto = titulo.lower()

    return any(
        palavra in texto
        for palavra in AREAS_INTERESSE
    )


def buscar_vagas_iel():

    vagas = []

    try:

        resposta = requests.get(
            "https://carreiras.iel.org.br/PA",
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )

        html = resposta.text

        links = sorted(
            set(
                re.findall(
                    r'https://carreiras\.iel\.org\.br/PA/vaga/[^\s"<]+',
                    html
                )
            )
        )

        print("Links encontrados:", len(links))

        for link in links:

            try:

                pagina = requests.get(
                    link,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    },
                    timeout=30
                ).text

                titulo_match = re.search(
                    r'"title":"([^"]+)"',
                    pagina
                )

                cidade_match = re.search(
                    r'"addressLocality":"([^"]+)"',
                    pagina
                )

                titulo = (
                 
