import tweepy
import pandas as pd


# Informar as credenciais de acesso entre aspas
client = tweepy.Client(bearer_token="Inserir o bearer token aqui")

# Definir a consulta de pesquisa
query = "COLOCAR QUERY AQUI"

# Criar uma lista para armazenar os tweets
tweets = client.search_all_tweets(query=query)

tweetsCollected = []

for tweet in tweets.data:
    nomeDeUsuario = tweet['user']['name']
    dataEHora = tweet['created_at']
    texto = tweet['text']
    tweetsCollected.append([nomeDeUsuario, dataEHora, texto])
    

# Criar um DataFrame a partir da lista de tweets
df = pd.DataFrame(tweetsCollected, columns=['nomeDeUsuario', 'dataEHora', 'texto'])

# Salvar o DataFrame em um arquivo CSV
df.to_csv('tweets2024-01-15.csv', index=False)