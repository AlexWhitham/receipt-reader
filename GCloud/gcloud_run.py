from gcloud_parser import GcloudParser
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c:/Users/whith/Documents/Google_receipts/receipts-svc-acc.json'

PATH = 'c:/Users/whith/Google Drive/Receipts/Receipt.pdf'

parser = GcloudParser(debug=True)

articles, dates, markets = parser.parse_pdf(PATH)
print(articles)
print(markets)
