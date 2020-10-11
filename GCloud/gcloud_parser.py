import numpy as np
from google.cloud import vision
from pdf2image import convert_from_path
import datetime
import io
import os
import pickle
import dill

# filtering out entry by having full match to the words in this list
SKIPTHIS = [";SS;",
            ";C;"
            ]

# filtering out entire entry by having partial match to a word from this list
BLACKLIST = ["ORIGINAL PRICE",
             "@",
             "#",
             "live well",
             "well for less",
             "for tess",
             "olborn",
             "$",
             "CANCELLED",
             "BALANCE",
             "REDUCTION",
             "DUPLICATE",
             "RECEIPT",
             "SmartShop",
             "Vat Number",
             "PONTYPRIDD",
             "ashier",
             "THINK 25",
             "ainsbury",
             "Supermarket",
             "660 4548 36",
             "625200",
             "S2274"
             ]


class GcloudParser:
    def __init__(self, debug=False, min_length=4, max_height=1):
        self.debug = debug
        self.min_length = min_length
        self.max_height = max_height
        self.client = vision.ImageAnnotatorClient()
        self.allowed_labels = ["item", "price", "shop", "date"]

    def parse_date(self, date_from_list):
        date_from_list = list(str(date_from_list).split(" "))
        date_str = str(date_from_list[1]).replace("']", "")
        for fmt in ["%d.%m.%y", "%Y-%m-%d", "%d.%m.%y %H:%M", "%d.%m.%Y", "%d%b%Y"]:
            for substr in date_str.split(" "):
                try:
                    new_purch_date = datetime.datetime.strptime(
                        substr, fmt).strftime("%d/%m/%Y")
                    return new_purch_date
                except Exception as e:
                    pass
        return None

    def parse_pdf(self, path):
        pages = convert_from_path(path, 500)
        item_no = []
        articles = {}
        items = []
        prices = []
        date = []
        shop = []
        for page in pages:
            page.save("tmp.jpg")
            gcloud_response = self.detect_text("tmp.jpg")
            os.system("del tmp.jpg")
            gcloud_response = gcloud_response.replace("\n", ";")
            # print(gcloud_response)
            # break
            for skipword in SKIPTHIS:
                gcloud_response = gcloud_response.replace(skipword, ";")

            response_list = list(gcloud_response.split(";"))
            response_list = list(filter(None, response_list))
            response_list = [word for word in response_list if not any(
                bad in word for bad in BLACKLIST)]

            while len(response_list[-1]) != 3:
                response_list = response_list[:-1]
            if len(response_list[-1]) == 3:
                response_list = response_list[:-1]
            if response_list[-2].startswith("S"):
                del response_list[-2]

            amount_items = int(len(response_list[0:-1])/2)

            item_no = list(range(0, amount_items))
            items += response_list[0:amount_items]
            prices += response_list[amount_items:-1]
            prices = [p.replace(",", ".") for p in prices]

            articles = dict(zip(item_no, items))
            full_price = dict(zip(item_no, prices))
            for n in item_no:
                articles[n] = [articles[n], full_price[n]]
            # print(articles)
            try:
                date = self.parse_date(response_list[-1:])
            except Exception as e:
                pass

            shop = "Sainsburys"  # response_list[0]
        return articles, date, shop

    def detect_text(self, path):
        """Detects text in the file."""
        with io.open(path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(
                    response.error.message))
        return response.text_annotations[0].description
