#
# autores:
# Michel

# data: 22/03/2023

import requests

# URL da API:
# https://openweathermap.org/
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = "https://api.openweathermap.org/data/2.5/weather"

# definir a chave da API
# api_key = "SUA_CHAVE_API_AQUI"
api_key = "8990bd96b4a4d828f3b4176a1d51ad77"

# solicitar ao usuário que insira o nome da cidade
cidade = input("Digite o nome da cidade: ")

# enviar a solicitação para a API
# parametros = {"q": cidade, "appid": api_key}
parametros = {"q": cidade, "appid": api_key, "units": "metric", "lang": "pt_br"}

resposta = requests.get(url, params=parametros)
# print(resposta)
#
# verificar se a solicitação foi bem-sucedida
if resposta.status_code != 200:
    print("Erro ao obter dados da API.")
    
# extrair os dados da resposta
dados = resposta.json()
print(dados)

# exibir as informações do clima para a cidade
descricao = dados["weather"][0]["description"]
temperatura = dados["main"]["temp"]
print(f"O clima em {cidade} está {descricao} e a temperatura é de {temperatura:}°C.")
