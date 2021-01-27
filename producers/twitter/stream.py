import tweepy
class StreamListener(tweepy.StreamListener):
    def __init__(self, producer):
        self.producer = producer
        super().__init__()

    def on_status(self, status):
        data = {'tweet': status.text}
        self.producer.send('numtest', value=data)
        
    def on_error(self, status_code):
        if status_code == 420:
            return False