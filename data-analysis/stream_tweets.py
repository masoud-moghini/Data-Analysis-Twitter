#Stream api let to stream data flowing in twitter
#api twitter let us to know about specific twitter account


from tweepy import OAuthHandler,Stream,API
from tweepy.streaming import StreamListener
import json
Consumer_key='dfyieLmEdSIonrq8SvMAE1yFN'
Consumer_secret='I7vpLV5HrKEyFqMN1fhKPfhg2vKmMhXanU88I5HAW6bDxIilbG'
Access_Token='447360683-1Ck8kOQaaLFj9XOumBeAAqB9y9TFzJx5Hktq9HoO'
Access_Token_Secret='7n3cxD3HcIWPF97DAeKx1jgiRpX9x6ukDBTto0EHJeEQJ'


auth=OAuthHandler(Consumer_key,Consumer_secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

class PrintListener(StreamListener):
    def on_status(self,status):
        if not status.text[:3]=='RT ':
            print(status.text)
            print(status.author.screen_name,
                status.created_at,
                '\n',status.source,
                '\n')
        
        
        #print (dir(status))
    def on_error(self,status_code):
        print("Error at {}".format(status_code))
        return True 

    def on_timeout(self):
        print("Time out !")
        return True

def printToTerminal():
    listener=PrintListener()
    stream=Stream(auth,listener)
    languages=('fa',)
    stream.sample(languages=languages)
def pull_down_tweets(screen_name):
    api=API(auth)
    tweets= api.user_timeline(screen_name=screen_name,count=200)
    with open('milan.json',"w")as file:
        for tweet in tweets:
            #print(json.dumps(tweet._json,indent=4))
            file.write(str(tweet.text)+"\n\n\n")

