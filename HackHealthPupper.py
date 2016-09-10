import praw, re, requests, os, glob, sys
from flask import Flask, request, render_template
import random as random
from DoggoIdentifier import DoggoAPICall
import operator
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
top_tags_dict = {}

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

sounds = ["Dog.mp3","Puppy.mp3","Puppy2.mp3","Dog2.mp3"]

current_doggo = None

@app.route('/')
def hello_world():
    doggo_object = scrape_pic(old_doggo)
    global current_doggo
    current_doggo = doggo_object

    return render_template('pupperPage.html',values="", description="", sound=sounds[random.randint(0,3)], image_url=doggo_object.url, doggo_message=doggo_object.bork_message())

@app.route('/uppup')
def up_pup():
    classes = current_doggo.get_classes()
    for c in classes:
        if c in top_tags_dict:
            top_tags_dict[c] += 1
        else:
            top_tags_dict[c] = 1
    print("hello")
    print(top_tags_dict)
    doggo_object = scrape_pic(old_doggo)
    global current_doggo
    current_doggo = doggo_object
    return render_template('pupperPage.html', values ="",description="", sound=sounds[random.randint(0,3)],image_url=doggo_object.url, doggo_message=doggo_object.bork_message())

@app.route('/toptags')
def show_top_tags():
    sorted_top_tags = sorted(top_tags_dict.items(), key=operator.itemgetter(1), reverse=True)

    description = ""

    values = ""

    loop_range = 5
    if len(sorted_top_tags) < 5:
        loop_range = len(sorted_top_tags)

    for i in range(loop_range):
        description = description + sorted_top_tags[i][0] + " " 
        values = values + str(sorted_top_tags[i][1]) + " "

    return render_template('pupperPage.html',values=values, description=description, sound=sounds[random.randint(0,3)],image_url=current_doggo.url, doggo_message=current_doggo.bork_message())

if __name__ == '__main__':
    app.run(debug=True)



