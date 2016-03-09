# Tweets
import tweepy
from tweepy import OAuthHandler

consumer_key = 'ShxRj9kwBYRf6RVkA2HuChnRh'
consumer_secret = 'SAI6gHyfNuwUo0FsCL6vfjqNPqgmVeysu9TGwDuEgA38LwHxIS'
access_token = '105704081-w2MknuPm4t9GKafNENf3f4ruaohtzLlhsZh1TNDb'
access_secret = 'KRDbAXsb5T7lStCubTiKBA5oUqiCVaf1oIwoOCxeiE8L6'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(20):
    # Process a single status
    print(status.text) 
