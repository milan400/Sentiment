import tweepy
from textblob import TextBlob
import sys

consumer_key =  '8Vq0AulpCQKmdcZRkgGHGOsf4'
consumer_secret =  '9uQO0oJqpEOliqgYTlCS0xxx5MZGj7F9PFyfAOa7zlxkibgCrB'

access_token =  '989928898895884288-ZiUqWAILKo0yZBzbx2zJWo0xNjDqbe8'
access_token_secret =  'F1rdhw4OphNTBMQvWvO6vzF71bpZX3mOevpZvjoFKtpNy'

#authtentication
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#reading name 
names = sys.argv[1]



public_tweets = api.search(names)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("<br> <br>")
