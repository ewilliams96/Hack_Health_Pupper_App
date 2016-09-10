from clarifai.client import ClarifaiApi
from config import clientID, clientSecret

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

clarifai_test()
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
    def call_api():
        if web == True:
            self.result = clarifai_api.tag_image_urls(self.url)
        else:
            self.result = clarifai_api.tag_images(self.url, 'rb')

    # Use clarifai API to verify if an image from a url is actually a dog
    # returns bool
    def verify_dog_from_url():
        classes = self.get_classes()
        for thing in classes:
            if thing == "dog":
                return True
            elif thing == "puppy"
                return True
        return False

    # Get clarifai API classes as list
    def get_classes():
        return self.result.get('results')[0].get('result').get('tag').get('classes')

    # Use results from clarifai API to create more relevant description of image
    def bork_message():
        return None

