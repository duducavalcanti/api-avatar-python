# Importa o módulo requests
import requests

# URL da API que será consultada
url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Cria a requisição GET
resposta = requests.get(url)

# Converte a resposta para JSON
dados = resposta.json()

# Exibe o conteúdo da resposta
#print(dados)

# Percorre os personagens
for personagem in dados:

    # Exibe algumas informações
    print("Nome:", personagem["name"])
    print("Aliados:", personagem["allies"])
    print("Inimigos:", personagem["enemies"])
    print("-" * 40)