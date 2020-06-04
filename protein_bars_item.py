import re

import scrapy
from scrapy.loader.processors import Compose, Join


def remove_duplicates(in_list):
    already_seen = set()
    ret_list = []
    for elem in in_list:
        if not elem in already_seen:
            ret_list.append(elem)
        already_seen.add(elem)
    return ret_list


def strip_strings(in_list):
    return [re.sub('\s+', ' ', s).strip() for s in in_list]


def remove_emptys(in_list):
    return filter(len, filter(None, in_list))


def remove_break(input):
    return str(input).replace('<br>', ',')


class Remove(object):
    def __init__(self, removal_string):
        self.removal_string = removal_string

    def __call__(self, value):
        if len(value) == 0: return value
        return value.replace(self.removal_string, "").strip()


DEFAULT = scrapy.Field(
    output_processor=Compose(
        strip_strings, remove_emptys, remove_duplicates, Join(' ')),
)


class ProteinBarsItem(scrapy.Item):
    src = DEFAULT
    product_id = DEFAULT
    name = scrapy.Field(
        output_processor=Compose(
            strip_strings, remove_emptys, remove_duplicates, Join(' - ')),
    )
    brand = DEFAULT
    description = DEFAULT
    sku = DEFAULT
    barcode = DEFAULT
    available = DEFAULT
    price = DEFAULT
    tags = scrapy.Field(
        output_processor=Compose(
            strip_strings, remove_emptys, remove_duplicates, Join(', ')),
    )
    vendor = DEFAULT
    images = DEFAULT
    nutrition_facts_image_url = DEFAULT
    ingredients = DEFAULT
    serving_size = DEFAULT
    amount_per_serving = DEFAULT
    calories = DEFAULT
    calories_from_fat = DEFAULT
    total_fat = DEFAULT
    total_fat_percentage = DEFAULT
    saturated_fat = DEFAULT
    saturated_fat_percentage = DEFAULT
    trans_fat = DEFAULT
    trans_fat_percentage = DEFAULT
    cholesterol = DEFAULT
    cholesterol_percentage = DEFAULT
    sodium = DEFAULT
    sodium_percentage = DEFAULT
    potassium = DEFAULT
    potassium_percentage = DEFAULT
    total_carbohydrate = DEFAULT
    total_carbohydrate_percentage = DEFAULT
    dietary_fiber = DEFAULT
    dietary_fiber_percentage = DEFAULT
    sugars = DEFAULT
    protein = DEFAULT
    protein_percentage = DEFAULT
    vitamin_a = DEFAULT
    vitamin_c = DEFAULT
    calcium = DEFAULT
    iron = DEFAULT
    thiamin = DEFAULT
    riboflavin = DEFAULT
    niacin = DEFAULT
    vitamin_b6 = DEFAULT
    vitamin_b12 = DEFAULT
    phosphorus = DEFAULT
    magnesium = DEFAULT
    manganese = DEFAULT
    polydextrose = DEFAULT
    sorbitol = DEFAULT
    maltitol = DEFAULT
    glycerol = DEFAULT
    shipping_info = DEFAULT