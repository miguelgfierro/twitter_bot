A twitter bot that automatically tweets random quotes

Install twitter dependencies:

    $ sudo apt-get install libffi-dev libssl-dev
    $ sudo pip install -r requirements.txt

Create a new app to get the credentials at [Twitter](https://apps.twitter.com/)

Create a JSON file of user data and put into `data/botname1`:

    {
        "consumer_key": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "consumer_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "access_token": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "access_token_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXX"
    }

Define your bots in `bots.conf`:

    {
      "bot_usernames": [
        "botname1",
        "botname2",
        "botname3"
      ]
    }

Add your quotes to `data/quotes.json`

Cron it. Create a file called `crontab.txt` and fill it with something like this:

    # Run Twitter bots everyday at 13:00
    0 13 * * * /bin/bash -c 'cd /path/to/twitter_bot/src && python main.py &>> ../log/cron.log'
    # Or every three hours
    0 */3 * * *  /bin/bash -c 'cd /path/to/twitter_bot/src && python main.py &>> ../log/cron.log'
    
Finally to make a cron task:
    
    $ crontab crontab.txt
    
    
Disclaimer:

I hold no liability for what you do with this bot or what happens to you by using this bot. Abusing this bot can get you banned from Twitter, so make sure to read up on [proper usage](https://support.twitter.com/articles/76915-automation-rules-and-best-practices) of the Twitter API.
