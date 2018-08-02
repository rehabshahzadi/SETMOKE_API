import argparse
from src.GooglePlusDataRetreivel import GooglePlus
from src.TwitterDataRetrievel import S_Twitter#
from util.ConfigParser import ConfigParser
# import util.Input
import json

def save_to_file(googlePlus_mentionlist):
    length=len(googlePlus_mentionlist)
    writer=open("temp",'w')
    writer.write("[\n")
   # jsonArray=[]
    count=1
    for items in googlePlus_mentionlist:

        resharers=items.get_resharer()
        if not resharers:
         resharers='[]'
        else:
         resharers=items.get_resharer()

        my_json_string = json.dumps({'text': items.get_text(),'display_name': items.get_display_name(),
        'time': items.get_time(),
        'reshare_count' :items.get_reshare_count(),
        'status_id':items.get_status_id(),
        'source':items.get_source(),
        'resharers':resharers})
        if count < length:
            writer.write(my_json_string+",")
        else:
            writer.write(my_json_string )
        count=count+1
    writer.write("]")
if __name__ == '__main__':

 # main()
    #keyword_to_search=util.Input.kwd
    #limit=util.Input.limit
    keyword_to_search="imran khan"
    limit=2
    obj = ConfigParser()
    gp_api_credentials = obj.get("googlePlus_credentials")
    api_key = gp_api_credentials["api_key"]
    gp = GooglePlus(api_key)

    googlePlus_mentionlist = gp.get_googleplus_data(keyword_to_search, limit)
    print(googlePlus_mentionlist)

    save_to_file(googlePlus_mentionlist)
    twitter_api_credentials = obj.get("twitter_credentials")
    consumer_key = twitter_api_credentials["consumer_key"]
    consumer_secret = twitter_api_credentials["consumer_secret"]
    oauth_token = twitter_api_credentials["oauth_token"]
    oauth_token_secret = twitter_api_credentials["oauth_token_secret"]
    twitter=S_Twitter(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
    twitter_mentionlist=twitter.get_twitter_data(keyword_to_search, limit)

    



