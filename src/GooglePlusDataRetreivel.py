from apiclient import discovery
from src.Mention import Mention
class GooglePlus:

    def __init__(self, API_KEY):
        self.GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)


    def get_googleplus_data(self, keyword, limit) :
        mentionList=[]

        activity = self.GPLUS.activities().search(query=keyword, maxResults=20).execute()
        counter = 0
        while (True):


            nextToken = activity['nextPageToken']
            items = activity.get('items', [])
            for data in items:
                post = ' '.join(data['title'].strip().split())
                if post:
                    mention = Mention()
                    #  print(TMPL % (data['actor']['displayName'],
                    #               data['published'], post) )
                    print(data)
                    print("----------------Post Info-----------------------")
                    mention.set_source('GooglePlus')
                    print("Post ID: " + data["id"])
                    print("Post url: " + data["url"])
                    mention.set_status_id(data['url'])
                    print("Created at: " + data["published"])
                    mention.set_time(data["published"])
                    print("Resharer Count: " + str(data["object"]["resharers"]['totalItems']))
                    mention.set_reshare_count(str(data["object"]["resharers"]['totalItems']))
                    print("Replies Count: " + str(data["object"]["replies"]['totalItems']))
                    print("Plusoners Count: " + str(data["object"]["plusoners"]['totalItems']))
                    print("Text: " + data["object"]['content'])
                    mention.set_text(data["object"]['content'])
                    for s in data['object']:
                        if s == 'attachments':
                            attachments = data["object"]['attachments']
                            for attachment in attachments:
                                print("attachments:" + attachment["url"])
                    print("----------------User Info-----------------------")
                    print("Diplay Name:" + data['actor']['displayName'])
                    mention.set_display_name(data['actor']['displayName'])
                    mention.set_display_picture( data['actor']['image']['url'])
                    print("Display Image:" + data['actor']['image']['url'])
                    mentionList.append(mention)
                    counter = counter + 1
                    print("--------------------------------------------"+ str(counter))
                    if counter>=limit:
                        break
            if counter<limit :
             activity = self.GPLUS.activities().search(query=keyword, maxResults=20, pageToken=nextToken).execute()
            else:
                break
        return mentionList