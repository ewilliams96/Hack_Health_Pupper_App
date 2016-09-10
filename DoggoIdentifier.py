from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi()
# test clarifai-python
def clarifai_test():
    # test
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls('http://i.imgur.com/UTlvh4G.jpg')
    print(result)

    # get classes of image as identified by ClarifaiApi
    classes = result.get('results')[0].get('result').get('tag').get('classes')
    print(classes)


class DoggoAPICall():
    # constructor for class to make API call
    # By default, web = True, so provide an online URL of an image for verification
    # To check a local file, provide path and set web to False.
    def __init__(self, url, web=True):
        self.url = url
        self.web = web
        self.call_api()
    
    # Call Clarifai API and store results
    def call_api():
        self.results = clarifai_api.tag_image_urls(self.url)

    # Use clarifai API to verify if an image from a url is actually a dog
    def verify_dog_from_url():
        return None
        

    # Use clarifai API to verify if an image from a loca file is actually a dog
    def verify_dog_from_file():
        return None

    # Get clarifai API classes as list
    def get_classes():
        return None:


    # Use results from clarifai API to create more relevant description of image
    def bork_message():
        return None

