import tweepy
from dotenv import load_dotenv
import os 
import service_scraping

load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter V1
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)


# Authenticate to Twitter V2
client = tweepy.Client(
    bearer_token,
    api_key,
    api_secret_key,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

#Tweet
api = tweepy.API(auth)
media_id = api.media_upload("yabastamacri.jfif").media_id_string


data = service_scraping.service_scrapping()
hora, profundidad, magnitud, latitud, longitud, provincia = data

tweet_text = f"Temblor en Argentina: Provincia de : {provincia} de {magnitud} en la escala de richter. \n- Profundidad: {profundidad}\n- Latitud: {latitud}\n- Longitud: {longitud}\n- Hora: {hora}"

#Send tweet
client.create_tweet(text=tweet_text)


#Send tweet with media
#client.create_tweet(text=tweet_text, media_ids=[media_id])
print("Tweet sent!")

