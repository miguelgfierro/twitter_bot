# Setup

Install twitter dependencies:

    $ sudo pip install twitter

Create a new app to get the credentials at [Twitter](https://apps.twitter.com/)

Create a JSON file of user data and put into `data/botname1`:

    {
        "consumer_key": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "consumer_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "access_token": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "access_token_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXX"
    }

Define your bots in `twitter_bots.conf`:

    {
      "logging": {
        "logfile": "logs/log",
        "max_bytes": 1000000,
        "backup_count": 5
      },
      "bot_usernames": [
        "botname1",
        "botname2",
        "botname3"
      ]
    }

Add your quotes to `data/quotes.json`

Cron it:

    # Run Twitter bots everyday at 13:00
    0 13 * * * /bin/bash -c 'cd /path/to/botdir && ./tweet_bots.py &>> cron.log'
