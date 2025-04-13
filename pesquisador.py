import requests
from bs4 import BeautifulSoup
import json

def pesquisar_dores(nicho, persona):
    """
    Pesquisa dores reais no Google e Reddit.

    Args:
        nicho (str): Nicho da persona.
        persona (str): Persona a ser pesquisada.

    Returns:
        dict: Relatório com os principais problemas encontrados.
    """

    dores = {}

    # Pesquisa no Google
    google_query = f"{nicho} {persona} problemas"
    google_url = f"https://www.google.com/search?q={google_query}"
    google_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        google_response = requests.get(google_url, headers=google_headers)
        google_response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        google_soup = BeautifulSoup(google_response.content, "html.parser")
        google_results = google_soup.find_all("div", class_="tF2Cxc")

        for result in google_results[:5]:  # Limita a 5 resultados
            title = result.find("h3").text
            link = result.find("a")["href"]
            dores[title] = link

    except requests.exceptions.RequestException as e:
        print(f"Erro na pesquisa do Google: {e}")

    # Pesquisa no Reddit
    reddit_query = f"{nicho} {persona} problems"
    reddit_url = f"https://www.reddit.com/search/?q={reddit_query}"

    try:
        reddit_response = requests.get(reddit_url, headers=google_headers)
        reddit_response.raise_for_status()

        reddit_soup = BeautifulSoup(reddit_response.content, "html.parser")
        reddit_results = reddit_soup.find_all("div", class_="_1oQyIsiPHYt6nx7VOmd1sz")

        for result in reddit_results[:5]:  # Limita a 5 resultados
            title = result.find("h3").text
            link = "https://www.reddit.com" + result.find("a")["href"]
            dores[title] = link

    except requests.exceptions.RequestException as e:
        print(f"Erro na pesquisa do Reddit: {e}")

    return dores

# Exemplo de uso
nicho = "SST"
persona = "Técnico"
relatorio = pesquisar_dores(nicho, persona)
print(json.dumps(relatorio, indent=4))