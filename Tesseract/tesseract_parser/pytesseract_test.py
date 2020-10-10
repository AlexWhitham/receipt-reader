import pytesseract as pts
from PIL import Image
from pdf2image import convert_from_path
import enchant
# from invoice2data import extract_data
from tesseract_parser import tesseract_parser as tp

# def is_number(in_str):
#     try:
#         _ = float(in_str)
#         return True
#     except Exception as e:
#         return False
#
# def is_decimal(i_num):
#     if round(i_num) != i_num:
#         return True
#     else:
#         return False
#


PATH = 'c:/Users/whith/Google Drive/Receipts/Receipt.pdf'

parser = tp.TesseractParser(debug=True, iterations=3)

print(parser.parse_pdf(PATH, save_crop=True))
