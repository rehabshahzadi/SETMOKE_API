from SETMOK_API.util.ConfigurationParser import ConfigurationParser
from SETMOK_API.src.GooglePlusDataRetreivel import GooglePlus
from SETMOK_API.src.TwitterDataRetrievel import S_Twitter
import sys
class SETMOKE_API:

    def __init__(self, keyword=None, configpath=None,limit=2,source=None):
        self.set_keyword(keyword)
        self.set_config_path(configpath)
        self.set_source(source)
        self.set_limit(limit)

    def set_limit(self, limit):
        self.limit = limit

    def set_keyword(self,keyword):
        self.keyword = keyword
        if self.get_keyword()== None:
            sys.exit("Please provide a keyword to search \n SETMOKE_API(<keyword>,<config_path>,<source>,<limit>)")

    def set_config_path(self, config_path):
        self.config_path = config_path
        if self.get_config_path()==None :
            sys.exit("config_path is empty.Please provide config file path \n SETMOKE_API(<keyword>,<config_path>,<source>,<limit>)")

    def set_source(self, source):
        self.source = source

    def get_limit(self):
        return self.limit

    def get_keyword(self):
        return self.keyword

    def get_config_path(self):
        return self.config_path

    def get_source(self):
        return self.source


    def get_googleplus_data(self):
        self.set_source("googlePlus")
        obj = ConfigurationParser(self.get_config_path())
        gp_api_credentials = obj.get("googlePlus_credentials")
        api_key = gp_api_credentials["api_key"]
        gp = GooglePlus(api_key)
        googlePlus_mentionlist = gp.get_googleplus_data(self.keyword, self.limit)
        print(googlePlus_mentionlist)
        return googlePlus_mentionlist



    def get_Twitter_data(self):
        self.set_source("Twitter")
        obj = ConfigurationParser(self.get_config_path())
        twitter_api_credentials = obj.get("twitter_credentials")
        consumer_key = twitter_api_credentials["consumer_key"]
        consumer_secret = twitter_api_credentials["consumer_secret"]
        oauth_token = twitter_api_credentials["oauth_token"]
        oauth_token_secret = twitter_api_credentials["oauth_token_secret"]
        twitter = S_Twitter(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
        twitter_mentionlist = twitter.get_twitter_data(self.keyword, self.limit)
        return twitter_mentionlist


    def get_data(self):
        if self.get_source()=='googlePlus':
            return self.get_googleplus_data()
        elif self.get_source()=='twitter':
            return self.get_Twitter_data()
        else :
            google_data=self.get_googleplus_data()
            twitter_data=self.get_Twitter_data()
            data=google_data + twitter_data
            return data
