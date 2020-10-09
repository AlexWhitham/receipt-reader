import numpy as np
from google.cloud import vision
from pdf2image import convert_from_path
import datetime
import io
import os
import pickle
import dill

SKIPTHIS = ["'",
            ";Cive well for less;SS;PONTYPRIDD;01443 625200;Sainsburys Supermarkets Ltd;33 Holborn London EC1N 2HT;www.sainsburys.co.uk;Vat Number : 660 4548 36;SmartShop",
            "#7452;$2274;",
            ";16 BALANCE DUE",
            "R67;"]


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
                        substr, fmt).strftime("%d%m%Y")
                    return new_purch_date
                except Exception as e:
                    pass
        return None

    def parse_pdf(self, path):
        pages = convert_from_path(path, 500)
        items = []
        prices = []
        date = []
        shop = []
        for page in pages:
            pkl_name = path.replace(".pdf", ".pkl")
            page.save("tmp.jpg")
            gcloud_response = self.detect_text("tmp.jpg")
            os.system("del tmp.jpg")
            gcloud_response = gcloud_response.replace("\n", ";")
            for skipword in SKIPTHIS:
                gcloud_response = gcloud_response.replace(skipword, "")
            response_list = list(gcloud_response.split(";"))
            response_list = list(filter(None, response_list))

            amount_items = int(len(response_list[1:-2])/2)
            items += response_list[1:amount_items]
            prices += response_list[amount_items:-1]

            date = self.parse_date(response_list[-1:])

            shop = response_list[0]
        return items, prices, date, shop

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
