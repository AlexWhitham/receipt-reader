from gcloud_parser.gcloud_parser import GcloudParser
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c:/Users/whith/Google Drive/Receipts/receipts-01102020-9cb15baf0bfd.json'

PATH = 'c:/Users/whith/Google Drive/Receipts/Receipt.pdf'

parser = GcloudParser(debug=True)

articles, dates, markets = parser.parse_pdf(PATH)
print(articles)
print(markets)
