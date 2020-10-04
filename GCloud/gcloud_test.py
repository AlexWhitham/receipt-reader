from google.cloud import vision
import io
from pdf2image import convert_from_path
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c:/Users/whith/Google Drive/Receipts/receipts-01102020-9cb15baf0bfd.json'

PATH = 'c:/Users/whith/Google Drive/Receipts/Receipt.pdf'
pages = convert_from_path(PATH, 501)
client = vision.ImageAnnotatorClient()

for page in pages:
    page.save('tmp.jpg')
    with io.open('tmp.jpg', 'rb') as image_file:
        content = image_file.read()
    os.system('del tmp.jpg')
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    print(response.text_annotations[0].description.encode('utf-8'))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))
