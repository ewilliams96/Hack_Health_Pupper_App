import praw, re, requests, os, glob, sys
from flask import Flask, request, render_template
from random import shuffle
'''
setting up a reddit user for scraping pictures
'''

user_agent = "pupper_finder"
reddit = praw.Reddit(user_agent=user_agent)
MIN_SCORE = 20 # min score for pup pictures
subreddit = "rarepuppers"

def scrape_pic():

    submissions = reddit.get_subreddit(subreddit).get_hot(limit=50)
    #now let's parse through what we scraped and decide what we return
    shuffle(submissions) #randomize
    for submission in submissions:
        if "imgur.com/" not in submission.url:
            continue
        if submission.score < MIN_SCORE:
            continue
       #now we need to get this image and download, and then serve it
        if "http://i.imgur.com/" in submission.url:


            break
    return None


'''
setting up machine learning stuff on pictures
'''


def create_message():
    """
    create pupper message
    :return:
    """


    return None


'''
setting up flask server stuff
'''

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('pupperPage.html')


if __name__ == '__main__':
    app.run()


