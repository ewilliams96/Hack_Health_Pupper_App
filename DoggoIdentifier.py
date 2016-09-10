from clarifai.client import ClarifaiApi

# test
clarifai_api = ClarifaiApi()
result = clarifai_api.tag_image_urls('http://i.imgur.com/UTlvh4G.jpg')

# get classes of image as identified by ClarifaiApi
classes = result.get('results')[0].get('result').get('tag').get('classes')
print(classes)

