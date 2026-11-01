import os
import json
import requests
import feedparser
import re
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

    "site:sejatrainee.com.br estágio Belém Pará",
    "site:sejatrainee.com.br tecnologia Belém Pará",
    "site:sejatrainee.com.br TI Belém Pará",
    "site:sejatrainee.com.br computação Belém Pará",
    "site:sejatrainee.com.br moda Belém Pará",

    "site:estagiotrainee.com estágio Belém Pará",
    "site:estagiotrainee.com tecnologia Belém Pará",
    "site:estagiotrainee.com TI Belém Pará",
    "site:estagiotrainee.com computação Belém Pará",
    "site:estagiotrainee.com moda Belém Pará"
    "site:ciadetalentos.com.br/#jobs estágio Belém Pará",
    "site:ciadetalentos.com.br/#jobs trainee Belém Pará",
    "site:ciadeestagios.com.br/vagas-de-estagio/ estágio Belém Pará",
    "site:ciadeestagios.com.br/vagas-de-estagio/ trainee Belém Pará",
    "site:nube.com.br/ estágio Belém Pará",
    "site:nube.com.br/ trainee Belém Pará",
    "site:portal.ciee.org.br/quero-uma-vaga/ estágio Belém Pará",
    "site:portal.ciee.org.br/quero-uma-vaga/ trainee Belém Pará",
    "site:app.eureca.me/oportunidades estágio Belém Pará",
    "site:app.eureca.me/oportunidades trainee Belém Pará",
    "site:superestagios.com.br/index/vagasEstagio.php estágio Belém Pará",
    "site:superestagios.com.br/index/vagasEstagio.php trainee Belém Pará",
    "site:portalabre.com.br/Vagas.do?action=pesquisar estágio Belém Pará",
    "site:portalabre.com.br/Vagas.do?action=pesquisar trainee Belém Pará",
    "site:glassdoor.com.br/Vaga/bel%C3%A9m-estagio-vagas-SRCH_IL.0,5_IC2465757_KO6,13.htm tecnologia",
    "site:glassdoor.com.br/Vaga/bel%C3%A9m-estagio-vagas-SRCH_IL.0,5_IC2465757_KO6,13.htm moda",
    
]

PALAVRAS_OBRIGATORIAS = [
    "belém",
    "belem",
    "ananindeua",
    "para",
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

    if not any(p in texto for p in PALAVRAS_OBRIGATORIAS):
        return False

    if not any(p in texto for p in PALAVRAS_ESTAGIO):
        return False

    if any(p in texto for p in PALAVRAS_BLOQUEADAS):
        return False

    return True

PALAVRAS_INTERESSE = [
    "ti",
    "t.i",
    "tecnologia",
    "informatica",
    "informática",
    "computacao",
    "computação",
    "ciência",
    "ciencia",
    "ciência de dados",
    "dados",
    "ciencia da computacao",
    "ciência da computação",
    "sistemas",
    "sistema",
    "software",
    "desenvolvimento",
    "programacao",
    "programação",
    "engenharia de software",
    "ads",
    "análise e desenvolvimento de sistemas",
    "analise e desenvolvimento de sistemas",
    "moda",
    "design",
    "design de moda",
    "marketing",
    "publicidade",
    "ux",
    "ui"
]

PALAVRAS_BLOQUEADAS_IEL = [
    "contábeis",
    "contabeis",
    "contabilidade",
    "rh",
    "recursos humanos",
    "logística",
    "logistica",
    "administração",
    "administracao",
    "marketing",
    "publicidade",
    "propaganda",
    "comunicação",
    "jonalismo",
    "comunicação social"
]

def buscar_vagas_iel():

    vagas = []

    try:

        html = requests.get(
            "https://carreiras.iel.org.br/PA",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        ).text

        links = sorted(set(re.findall(
            r'https://carreiras\.iel\.org\.br/PA/vaga/[^\s"<]+',
            html
        )))

        for link in links:

            try:

                pagina = requests.get(
                    link,
                    headers={"User-Agent": "Mozilla/5.0"},
                    timeout=30
                ).text

                titulo = re.search(
                    r'"title":"([^"]+)"',
                    pagina
                )

                cidade = re.search(
                    r'"addressLocality":"([^"]+)"',
                    pagina
                )

                titulo = (
                    titulo.group(1)
                    if titulo else
                    ""
                )

                titulo_normalizado = titulo.lower()

                if not any(
                    palavra in titulo_normalizado
                    for palavra in PALAVRAS_INTERESSE
                ):
                    continue

                if any(
                    palavra in titulo_normalizado
                    for palavra in PALAVRAS_BLOQUEADAS_IEL
                ):
                    continue
               
                cidade = (
                    cidade.group(1)
                    if cidade else
                    ""
                )

                cidade_normalizada = cidade.lower()

                if cidade_normalizada not in [
                    "belém",
                    "belem",
                    "ananindeua"
                ]:
                    continue

                vagas.append(
                    {
                        "titulo": f"[IEL] {titulo}",
                        "link": link
                    }
                )

            except:
                pass

    except Exception as erro:

        print("Erro IEL:", erro)

    return vagas

def buscar_vagas_ciee():

    vagas = []

    try:

        for pagina in range(1, 51):

            url = (
                "https://api.ciee.org.br/vagas/"
                f"vitrine-vaga/publicadas?page={pagina}"
            )

            resposta = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
                timeout=30
            )

            dados = resposta.json()

            for vaga in dados.get(
                "content",
                []
            ):

                local = vaga.get(
                    "local"
                )

                if not local:
                    continue

                cidade = str(
                    local.get(
                        "cidade",
                        ""
                    )
                ).lower()

                if cidade not in [
                    "belém",
                    "belem",
                    "ananindeua"
                ]:
                    continue

                area = str(
                    vaga.get(
                        "areaProfissional",
                        ""
                    )
                )

                descricao = str(
                    vaga.get(
                        "descricao",
                        ""
                    )
                )

                texto = area.lower()

                if any(
                    palavra in texto
                    for palavra in PALAVRAS_BLOQUEADAS_IEL
                ):
                    continue

                if not any(
                    palavra in texto
                    for palavra in PALAVRAS_INTERESSE
                ):
                    continue

                codigo = vaga.get(
                    "codigoVaga"
                )

                empresa = vaga.get(
                    "nomeEmpresa",
                    "Empresa não informada"
                )

                vagas.append(
                    {
                        "titulo":
                            f"[CIEE] {area} - {empresa}",
                        "link":
                            (
                                f"https://web.ciee.org.br/login?codigoVaga={codigo}"
                            )
                    }
                )

    except Exception as erro:

        print(
            "Erro CIEE:",
            erro
        )

    print(
        "Vagas CIEE:",
        len(vagas)
    )

    for vaga in vagas:

        print(
            vaga["titulo"]
        )
    
    return vagas
    
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

            print(
                "Busca:",
                busca,
                "- resultados:",
                len(feed.entries)
            )
            
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

    print(
        "Google encontrou",
        len(vagas),
        "vagas"
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

    vagas_google = buscar_vagas()

    vagas_iel = buscar_vagas_iel()

    vagas_ciee = buscar_vagas_ciee()

    vagas = (
        vagas_google
        + vagas_iel
        + vagas_ciee
    )
    
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
