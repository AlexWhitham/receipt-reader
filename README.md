# receipt-reader
Read receipts and upload them to Google Sheets.

# based on
    git repo https://github.com/lutzkuen/receipt-parser
    guide https://medium.com/better-programming/google-vision-and-google-sheets-api-line-by-line-receipt-parsing-2e2661261cda

### Example settings file
[settings]  
spreadsheet_id = 1lKnQ1nqVViIDG4Kww_XiDm8U51AWzhb1dA63gyuuAJY  
spreadsheet_range = List!A:L  
oauth_token = ../oauth_client_secret.json  
oauth_pickle = ../token.pickle  
[drive]  
receipts_path = ../drive/Belege