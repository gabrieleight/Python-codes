import tweepy
import pandas as pd
from datetime import datetime

def get_client(bearer_token):
    # Autenticar na API do Twitter
    client = tweepy.Client(bearer_token)
    return client

def collecting_tweets(client, query):
    tweets = client.search_all_tweets(query=query)

    tweetsCollected = []

    for tweet in tweets.data:
        nomeDeUsuario = tweet['user']['name']
        dataEHora = tweet['created_at']
        texto = tweet['text']
        tweetsCollected.append([nomeDeUsuario, dataEHora, texto])
    
    return tweetsCollected
    
def exporting_tweets(tweetsCollected):
    # Criar um DataFrame a partir da lista de tweets
    df = pd.DataFrame(tweetsCollected, columns=['nomeDeUsuario', 'dataEHora', 'texto'])

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(f"tweets{datetime.today}.csv", index=False)
    print("Tweets exportados com sucesso!")

###################################################################################################
###################################################################################################
#############VOCÊ PODE APENAS ALTERAR O CODIGO ABAIXO PARA TESTAR AS FUNCIONALIDADES###############

def main():
    # Token de acesso
    bearer_token = "your_bearer_token_here"
    
    # Criar um cliente
    client = get_client(bearer_token)
    
    # Query de busca
    query = "your_query_here"
    
    # Coletar tweets
    tweetsCollected = collecting_tweets(client, query)
    
    # Exportar tweets
    exporting_tweets(tweetsCollected)
    
    
if __name__ == "__main__":
    main()