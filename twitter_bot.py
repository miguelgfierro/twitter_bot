from twitter import Twitter,OAuth
import json
from random import choice

class TwitterBot:

    def __init__(self, name):
        botfile = open('data/' + name, 'rb')
        self.data = json.load(botfile)
        botfile.close()
        quote_file = open('data/quotes.json','rb')
        self.quotes_data = json.load(quote_file)
        quote_file.close()
        self.quotes = self.quotes_data['quotes']
        self.twitter_client = Twitter(auth = OAuth(self.data['access_token'], self.data['access_token_secret'],
                                       self.data['consumer_key'], self.data['consumer_secret']))

    def tweet_random_quote(self):
        trimmed_quote = self.random_quote()[:140]
        result = self.twitter_client.statuses.update(status = trimmed_quote)
        return result

    def random_quote(self):
        return choice(self.quotes)