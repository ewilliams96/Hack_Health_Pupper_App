import praw, re, requests, os, glob, sys
from flask import Flask, request, render_template
import random as random
from DoggoIdentifier import DoggoAPICall
'''
setting up a reddit user for scraping pictures
'''

#regex for imgur pattern
imgurUrlPattern = re.compile(r'(http://i.imgur.com/(.*))(\?.*)?')
#regex for imgur pattern

user_agent = "pupper_finder"
reddit = praw.Reddit(user_agent=user_agent)
MIN_SCORE = 1 # min score for pup pictures
subreddit = "rarepuppers"


def yielding(ls):
    for i in ls:
        yield i

def scrape_pic():

    submissions = reddit.get_subreddit(subreddit).get_new(limit=300)
    #now let's parse through what we scraped and decide what we return

    temp_list = list(yielding(submissions))
    starting_index = random.randint(0,280)

    for submission in temp_list[starting_index:]:
        if "gifv" in submission.url:
            continue
        if submission.score < MIN_SCORE:
            continue
       #now we need to get this image and download, and then serve it
        if "http://i.imgur.com/" in submission.url:
            url = imgurUrlPattern.search(submission.url).group(1)
            # 
            dac = DoggoAPICall(url)

            if dac.verify_dog():
                return dac
            else:
                print("not a doggo", url)
            #checks for the case with a '?' in the filename
            
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
    doggo_object = scrape_pic()
    return render_template('pupperPage.html', image_url=doggo_object.url, doggo_message=doggo_object.bork_message())

if __name__ == '__main__':
    app.run(debug=True)



