import os
import time
import logging as log
import praw
import tweepy


SUBREDDIT = os.environ.get('TWEETBOT_REDDIT_SUBREDDIT')
TWITTER_USER = os.environ.get('TWEETBOT_TWITTER_USER')
TWITTER_KEY = os.environ.get('TWEETBOT_TWITTER_KEY')

reddit = praw.Reddit(client_id=os.environ.get('TWEETBOT_REDDIT_CLIENT_ID'),
                     client_secret=os.environ.get('TWEETBOT_REDDIT_CLIENT_SECRET'),
                     password=os.environ.get('TWEETBOT_REDDIT_USER_KEY'),
                     user_agent=os.environ.get('TWEETBOT_REDDIT_USER_AGENT'),
                     username=os.environ.get('TWEETBOT_REDDIT_USER_NAME'))
subreddit = reddit.subreddit(SUBREDDIT)

twitter_keys = {
    'consumer_key' : os.environ.get('TWEETBOT_TWITTER_CONSUMER_KEY'),
    'consumer_secret' : os.environ.get('TWEETBOT_TWITTER_CONSUMER_SECRET'),
    'access_token_key' : os.environ.get('TWEETBOT_TWITTER_ACCESS_TOKEN'),
    'access_token_secret' : os.environ.get('TWEETBOT_TWITTER_ACCESS_TOKEN_SECRET')
}

twitter_auth = tweepy.OAuthHandler(
                twitter_keys['consumer_key'],
                twitter_keys['consumer_secret']
            )
twitter_auth.set_access_token(
                twitter_keys['access_token'],
                twitter_keys['access_token_secret']
            )
twitter_api = tweepy.API(twitter_auth)

old_posts = subreddit.new(limit=25)


def tweet(post):
    try:
        log.debug('Tweeting post ' + post.title + '...')
        url = (post.url)
        file_name = url.split("/")
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            r = requests.get(url)
            with open(file_name,"wb+") as f:
                f.write(r.content)
            media = twitter_api.media_upload(file_name)
            post_result = twitter_api.update_status(status=post.title, 
                                                    media_ids=[media.media_id])
    except:
        log.error('Failed to tweet post ' + post.title)
        pass


def tweetbot():
    log.debug('Starting tweetbot...')
    while True:
        new_posts = subreddit.new(limit=25)
        for new_post in new_posts:
            if new_post not in old_posts:
                tweet(new_post)
        time.sleep(1)
    log.debug('Exiting tweetbot...')


if __name__ == '__main__':
    tweetbot()
