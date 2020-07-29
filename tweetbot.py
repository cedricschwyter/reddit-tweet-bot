import os
import time
import logging as log
import praw


SUBREDDIT = os.environ.get('TWEETBOT_REDDIT_SUBREDDIT')
TWITTER_USER = os.environ.get('TWEETBOT_TWITTER_USER')
TWITTER_KEY = os.environ.get('TWEETBOT_TWITTER_KEY')

reddit = praw.Reddit(client_id=os.environ.get('TWEETBOT_REDDIT_CLIENT_ID'),
                     client_secret=os.environ.get('TWEETBOT_REDDIT_CLIENT_SECRET'),
                     password=os.environ.get('TWEETBOT_REDDIT_USER_KEY'),
                     user_agent=os.environ.get('TWEETBOT_REDDIT_USER_AGENT'),
                     username=os.environ.get('TWEETBOT_REDDIT_USER_NAME'))
subreddit = reddit.subreddit(SUBREDDIT)

old_posts = subreddit.new(limit=25)


def tweet(post):
    log.debug('Tweeting post ' + post.title + '...')


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
