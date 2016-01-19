import json

from twitter_bot import TwitterBot


def load_conf(filename):
    with open(filename) as f:
        return json.load(f)

def main():
    import os
    print(os.getcwd())
    conf_file = '../data/bots.conf'
    conf = load_conf(conf_file)
    for bot_username in conf['bot_usernames']:
        try:
            bot = TwitterBot(bot_username)

            tweet = bot.tweet_random_quote()
            if tweet:
                msg = '%s tweeted %s' % (bot_username, tweet.text)
                print msg
            else:
                msg = '%s failed to tweet' % bot_username
                print msg

            result = bot.retweet_keyword_home_timeline()

        except Exception as e:
            error_msg = "%s ERROR: %s" % (bot_username, str(e))
            print error_msg

if __name__ == "__main__":
    main()