
importar json
solicitações de importação
importar feedparser
importar re
from datetime import datetime

BUSCAS = [
    "site:gupy.io estágio tecnologia Belém Pará",
    "site:gupy.io estágio TI Belém Pará",
    "site:gupy.io estágio ciência da computação Belém Pará",
    "site:gupy.io estágio sistemas de informação Belém Pará",
    "site:gupy.io estágio desenvolvimento software Belém Pará",

    "site:linkedin.com/jobs estágio tecnologia Belém Pará",
    "site:linkedin.com/jobs estágio TI Belém Pará",
    "site:linkedin.com/jobs estágio de programação Belém Pará",

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
    "site:ciadetalentos.com.br/#jobs estagiário Belém Pará",
    "site:ciadeestagios.com.br/vagas-de-estagio/ estágio Belém Pará",
    "site:ciadeestagios.com.br/vagas-de-estagio/ estagiário Belém Pará",
    "site:nube.com.br/ estágio Belém Pará",
    "site:nube.com.br/ trainee Belém Pará",
    "site:portal.ciee.org.br/quero-uma-vaga/ estágio Belém Pará",
    "site:portal.ciee.org.br/quero-uma-vaga/ estagiário Belém Pará",
    "site:app.eureca.me/oportunidades estágio Belém Pará",
    "site:app.eureca.me/oportunidades estagiário Belém Pará",
    "site:superestagios.com.br/index/vagasEstagio.php estágio Belém Pará",
    "site:superestagios.com.br/index/vagasEstagio.php estagiário Belém Pará",
    "site:portalabre.com.br/Vagas.do?action=pesquisar estágio Belém Pará",
    "site:portalabre.com.br/Vagas.do?action=pesquisar estagiário Belém Pará",
    "site:glassdoor.com.br/Vaga/bel%C3%A9m-estagio-vagas-SRCH_IL.0,5_IC2465757_KO6,13.htm tecnologia",
    "site:glassdoor.com.br/Vaga/bel%C3%A9m-estagio-vagas-SRCH_IL.0,5_IC2465757_KO6,13.htm moda",
    
]

PALAVRAS_OBRIGATORIAS = [
    "belém",
    "belém",
    "ananindeua",
    "pára",
    "pára"
]

PALAVRAS_ESTAGIO = [
    "estágio",
    "estágio",
    "estagiário",
    "estagiario",
    "estagiário"
]

PALAVRAS_BLOQUEADAS = [
    "guiné",
    "guiné",
    "guiné-bissau",
    "bissau",
    "África",
    "África do Sul",
    "escritório em casa",
    "remoto",
    "remoto",
    "São Paulo",
    "São Paulo",
    "rio de janeiro",
    "curitiba",
    "porto alegre",
    "Bangkok",
    "Tailândia"
]


def carregar_histórico():

    tentar:
        com open("seen.json", "r", encoding="utf-8") as f:
            retornar conjunto(json.load(f))
    exceto:
        retornar conjunto()


def salvar_histórico(histórico):

    com open("seen.json", "w", encoding="utf-8") as f:
        json.dump(
            lista(histórico),
            f,
            garantir_ascii=Falso,
            recuo=2
        )


def vaga_valida(texto):

    texto = texto.lower()

    se não houver (p em texto para p em PALAVRAS_OBRIGATORIAS):
        retornar Falso

    if not any(p em texto para p em PALAVRAS_ESTAGIO):
        retornar Falso

    se houver(p em texto para p em PALAVRAS_BLOQUEADAS):
        retornar Falso

    retornar Verdadeiro

PALAVRAS_INTERESSE = [
    "ti",
    "ti",
    "tecnologia",
    "informática",
    "informática",
    "computação",
    "computação",
    "ciência",
    "ciência",
    "ciência de dados",
    "dados",
    "ciência da computação",
    "ciência da computação",
    "sistemas",
    "sistema",
    "software",
    "desenvolvimento",
    "programação",
    "programação",
    "engenharia de software",
    "anúncios",
    "análise e desenvolvimento de sistemas",
    "analisar e desenvolver sistemas",
    "moda",
    "projeto",
    "design de moda",
    "marketing",
    "publicidade",
    "ux",
    "interface do usuário"
]

PALAVRAS_BLOQUEADAS_IEL = [
    "contábeis",
    "contabeis",
    "contabilidade",
    "rh",
    "recursos humanos",
    "logística",
    "logística",
    "administração",
    "administração",
    "marketing",
    "publicidade",
    "propaganda",
    "comunicação",
    "jonalismo",
    "comunicação social"
]

