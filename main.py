import praw
import pdb
import re
import os

reddit = praw.Reddit('newbot')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("------------------------------------\n")
    print("done..................................")