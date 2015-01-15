import json
import tweepy

import bot



class StreamListener(tweepy.StreamListener):
    def on_data(self, data):
        print('Incoming: {0}'.format(data))
        tweet = json.loads(data)

        id = tweet['id_str']
        bot.api.create_favorite(id)

        # Return True to keep the stream listener listening.
        return True



def main():
    listener = StreamListener()
    stream = tweepy.Stream(bot.auth, listener)
    stream.filter(track=('entrepreneur', 'startup', 'marketing', 'growth hack', 'growth hacking', 'growth hacker'))

if __name__ == '__main__':
    main()