def buscar_vagas_iel():

    = []

    tentar:

        html = solicitações.get(
            "https://carreiras.iel.org.br/PA",
            headers={"User-Agent": "Mozilla/5.0"},
            tempo limite=30
        ).texto

        links = sorted(set(re.findall(
            r'https://carreiras\.iel\.org\.br/PA/vaga/[^\s"<]+',
            html
        )))

        para link em links:

            tentar:

                pagina = requests.get(
                    link,
                    headers={"User-Agent": "Mozilla/5.0"},
                    tempo limite=30
                ).texto

                título = re.pesquisa(
                    r'"título":"([^"]+)"',
                    página
                )

                cidade = re.pesquisa(
                    r'"addressLocality":"([^"]+)"',
                    página
                )

                título = (
                    titulo.grupo(1)
                    se titulo senão
                    ""
                )

                titulo_normalizado = titulo.lower()

                se não houver nenhum(
                    palavra em titulo_normalizado
                    para palavra em PALAVRAS_INTERESSE
                ):
                    continuar

                se houver(
                    palavra em titulo_normalizado
                    para palavra em PALAVRAS_BLOQUEADAS_IEL
                ):
                    continuar
               
                cidade = (
                    cidade.grupo(1)
                    se cidade senão
                    ""
                )

                cidade_normalizada = cidade.lower()

                se cidade_normalizada não estiver em [
                    "belém",
                    "belém",
                    "ananindeua"
                ]:
                    continuar

                vagas.append(
                    {
                        "título": f"[IEL] {título}",
                        "link": link
                    }
                )

            exceto:
                passar

    exceto Exception como erro:

        print("Erro IEL:", erro)

    retorno

def buscar_vagas_ciee():

    = []

    tentar:

        para página em range(1, 51):

            url = (
                "https://api.ciee.org.br/vagas/"
                f"vitrine-vaga/publicadas?page={página}"
            )

            resposta = requests.get(
                URL,
                cabeçalhos={
                    "User-Agent": "Mozilla/5.0"
                },
                tempo limite=30
            )

            dados = resposta.json()

            para vaga em dados.get(
                "contente",
                []
            ):

                local = vaga.get(
                    "local"
                )

                se não for local:
                    continuar

                cidade = str(
                    local.get(
                        "†",
                        ""
                    )
                ).mais baixo()

                se cidade não estiver em [
                    "belém",
                    "belém",
                    "ananindeua"
                ]:
                    continuar

                área = str(
                    vaga.obter(
                        "áreaProfissional",
                        ""
                    )
                )
                area_normalizada = area.lower()       
                
                se area_normalizada em [
                    "administrativa",
                    "contabilidade",
                    "campo do direito",
                    "recursos humanos"
                ]:
                    continuar
                descrição = str(
                    vaga.obter(
                        "descricao",
                        ""
                    )
                )

                texto = área.lower()

                se houver(
                    palavra em texto
                    para palavra em PALAVRAS_BLOQUEADAS_IEL
                ):
                    continuar

                se não houver nenhum(
                    palavra em texto
                    para palavra em PALAVRAS_INTERESSE
                ):
                    continuar

                código = vaga.get(
                    "codigoVaga"
                )

                empresa = vaga.get(
                    "nomeEmpresa",
                    "Empresa não informada"
                )

                vagas.append(
                    {
                        "título":
                            f"[CIEE] {área} - {empresa}",
                        "link":
                            (
                                f"https://web.ciee.org.br/login?codigoVaga={codigo}"
                            )
                    }
                )

    exceto Exception como erro:

        imprimir(
            "Erro CIEE:",
            erro
        )

    imprimir(
        "Vagas CIEE:",
        len(vagas)
    )

    para vaga em amigo:

        imprimir(
            vaga["título"]
        )
    
    retorno
    
def buscar_vagas():

    = []

    histórico = carregar_histórico()

    para busca em BUSCAS:

        tentar:

            url = (
                "https://news.google.com/rss/search?q="
                + busca.replace(" ", "+")
            )

            feed = feedparser.parse(url)

            imprimir(
                "Busca:",
                busca,
                "- resultados:",
                len(feed.entries)
            )
            
            para item em feed.entries:

                título = item.title.strip()
                link = item.link.strip()

                texto = f"{titulo} {link}"

                se não vaga_valida(texto):
                    continuar

                se link em histórico:
                    continuar

                histórico.adicionar(link)

                vagas.append(
                    {
                        "título": título,
                        "link": link
                    }
                )

        exceto Exception como erro:

            print("Erro:", erro)

    salvar_histórico(histórico)

    imprimir(
        "Google encontrou",
        len(vagas),
        "vagas"
)
    
    retorno


def enviar_telegram(texto):

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    solicitações.post(
        URL,
        dados={
            "chat_id": chat_id,
            "texto": texto[:4000]
        },
        tempo limite=30
    )


def main():

    jo_google = buscar_vagas()

    vagas_iel = buscar_vagas_iel()

    vagas_ciee = buscar_vagas_ciee()

    = (
        joão_google
        +seu_iel
        +sociedade_da_sociedade
    )
    
    cabecallho = (
        f"📢 Radar de Estágios - Belém/PA\n"
        f"{datetime.now().strftime('%d/%m/%Y')}\n\n"
    )

    se não for um:

        mensagem = (
            cabecalho
            + "Nenhuma nova vaga encontrada hoje."
        )

    outro:

        linhas = []

        para vaga em mercado[:15]:

            linhas.append(
                f"• {vaga['titulo']}\n{vaga['link']}"
            )

        mensagem = cabecalho + "\n\n".join(linhas)

    enviar_telegram(mensagem)


se __name__ == "__main__":
    principal()
