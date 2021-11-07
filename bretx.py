

#El primer pas serà importar les llibreries que necessitarem
import tweepy
import pandas
import time

#A continuació inicialitzarem les claus donades per l'API de Twitter per poder accedir-hi
consumer_key = "4ikBRcdJVZJmcXF8WOsuQ0VY5"
consumer_secret = "ksmxgT77nUprvScPsPqb3bgy387cLkuTaiIMmqsKfsOcoA5Bbh"
access_token = "1455605536582512643-zJ9scn7mf8WYmNca2DB90cNLHYVC8P"
access_token_secret = "ZLuoquSYSjEyUVzKxDFlLoSkGG9588Ee7ZCftqCQZhoeM"

#El pas següent serà per poder obtenir accés a l'API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#El text que buscarem serà la paraula clau "Brexit" i ho farem fins a 1000 iteracions
text_query = 'brexit'
count = 1000

try:
    # Crearem la query utilitzant les opcions que necessitem de l'API
    tweets = tweepy.Cursor(api.search_tweets, q=text_query).items(count)

    # Treurem la informació de cada un dels iterables dins la variable tweets
    tweets_list = [[tweet.created_at,
                    tweet.id,
                    tweet.text,
                    tweet.truncated,
                    tweet.in_reply_to_screen_name,
                    tweet.place,
                    tweet.is_quote_status,
                    tweet.retweeted] for tweet in tweets]

    # Creem un dataset a partir de tweets_list
    tweets_df = pandas.DataFrame(tweets_list)

except BaseException as e:
    print('failed on_status,', str(e))
    time.sleep(3)

#Per poder visualitzar i treballar amb el dataset, l'exportarem a csv
#Cal ficar el directori  d'on volem guardar el document
tweets_df.to_csv(r'C:\Users\lidia\OneDrive\Escriptori\MÀSTER UOC\Brexit_consequences.csv')
