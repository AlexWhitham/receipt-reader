# receipt-reader
Read receipts and upload them to Google Sheets.
After setting up credentials run in terminal:
python GCloud/parse_all.py --settings receipt_parser.conf

# based on
    git repo https://github.com/lutzkuen/receipt-parser
    guide https://medium.com/better-programming/google-vision-and-google-sheets-api-line-by-line-receipt-parsing-2e2661261cda

### Example settings file
[settings]  
spreadsheet_id = <'from url of your spreadsheet'>
spreadsheet_range = Sheet!A:L  
oauth_token = ../oauth_client_secret.json  
oauth_pickle = ../token.pickle  
[drive]  
receipts_path = ../Receipts
