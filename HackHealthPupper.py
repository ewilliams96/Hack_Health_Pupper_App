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
old_doggo = "string"
image_history = {}

def yielding(ls):
    for i in ls:
        yield i

def scrape_pic(old_doggo):

    submissions = reddit.get_subreddit(subreddit).get_new(limit=300)
    #now let's parse through what we scraped and decide what we return

    temp_list = list(yielding(submissions))

    random.shuffle(temp_list)
    for submission in temp_list:
        if "gifv" in submission.url:
            continue
        if submission.score < MIN_SCORE:
            continue
       #now we need to get this image and download, and then serve it
        if "http://i.imgur.com/" in submission.url:
            url = imgurUrlPattern.search(submission.url).group(1)
            dac = DoggoAPICall(url)
            if dac.verify_dog():
                del_keys = []
                for key in image_history.keys():
                    image_history[key] -= 1
                    if image_history[key] == 0:
                        del_keys.append(key)
                for key in del_keys:
                    del image_history[key]
                   
                if dac.url not in image_history:
                    image_history[dac.url] = 10 # minimum occurrences before next appearance
                    return dac
               
            else:
                print("not a doggo", url)
       
    return None




'''
setting up flask server stuff
'''

app = Flask(__name__)




@app.route('/')
def hello_world():
    doggo_object = scrape_pic(old_doggo)
    return render_template('pupperPage.html', image_url=doggo_object.url, doggo_message=doggo_object.bork_message())

if __name__ == '__main__':
    app.run(debug=True)



