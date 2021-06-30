# Read Sainsbury's receipts from Google Docs Scans and upload them to Google Sheets.

# Setup
- Set up credentials and config file
- Install poetry: https://python-poetry.org/docs/
- Run in terminal:
``` poetry run python GCloud/parse_all.py --settings receipt_parser.conf ```

## Note: Before scanning fold receipt from the last item line down to the date (just after barcode) and scan like that (One day I'll remove that bit with code...maybe).

# Example config file

[sheets]

spreadsheet_id = <'from url of your spreadsheet'> 

spreadsheet_range = Sheet1!A:Z

oauth_token = <'path to your token'>.json

oauth_pickle = <'path to your token'>.json

[drive]

receipts_path = <'path to your folder in Google Drive'>

## This receipt scanning tool was build after being inspired by this repo:
git repo https://github.com/lutzkuen/receipt-parser

guide https://medium.com/better-programming/google-vision-and-google-sheets-api-line-by-line-receipt-parsing-2e2661261cda
