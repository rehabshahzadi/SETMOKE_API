import argparse
from src.GooglePlusDataRetreivel import GooglePlus
from src.TwitterDataRetrievel import S_Twitter
from util.ConfigParser import ConfigParser

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Social media data extraction.')
    parser.add_argument("-k", "--keyword", type=str, required=True, dest='kwd', help='Enter a keyword to search')
    parser.add_argument("-l", "--limits", type=int, default=20, dest='limit', help='number of results to return')
    parser.add_argument("-o", "--outputfile", type=int, dest='filename', help='main.py -o <outputfile>')
    args = parser.parse_args()
    keyword_to_search=args.kwd
    limit=args.limit
    obj = ConfigParser()
    gp_api_credentials = obj.get("googlePlus_credentials")
    api_key = gp_api_credentials["api_key"]
    gp = GooglePlus(api_key)

    googlePlus_mentionlist = gp.get_googleplus_data(keyword_to_search, limit)
    twitter_api_credentials = obj.get("twitter_credentials")
    consumer_key = twitter_api_credentials["consumer_key"]
    consumer_secret = twitter_api_credentials["consumer_secret"]
    oauth_token = twitter_api_credentials["oauth_token"]
    oauth_token_secret = twitter_api_credentials["oauth_token_secret"]
    twitter=S_Twitter(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
    twitter_mentionlist=twitter.get_twitter_data(keyword_to_search, limit)