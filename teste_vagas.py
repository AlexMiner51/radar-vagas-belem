import requests

url = "https://trabalheconosco.vagas.com.br/vagas"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/130.0.0.0 "
        "Safari/537.36"
    )
}

resposta = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("STATUS:", resposta.status_code)

print()

print("URL FINAL:")
print(resposta.url)

print()

print("TAMANHO:")
print(len(resposta.text))

print()

print(resposta.text[:3000])
