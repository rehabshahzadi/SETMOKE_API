import tweepy

from src.GooglePlusDataRetreivel import GooglePlus
from src.TwitterDataRetrievel import S_Twitter
from util.ConfigParser import ConfigParser

if __name__ == '__main__':

    keyword_to_search='imran khan'
    obj = ConfigParser()
    gp_api_credentials = obj.get("googlePlus_credentials")
    api_key = gp_api_credentials["api_key"]
    gp = GooglePlus(api_key)

    googlePlus_mentionlist = gp.get_googleplus_data(keyword_to_search, 30)


    twitter_api_credentials = obj.get("twitter_credentials")
    consumer_key = twitter_api_credentials["consumer_key"]
    consumer_secret = twitter_api_credentials["consumer_secret"]
    oauth_token = twitter_api_credentials["oauth_token"]
    oauth_token_secret = twitter_api_credentials["oauth_token_secret"]
    twitter=S_Twitter(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
    twitter_mentionlist=twitter.get_twitter_data(keyword_to_search, 30)