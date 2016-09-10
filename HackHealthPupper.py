import praw, re, requests, os, glob, sys
from flask import Flask, request, render_template
import random as random
'''
setting up a reddit user for scraping pictures
'''

#regex for imgur pattern
imgurUrlPattern = re.compile(r'(http://i.imgur.com/(.*))(\?.*)?')
#regex for imgur pattern

user_agent = "pupper_finder"
reddit = praw.Reddit(user_agent=user_agent)
MIN_SCORE = 10 # min score for pup pictures
subreddit = "rarepuppers"


def yielding(ls):
    for i in ls:
        yield i

def scrape_pic():

    submissions = reddit.get_subreddit(subreddit).get_hot(limit=500)
    #now let's parse through what we scraped and decide what we return

    temp_list = list(yielding(submissions))
    starting_index = random.randint(0,400)

    for submission in temp_list[starting_index:]:
        if "gifv" in submission.url:
            continue
        if submission.score < MIN_SCORE:
            continue
       #now we need to get this image and download, and then serve it
        if "http://i.imgur.com/" in submission.url:
            pre_worked_url = imgurUrlPattern.search(submission.url)

            return pre_worked_url
            #checks for the case with a '?' in the filename
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
    image_url = scrape_pic()

    print(image_url.group(1))
    return render_template('pupperPage.html', image_url=image_url.group(1))

@app.route('/get_image')
def get_image():
    image_url = scrape_pic()
    return render_template('pupperPage.html',image_url=image_url.group(1))

if __name__ == '__main__':
    app.run(debug=True)


