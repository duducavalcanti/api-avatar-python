# Instale a biblioteca no Colab ou terminal:
# pip install googletrans==4.0.0-rc1

# Importa os módulos necessários
import requests
from googletrans import Translator

# URL da API
url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Faz a requisição
resposta = requests.get(url)

# Converte para JSON
dados = resposta.json()

# Cria o tradutor
tradutor = Translator()

# Função para traduzir textos
def traduzir_texto(texto):

    # Verifica se o texto existe
    if texto:
        traducao = tradutor.translate(texto, dest='pt')
        return traducao.text

    return "Sem informação"

# Percorre os personagens
for personagem in dados:

    # Obtém os atributos
    nome = personagem.get("name", "Sem nome")
    afiliacao = personagem.get("affiliation", "Sem afiliação")

    # Traduz os atributos
    nome_traduzido = traduzir_texto(nome)
    afiliacao_traduzida = traduzir_texto(afiliacao)

    # Exibe os resultados
    print("Nome original:", nome)
    print("Nome traduzido:", nome_traduzido)

    print("Afiliação original:", afiliacao)
    print("Afiliação traduzida:", afiliacao_traduzida)

    print("-" * 50)