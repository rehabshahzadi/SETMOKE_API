import  tweepy, json
from twitter import *
from src.Mention import Mention

from src.Retweeter import Retweeter

class S_Twitter :

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):

     auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth1.set_access_token(oauth_token, oauth_token_secret)
     self.tweeter_api = tweepy.API(auth1)

     self.twitter = Twitter(auth = OAuth('2744706848-k2qvSjn2Z2RJuwuNi6nG3pUFfkV6LaQrjlPiX5C',
                               'Mg2rgYE8kqPmLDmWLEdVUka9yHybp3r4lY8Y1oEWatJ2n',
                               'cYIVpMAP9NhcEUURwYOmANLnU',
                  'qjmdfdoJpEaKAMgfjJ1WXnDRGzRzParxwfkCUh1WFvCxfRSBIu'))
    def get_data(self, tweets_list, mentionlist):

        for tweet in tweets_list:
            if(self.count<self.limit) :
                mention=Mention()
                mention.set_source("Twitter")
                mention.set_reshare_count(str(tweet["retweet_count"]))
                print("Tweet Text: " + tweet["text"])
                mention.set_text(tweet['text'])
                # # print(json.dumps(tweet, sort_keys=True, indent=4))
                # print("----------------Post Info-----------------------")
                # print("Tweet ID: " + tweet["id_str"])
                # print("Created at: " + tweet["created_at"])
                # mention.set_time(tweet["created_at"])
                # print("Tweet Language: " + tweet["lang"])
                # print("Retweet Count: " + str(tweet["retweet_count"]))


                if tweet["retweet_count"] != 0:
                    mention.set_display_name(tweet["retweeted_status"]["user"]["screen_name"])
                    mention.set_display_picture(tweet["retweeted_status"]['user']['profile_image_url'])
                    mention.set_status_id(str(tweet["retweeted_status"]['id']))
                    # print("----------------Retweeted User Info-----------------------")
                    # print("User ID: " + tweet["retweeted_status"]["user"]["id_str"])
                    # print("User Name: " + tweet["retweeted_status"]["user"]["name"])
                    # print("User Screen Name: " + tweet["retweeted_status"]["user"]["screen_name"])


                    # print("User Location: " + tweet["retweeted_status"]["user"]["location"])
                    # print("Tweets: " + str(tweet["retweeted_status"]['user']['statuses_count']))
                    # print("Folowing: " + str(tweet["retweeted_status"]['user']['friends_count']))
                    # print("Follower: " + str(tweet["retweeted_status"]['user']['followers_count']))
                    # print("Likes: " + str(tweet["retweeted_status"]['user']['favourites_count']))
                    # print("fav: " + str(tweet["retweeted_status"]['favorite_count']))
                    # print("status_id: " + str(tweet["retweeted_status"]['id']))


                    retweets = self.twitter.statuses.retweets._id(_id=str(tweet["retweeted_status"]['id']))
                    retweeterlist = []
                    for retweet in retweets:
                        retweeter = Retweeter()
                        retweeter.set_display_name(retweet["user"]["screen_name"])
                        retweeter.set_time(retweet["created_at"])
                        retweeter.set_display_picture(retweet["user"]["profile_image_url"])
                        retweeterlist.append(retweeter)
                        # print(" - retweeted by %s" % (retweet["user"]["screen_name"]))
                        # print("retweet time:"  +retweet["created_at"] )
                    mention.set_resharer(retweeterlist)
                else:
                    # print("----------------User Info-----------------------")
                    # print("User ID: " + tweet["user"]["id_str"])
                    # print("User Name: " + tweet["user"]["name"])
                  #  print("User Screen Name: " + tweet["user"]["screen_name"])
                    mention.set_display_picture(tweet['user']['profile_image_url'])
                    mention.set_display_name(tweet['user']['screen_name'])
                    # print("User Location: " + tweet["user"]["location"])
                    # print("Tweets: " + str(tweet['user']['statuses_count']))
                    # print("Folowing: " + str(tweet['user']['friends_count']))
                    # print("Follower: " + str(tweet['user']['followers_count']))
                    # print("Likes: " + str(tweet['user']['favourites_count']))
                mentionlist.append(mention)
                self.count=self.count+1
                print("<---------------------"+str(self.count)+"---------------------------->")
            else:
                    return mentionlist
        return mentionlist

    def get_twitter_data(self, keyword, limit):
      self.count=0
      self.limit=limit
      count=0
      mentionList=[]
      search_hashtag = tweepy.Cursor(self.tweeter_api.search, q=keyword).items(50)
      tweets_list = []
      for tweet in search_hashtag:
          tweets_list.append(json.loads(json.dumps(tweet._json)))
      id_ = tweets_list[len(tweets_list) - 1]["id"]
      mentionList=self.get_data(tweets_list ,mentionList)
      while (True):
        if self.count < self.limit :
          search_hashtag = tweepy.Cursor(self.tweeter_api.search, q=keyword, since_id=id_).items(50)
          for tweet in search_hashtag:
              print(json.dumps(tweet._json))
              for tweet in search_hashtag:
                  tweets_list.append(json.loads(json.dumps(tweet._json)))
              id_ = tweets_list[len(tweets_list) - 1]["id"]
              mentionList=self.get_data(tweets_list, mentionList)
              count=count+1
              print(count)

        else:
            break

      return mentionList