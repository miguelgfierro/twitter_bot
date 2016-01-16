from twitter_bot import TwitterBot
import json


def load_conf(filename):
    with open(filename) as f:
        return json.load(f)

def tweet_quote():
    conf = load_conf('data/bots.conf')
    for bot_username in conf['bot_usernames']:
        try:
            bot = TwitterBot(bot_username)
            tweet = bot.tweet_random_quote()
            if tweet:
                msg = '%s tweeted %s' % (bot_username, tweet)
                print msg
            else:
                msg = '%s failed to tweet' % bot_username
                print msg

        except Exception as e:
            error_msg = "%s ERROR + %s" % (bot_username, str(e))
            print error_msg

if __name__ == "__main__":
    tweet_quote()