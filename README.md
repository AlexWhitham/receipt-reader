# Read Sainsbury's receipts from Google Docs Scans and upload them to Google Sheets.

# Setup
- Set up credentials and config file
- Install poetry: https://python-poetry.org/docs/
- Install chocolatey https://chocolatey.org/install
- Then install poppler using choco: choco install poppler
```
from pdf2image import convert_from_path
images = convert_from_path("mypdf.pdf", 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
```
- Run in terminal:
``` poetry run python GCloud/parse_all.py --settings receipt_parser.conf ```

## Note: 
- Before scanning fold receipt from the last item line down to the date (just after barcode) and scan like that (One day I'll remove that bit with code...maybe)
- You might need to adjust the BLACKLIST
- Keep an eye on the numbers. Mostly the tool runns like a charm, but sometimes hiccups and mix things up. Double check numbers are alligning with the receipt total 

## Example config file

```
[sheets]
spreadsheet_id = <'from url of your spreadsheet'> 
spreadsheet_range = Sheet1!A:Z
oauth_token = <'path to your token'>.json
oauth_pickle = <'path to your token'>.json

[drive]
receipts_path = <'path to your folder in Google Drive'>
```

## This receipt scanning tool was build after being inspired by following
- Git repo https://github.com/lutzkuen/receipt-parser

- Guide https://medium.com/better-programming/google-vision-and-google-sheets-api-line-by-line-receipt-parsing-2e2661261cda
