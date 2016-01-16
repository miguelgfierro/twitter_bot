A twitter bot that automatically tweets random quotes

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

Define your bots in `bots.conf`:

    {
      "bot_usernames": [
        "botname1",
        "botname2",
        "botname3"
      ]
    }

Add your quotes to `data/quotes.json`

Cron it:

    # Run Twitter bots everyday at 13:00
    0 13 * * * /bin/bash -c 'cd /path/to/botdir && python main.py &>> cron.log'
    # Every three hours
    0 */2 * * *  /bin/bash -c 'cd /path/to/botdir && python main.py &>> cron.log'
