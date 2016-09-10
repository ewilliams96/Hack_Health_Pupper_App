from clarifai.client import ClarifaiApi
from config import clientID, clientSecret
import random

clarifai_api = ClarifaiApi(clientID, clientSecret)
# test clarifai-python

def clarifai_test():
    # test
    #clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls('http://i.imgur.com/UTlvh4G.jpg')
    print(result)

    # get classes of image as identified by ClarifaiApi
    classes = result.get('results')[0].get('result').get('tag').get('classes')
    print(classes)


class DoggoAPICall():
    # constructor for class to make API call
    # By default, web = True, so provide an online URL of an image for verification
    # To check a local file, provide path and set web to False.
    # lists (of urls or paths) may also work
    def __init__(self, url, web=True):
        self.url = url
        self.web = web
        self.call_api()
    
    # Call Clarifai API and store results
    def call_api(self):
        if self.web == True:
            self.result = clarifai_api.tag_image_urls(self.url)
        else:
            self.result = clarifai_api.tag_images(self.url, 'rb')

    # Use clarifai API to verify if an image from a url is actually a dog
    # returns bool
    def verify_dog(self):
        for tag in self.get_classes():
            if tag == 'dog':
                return True
            elif tag == 'puppy':
                return True
            elif tag == 'wolf':
                return True
            elif tag == 'canine':
                return True
        return False

    def check_pupper(self):
        for tag in self.get_classes():
            if tag == 'puppy':
                return True
        return False

    # Get clarifai API classes as list
    def get_classes(self):
        return self.result.get('results')[0].get('result').get('tag').get('classes')

    # Use results from clarifai API to create more relevant description of image
    def bork_message(self):
        actions = ['bark', 'bork', 'woof', 'nom', 'noms', 'stretch', 'yawn', 'sleep', 'roll',
        'nuzzle', 'roll', 'lick']
        adverbs = ['comforting', 'suspiciously', 'shy', 'smart', 'mischieveous', 'endearing', 'silly']

        bork_message = 'does a ' + adverbs[random.randint(0,len(adverbs) - 1)] + " " + actions[random.randint(0, len(actions) - 1)] + '!'

        # choose modifier / adjective
        modifier_index = random.randint(0, len(self.get_classes()) - 1)
        dog_modifier = self.get_classes()[modifier_index]
        while dog_modifier == 'puppy' or dog_modifier == 'dog':
            modifier_index = random.randint(0, len(self.get_classes()) - 1)
            dog_modifier = self.get_classes()[modifier_index]
        
        #choose type of dog_modifier
        dog_types = ['pupper', 'puppo', 'woofer', 'doggo', 'dogger']
        if self.check_pupper() == True:
            dog_type = dog_types[0:2][random.randint(0,1)]
        else:
            dog_type = dog_types[random.randint(0, len(dog_types) - 1)]
        
        bork_message = dog_modifier + " " + dog_type + " " + bork_message
        return bork_message

# test driver
def main():
    url = input("Give a url of a picture");
    dac = DoggoAPICall(url)
    print("This image contains: ", dac.get_classes())
    print("Is this image a dog? ", dac.verify_dog())
    print("Is this image a pupper? ", dac.check_pupper())
    print("This image says: ", dac.bork_message())

# test driver
#main()
