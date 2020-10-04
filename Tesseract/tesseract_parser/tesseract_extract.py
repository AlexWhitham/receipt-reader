import pytesseract as pts
from pdf2image import convert_from_path

PATH = "c:/Users/whith/Google Drive/Receipts/Receipt.pdf"
pages = convert_from_path(PATH, 501)
for page in pages:
    test_str = pts.image_to_data(page, lang='eng', config='--psm 6')
    current_linenum = 0
    current_line = ''
    for _line in test_str.split('\n')[1:]:
        line = _line.split('\t')
        if line[4] == current_linenum:
            current_line += line[-1] + ' '
        else:
            print(current_line)
            current_linenum = line[4]
            current_line = line[-1]
    print(current_line)
