import os
import json
import requests
import feedparser
import re
from datetime import datetime

BUSCAS = [
    "estágio tecnologia Belém Pará",
    "estágio TI Belém Pará",
    "estágio computação Belém Pará",
    "estágio ciência da computação Belém Pará",
    "estágio sistemas de informação Belém Pará",
    "estágio desenvolvimento software Belém Pará",
    "estágio ADS Belém Pará",
    "estágio informática Belém Pará",
    "estágio moda Belém Pará",
    "estágio design de moda Belém Pará",
    "estágio marketing Belém Pará",
    "estágio publicidade Belém Pará"
]

PALAVRAS_INTERESSE = [
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
    "analise e desenvolvimento de sistemas",
    "análise e desenvolvimento de sistemas",
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

CIDADES_ACEITAS = [
    "belém",
    "belem",
    "ananindeua"
]


def carregar_historico():

    try:

        with open(
            "seen.json",
   
