# -*- coding: utf-8 -*-
import json

import bs4 as bs4
import requests
import scrapy
from scrapy import Request, FormRequest, Selector
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider
import math


class ProfileSpider(CrawlSpider):
    name = 'julian'
    urls = [
        "https://www.nugonutrition.com/collections/products",
        "https://www.questnutrition.com/collections/protein-bars",
        "https://www.detourbar.com/collections/all",
        "https://www.nashuanutrition.com/collections/best-protein-bars",
        "https://protifoods.com/all-protein-products/protein-bars/",
        "https://shop.metrx.com/Protein-Bars-and-Snacks/c/METRx@ProteinBars",
        "https://maximsportvoeding.nl/maxim_en/producten-en/protein-bars",
        "https://slim4life.com/product-category/all-supplements/snack-bars/",
        "https://shop.thinkproducts.com/Protein-Bars/c/ThinkProducts@Bars",
        "https://store.shopqwlc.com/collections/all-products/bars#MainContent",
        "https://www.bodylab.dk/shop/proteinbarer-12c1.html",
        "https://aussiebodies.com.au/products/all/?c=bar",
        "https://zoneperfect.com/products/macros",
        "https://zoneperfect.com/products/classics-bars",
        "https://www.grenade.com/us/grenade-carb-killa/",
        "https://julianbakery.com/shop/?fwp_categories=protein-bar&fwp_load_more=5"
    ]

    # def __init__(self, url="https://www.nugonutrition.com/collections/products", *args, **kwargs):
    # def __init__(self, url="https://www.questnutrition.com/collections/protein-bars", *args, **kwargs):
    # def __init__(self, url="https://www.detourbar.com/collections/all", *args, **kwargs):
    # def __init__(self, url="https://www.nashuanutrition.com/collections/best-protein-bars", *args, **kwargs):
    # def __init__(self, url="https://protifoods.com/all-protein-products/protein-bars/", *args, **kwargs):
    # def __init__(self, url="https://aussiebodies.com.au/wp-admin/admin-ajax.php", *args, **kwargs):
    # def __init__(self, url="https://shop.metrx.com/Protein-Bars-and-Snacks/c/METRx@ProteinBars", *args, **kwargs):
    # def __init__(self, url="https://maximsportvoeding.nl/maxim_en/producten-en/protein-bars", *args, **kwargs):
    # def __init__(self, url="https://slim4life.com/product-category/all-supplements/snack-bars/", *args, **kwargs):
    # def __init__(self, url="https://shop.thinkproducts.com/Protein-Bars/c/ThinkProducts@Bars", *args, **kwargs):
    # def __init__(self, url="https://store.shopqwlc.com/collections/all-products/bars#MainContent", *args, **kwargs):
    # def __init__(self, url="https://www.bodylab.dk/shop/proteinbarer-12c1.html", *args, **kwargs):
    def __init__(self, *args, **kwargs):
        super(ProfileSpider, self).__init__(*args, **kwargs)
        self.url = self.urls[-1]


    # def start_requests(self):
    #     lists = []
    #
    #     for url in self.urls:
    #         if "detour" in url:
    #             lists.append(Request(url, callback=self.parse_items_detour))
    #         elif "questnutrition" in url:
    #             lists.append(Request(url, callback=self.parse_items_quest))
    #         elif "nugonutrition" in url:
    #             lists.append(Request(url, callback=self.parse_items_nugo))
    #         elif "nashuanutrition" in url:
    #             lists.append(Request(url, callback=self.parse_items_nashua))
    #         elif "protifoods" in url:
    #             lists.append(Request(url, callback=self.parse_items_proti))
    #         elif "metrx" in url:
    #             lists.append(Request(url, callback=self.parse_items_metrx))
    #         elif "promaxnutrition" in url:
    #             lists.append(Request(url, callback=self.parse_items_promax))
    #         elif "maximsportvoeding" in url:
    #             lists.append(Request(url, callback=self.parse_items_maxim))
    #         elif "slim4life" in url:
    #             lists.append(Request(url, callback=self.parse_items_slim4life))
    #         elif "thinkproducts" in url:
    #             lists.append(Request(url, callback=self.parse_items_thinkthin))
    #         elif "shopqwlc" in url:
    #             lists.append(Request(url, callback=self.parse_items_wlc))
    #         elif "bodylab" in url:
    #             lists.append(Request(url, callback=self.parse_items_bodylab))
    #         elif "aussiebodies" in self.url:
    #             lists.append(Request(self.url, callback=self.parse_items_aussiebodies))
    #     return lists

    def start_requests(self):
        lists = []
        if not self.url:
            return None

        if "detour" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_detour))
        elif "questnutrition" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_quest))
        elif "nugonutrition" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_nugo))
        elif "nashuanutrition" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_nashua))
        elif "protifoods" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_proti))
        elif "metrx" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_metrx))
        elif "promaxnutrition" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_promax))
        elif "maximsportvoeding" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_maxim))
        elif "slim4life" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_slim4life))
        elif "thinkproducts" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_thinkthin))
        elif "shopqwlc" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_wlc))
        elif "bodylab" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_bodylab))
        elif "aussiebodies" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_aussiebodies))
        elif "zoneperfect" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_zoneperfect))
        elif "grenade" in self.url:
            lists.append(Request(self.url, callback=self.parse_items_grenade))
        elif "julianbakery" in self.url:
            lists.append(FormRequest(self.url, callback=self.parse_julian_bakery))

        return lists

    def parse_julian_bakery(self, response):
        lists = []
        products = response.xpath('/html/body/main/section/div/div[2]/div[2]/div[1]/div[2]/div/div/a/@href').extract()
        for product_url in products:
            lists.append(
                Request(product_url, callback=self.jullian_bakery)
            )

        return lists

    def jullian_bakery(self, response):
        lists = []
        item = ItemLoader(ProteinBarsItem(), response)
        price = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[2]/div/div/p/span/text()').get()
        currency = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[2]/div/div/p/span/span/text()').get()


        item.add_xpath('name', '//*[@id="product-508"]/section[1]/div/div/div[1]/h1/text()')
        item.add_value('price', f"{currency}{price}")
        item.add_xpath('description', '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[2]/p/text()')
        item.add_xpath('protein', '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[2]/div[2]/div/span[1]')
        item.add_xpath("images", '//meta[@property="og:image"]/@content')
        item.add_value("available", 'yes')
        item.add_value("brand", 'Julian Bakery')
        item.add_value("brand", 'Julian Bakery')

        calcium = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[17]/span[1]/text()').get()
        calories = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[4]/span[2]/text()').get()
        cholesterol = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[9]/span[1]/text()').get()
        cholesterol_percentage = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[9]/span[2]/text()').get()
        dietary_fiber = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[12]/span[1]/text()').get()
        dietary_fiber_percentage = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[12]/span[2]/text()').get()
        iron = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[18]/span[1]/text()').get()
        potassium = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[19]/span[1]/text()').get()
        potassium_percentage = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[19]/span[2]/text()').get()
        saturated_fat = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[7]/span[1]/text()').get()
        saturated_fat_percentage = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[7]/span[2]/text()').get()
        serving_size = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[2]/text()').get()
        sodium = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[10]/span[1]/text()').get()
        total_sugars = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[13]/span/text()').get()
        total_carbohydrate = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[11]/span[1]/text()').get()
        total_fat = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[6]/span[1]/text()').get()
        trans_fat = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[8]/span/text()').get()

        if calcium is not None:
            item.add_value("calcium", calcium.split(' ')[1])
        item.add_value("calories", calories)
        item.add_value("cholesterol", cholesterol)
        if cholesterol_percentage is not None:
            item.add_value("cholesterol_percentage", cholesterol_percentage.replace('%', ''))
        if dietary_fiber is not None:
            item.add_value("dietary_fiber", dietary_fiber.split(' ')[2])
        if dietary_fiber_percentage is not None:
            item.add_value("dietary_fiber_percentage", dietary_fiber_percentage.replace('%', ''))
        item.add_xpath('ingredients', '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/p[1]/text()')
        if iron is not None:
            try:
                item.add_value('iron', iron.split(' ')[1])
            except:
                print('iron error')
                print(iron)
        if potassium and potassium_percentage is not None:
            try:
                item.add_value('potassium', potassium.split(' ')[1])
                item.add_value('potassium_percentage', potassium_percentage.replace('%', ''))

            except:
                print('potassium error')
                print(potassium)
                print(potassium_percentage)
        if saturated_fat and saturated_fat_percentage is not None:
            item.add_value('saturated_fat', saturated_fat.split(' ')[2])
            item.add_value('saturated_fat_percentage', saturated_fat_percentage.replace('%', ''))
        if serving_size is not None:
            item.add_value('serving_size', " ".join(serving_size.split(' ')[3:-1]))
        if sodium is not None:
            item.add_value('sodium', sodium.replace(' ', ''))
        item.add_xpath('sodium', '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[10]/span[2]/text()')
        item.add_value('src', response.url)
        if total_sugars is not None:
            item.add_value('sugars', total_sugars.split(' ')[2])
        if total_carbohydrate is not None:
            item.add_value('total_carbohydrate', total_carbohydrate.replace(' ', ''))
        item.add_xpath('total_carbohydrate_percentage', '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[11]/span[2]/text()')
        if total_fat is not None:
            item.add_value('total_fat', total_fat.replace(' ', ''))
        item.add_xpath('total_fat_percentage', '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[6]/span[2]/text()')
        if trans_fat is not None:
            item.add_value('trans_fat', trans_fat.split(' ')[2])
        item.add_value('vendor', 'Julian Bakery')
        lists.append(item.load_item())
        return lists

    def parse_items_grenade(self, response):
        lists = []
        base_url = 'https://www.grenade.com/us/grenade-carb-killa/'
        categories = [
            'birthday-cake',
            'caramel-chaos',
            'chocolate-chip-cookie-dough',
            'chocolate-cream',
            'dark-chocolate-raspberry',
            'gingerbread',
            'peanut-nutter',
            'salted-caramel',
            'white-chocolate-cookie',
            'white-chocolate-salted-peanut',
        ]
        for category in categories:
            lists.append(
                Request(f"{base_url}{category}", callback=self.grenade)
            )
        return lists

    def grenade(self, response):
        lists = []
        item = ItemLoader(ProteinBarsItem(), response)
        amount_per_serving = response.xpath(
            '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[1]/th[2]/text()').get()
        item.add_value("amount_per_serving", amount_per_serving[amount_per_serving.find("(")+1:amount_per_serving.find(")")])
        item.add_value("brand", 'Carb Killa')
        item.add_value("vendor", 'Grenade')
        item.add_value("available", 'yes')
        item.add_value('src', response.url)
        item.add_xpath("images", '//meta[@property="og:image"]/@content')

        item.add_xpath('name', '//*[@id="maincontent"]/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/h1/text()')
        item.add_xpath('calories', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[2]/td[2]/text()')
        item.add_xpath('cholesterol', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[6]/td[2]/text()')
        item.add_xpath('cholesterol_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[6]/td[3]/text()')
        item.add_xpath('description', '//*[@id="maincontent"]/div[2]/div/div[4]/div[2]/div[1]/div[3]/div/p[1]/text()')
        item.add_xpath('dietary_fiber', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[10]/td[2]/text()')
        item.add_xpath('dietary_fiber_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[10]/td[3]/text()')
        item.add_xpath('ingredients', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[1]/div/div/p[1]/text()')
        item.add_xpath('potassium', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[8]/td[2]/text()')
        item.add_xpath('potassium_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[8]/td[3]/text()')
        item.add_xpath('price', '//*[@id="maincontent"]/div[2]/div/div[4]/div[2]/div[1]/div[2]/div/span/text()')
        item.add_xpath('protein', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[14]/td[2]/text()')
        item.add_xpath('protein_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[14]/td[3]/text()')
        item.add_xpath('saturated_fat', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[4]/td[2]/text()')
        item.add_xpath('saturated_fat_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[4]/td[3]/text()')
        item.add_xpath('sodium', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[7]/td[2]/text()')
        item.add_xpath('sodium_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[7]/td[3]/text()')
        item.add_xpath('sugars', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[11]/td[2]/text()')
        item.add_xpath('total_carbohydrate', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[9]/td[2]/text()')
        item.add_xpath('total_carbohydrate_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[9]/td[3]/text()')
        item.add_xpath('total_fat', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[3]/td[2]/text()')
        item.add_xpath('total_fat_percentage', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[3]/td[3]/text()')
        item.add_xpath('trans_fat', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[5]/td[3]/text()')
        lists.append(item.load_item())

        return lists

    def parse_items_zoneperfect(self, response):
        lists = []
        base_url = 'https://zoneperfect.com/'
        for url in response.xpath('//div[@class="PCP-ProductItem__text"]/a/@href').extract():
            lists.append(
                Request(f"{base_url}{url}", callback=self.zoneperfect)
            )
        return lists

    def zoneperfect(self, response):
        lists = []
        variants = response.xpath(
            '//div[6]/select[@class="PDP-Hero__select"]/option/text()'
        ).getall()

        for variant in variants:
            item = ItemLoader(ProteinBarsItem(), response)
            product_title = response.xpath('//div[@class="PCP-ProductItem__title"]/text()').get()
            product_sub_title = response.xpath('//div[@class="PCP-ProductItem__subtitle"]/text()').get()
            name = f"{product_title} {product_sub_title} - {variant}"
            item.add_value("name", name)
            item.add_value("available", 'yes')
            item.add_xpath("brand", '//div[@class="PDP-Hero__title"]/h1/text()')
            item.add_xpath("description", "//div[@class=\"PDP-Hero__text\"]/p/text()")

            table_rows = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()
            for index in range(len(table_rows)):
                if "Calories:" in table_rows[index]:
                    item.add_value("calories", str(table_rows[index]).split(": ")[1])

                if "Calories from" in table_rows[index]:
                    item.add_value("calories_from_fat", str(table_rows[index]).split(": ")[1])

                if "Calcium:" in table_rows[index]:
                    calcium = \
                    response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("calcium", calcium)

                if "Cholesterol, mg:" in table_rows[index]:
                    cholesterol = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[(index + 1)]
                    item.add_value("cholesterol", cholesterol)

                if "Dietary Fiber," in table_rows[index]:
                    dietary_fibr = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[(index + 1)]
                    item.add_value("dietary_fiber", dietary_fibr)

                if "Iron:" in table_rows[index]:
                    item.add_value("iron", str(table_rows[index]).split(":")[1])

                if "Magnesium:" in table_rows[index]:
                    item.add_value("magnesium", str(table_rows[index]).split(":")[1])

                if "Niacin:" in table_rows[index]:
                    item.add_value("niacin", str(table_rows[index]).split(":")[1])

                if "Phosphorus:" in table_rows[index]:
                    item.add_value("phosphorus", str(table_rows[index]).split(":")[1])

                if "Potassium," in table_rows[index]:
                    potassium = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[(index + 1)]
                    item.add_value("potassium", potassium)

                if "Protein, " in table_rows[index]:
                    protein = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[(index + 1)]
                    item.add_value("protein", protein)

                if "Riboflavin:" in table_rows[index]:
                    item.add_value("riboflavin", str(table_rows[index]).split(":")[1])

                if "Saturated Fat," in table_rows[index]:
                    sfat = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("saturated_fat", sfat)

                if "Sodium," in table_rows[index]:
                    sodium = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("sodium", sodium)

                if "Sodium," in table_rows[index]:
                    sodium = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("sodium", sodium)

                if "Thiamin:" in table_rows[index]:
                    item.add_value("thiamin", str(table_rows[index]).split(":")[1])

                if "Total Carbohydrate," in table_rows[index]:
                    total_carb = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("total_carbohydrate", total_carb)

                if "Total Fat," in table_rows[index]:
                    total_fat = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[(index + 1)]
                    item.add_value("total_fat", total_fat)

                if "Vitamin A:" in table_rows[index]:
                    vitamin_a = \
                    response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("vitamin_a", vitamin_a)

                if "Vitamin B12:" in table_rows[index]:
                    vitamin_b12 = response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("vitamin_b12", vitamin_b12)

                if "Vitamin B6:" in table_rows[index]:
                    vitamin_b6 = \
                    response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                        (index + 1)]
                    item.add_value("vitamin_b6", vitamin_b6)

                if "Vitamin C:" in table_rows[index]:
                    vitamin_c = \
                        response.xpath('//div[2]/div[1][@class="PDP-Info__pimContent"]//tr//td/text()').getall()[
                            (index + 1)]
                    item.add_value("vitamin_c", vitamin_c)

            item.add_xpath("images", '//meta[@property="og:image"]/@content')
            item.add_xpath("description", '//div[@class="PDP-Info__col PDP-Info__col--ingredients"]//p[2]/text()')
            lists.append(item.load_item())

        return lists

    def parse_items_aussiebodies(self, response):
        lists = []
        for url in response.xpath('//a[@class="view-product"]/@href').extract():
            lists.append(
                Request(url, callback=self.aussiebodies)
            )
        return lists

    def aussiebodies(self, response):
        lists = []
        body = {
            "action": response.xpath("//form[@id='sizeform']//input[@name='action']/@value").get(),
            "productid": response.xpath("//form[@id='sizeform']//input[@name='productid']/@value").get(),
            "producttitle": response.xpath("//form[@id='sizeform']//input[@name='producttitle']/@value").get(),
            "flavour": response.xpath("//form[@id='sizeform']//input[@name='flavour']/@value").get(),
        }

        data = {
            'name': body['producttitle'],
            'url': response.url
        }

        for size in response.xpath("//form[@id='sizeform']//input[@name='size[]']/@value").extract():
            body['size[]'] = size
            lists.append(
                FormRequest("https://aussiebodies.com.au/wp-admin/admin-ajax.php", formdata=body,
                        method='POST', meta=data, dont_filter=True, callback=self.parse_aussiebodies_flavours)
            )
        return lists

    def parse_aussiebodies_flavours(self, response):
        lists = []
        data = json.loads(response.body)

        for flavour in data:
            nutri = Selector(text=flavour['nutri'])
            item = ItemLoader(ProteinBarsItem(), nutri)

            item.add_value('src', response.meta['url'])
            item.add_value('name', f"{response.meta['name']} - {flavour['flavour']}")
            item.add_value('brand', "Aussie Bodies")
            item.add_value('description', bs4.BeautifulSoup(flavour['desc'], features="lxml").get_text())
            item.add_value('tags', str(flavour['feat']).replace('|', ', '))
            item.add_value('product_id', str(flavour['id']))
            item.add_value('images', flavour['image'])


            serving_size = nutri.xpath("//td[contains(text(), 'Servings per package:')]/text()").get()
            if serving_size:
                item.add_value('serving_size', str(serving_size).replace('Servings per package: ', ''))

            item.add_xpath('protein', "//td[contains(text(), 'Protein, Total')]/following-sibling::td[1]/text()")
            item.add_xpath('total_fat', "//td[contains(text(), 'Fat, Total')]/following-sibling::td[1]/text()")
            item.add_xpath('saturated_fat', "//td[contains(text(), 'Saturated')]/following-sibling::td[1]/text()")
            item.add_xpath('total_carbohydrate', "//td[contains(text(), 'Carbohydrate')]/following-sibling::td[1]/text()")
            item.add_xpath('sugars', "//td[contains(text(), 'Sugars')]/following-sibling::td[1]/text()")
            item.add_xpath('dietary_fiber', "//td[contains(text(), 'Dietary Fibre, Total')]/following-sibling::td[1]/text()")
            item.add_xpath('polydextrose', "//td[contains(text(), 'Polydextrose')]/following-sibling::td[1]/text()")
            item.add_xpath('sodium', "//td[contains(text(), 'Sodium')]/following-sibling::td[1]/text()")
            item.add_xpath('sorbitol', "//td[contains(text(), 'Sorbitol')]/following-sibling::td[1]/text()")
            item.add_xpath('maltitol', "//td[contains(text(), 'Maltitol')]/following-sibling::td[1]/text()")
            item.add_xpath('glycerol', "//td[contains(text(), 'Glycerol')]/following-sibling::td[1]/text()")

            lists.append(item.load_item())

        return lists


    def parse_items_bodylab(self, response):
        lists = []
        base_url = 'https://www.bodylab.dk'
        for url in response.xpath('//*[@class="plImg"]/a/@href').extract():
            lists.append(
                Request(f"{base_url}{url}", callback=self.bodylab)
            )
        return lists

    def bodylab(self, response):
        stock_str = response.xpath('//div[@class="inStockIndicator"]/img/@src').get()
        protein_array = response.xpath('//div[@class="Description_Productinfo"]/ul/li/text()').getall()

        protein = ''
        for pro in protein_array:
            if "protein" in pro:
                protein = pro

        item = ItemLoader(ProteinBarsItem(), response)

        item.add_value("src", response.url)
        item.add_xpath("name", '//meta[@property="og:title"]/@content')
        item.add_value("brand", 'Bodylab')
        item.add_value("available", "yes " if 'iconInStockCheckmark.svg' in stock_str else "no")
        item.add_xpath("images", '//meta[@property="og:image"]/@content')
        item.add_xpath("sku", '//span[@itemprop="productid"]/text()')
        item.add_xpath("description", '//div[@id="description"]//text()')
        item.add_xpath("price", '//span[@itemprop="price"]/@content')
        item.add_value("protein", protein.replace(' protein', ''))
        return item.load_item()

    def parse_items_wlc(self, response):
        lists = []
        base_url = "https://store.shopqwlc.com"

        for url in list(set(response.xpath("//div[@class='grid-view-item product-card']/a/@href").extract())):
            lists.append(
                Request(f"{base_url}{url}", callback=self.wlc)
            )
        return lists

    def wlc(self, response):
        lists = []
        json_data = requests.get(f"{response.url}.js").json()

        for index, data in enumerate(json_data['variants']):
            item = ItemLoader(ProteinBarsItem(), response)

            item.add_value("src", response.url)
            item.add_value("product_id", str(data['id']))
            item.add_value("name", data['name'])
            item.add_value("brand", "Quick Weight Loss Center")

            description = bs4.BeautifulSoup(json_data['description'], features="lxml")
            item.add_value("description", description.get_text())
            item.add_value("sku", data['sku'])
            item.add_value("barcode", data['barcode'])
            item.add_value("available", "yes" if data['available'] else "no")
            item.add_value("price", str(data['price']/100))
            item.add_value("tags", ', '.join(json_data['tags']))
            item.add_value("vendor", json_data['vendor'])
            item.add_value("images", " , ".join(json_data['images']))

            item.add_xpath("nutrition_facts_image_url", "//div[@class='thumbnails-wrapper']//li[last()]/a/@href")
            lists.append(item.load_item())
        return lists

    def parse_items_thinkthin(self, response):
        lists = []
        base_url = "https://shop.thinkproducts.com"

        for url in response.xpath("//div[@class='item_detail']/a/@href").extract():
            lists.append(
                Request(base_url+url, callback=self.thinkthin)
            )

        return lists

    def thinkthin(self, response):
        lists = []
        base_url = "https://shop.thinkproducts.com"

        name = response.xpath("//div[@class='prod_car']//img[@itemprop='image']/@alt").extract_first()
        images = response.xpath("//meta[@property='og:image']/@content").get()
        description = response.xpath("//meta[@property='og:description']/@content").get()
        tags = ', '.join(response.xpath("//div[@id='product_designations']//li/text()").extract())
        nutrition_url = response.xpath("//div[@id='product_nutrition']/img/@src").get()
        ingredients =response.xpath("//span[@itemprop='description']//text()").get()

        for res in response.xpath("//div[@id='REG-groups']//li[@class='variant_pricing']"):
            item = ItemLoader(ProteinBarsItem(), res)

            size = res.xpath(".//div[@class='line-one']/text()").get()

            item.add_value("src", response.url)
            item.add_value("name", f"{name} - {size}")
            item.add_value("description", description)
            item.add_value("brand", "ThinkThin")
            item.add_xpath("price", ".//div[@class='line-two']/text()")
            item.add_value("images", images)
            item.add_value("tags", tags)

            if nutrition_url:
                item.add_value("nutrition_facts_image_url", f"{base_url}{nutrition_url}")
            item.add_value("ingredients", ingredients)

            lists.append(item.load_item())

        return lists

    def parse_items_slim4life(self, response):
        lists = []

        for url in response.xpath("//*[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']/@href").extract():
            lists.append(
                Request(url, callback=self.slim4life)
            )

        next_page = response.xpath("//*[@class='next page-numbers']/@href").extract_first()
        if next_page:
            lists.append(
                Request(next_page, callback=self.parse_items_slim4life)
            )

        return lists

    def slim4life(self, response):
        item = ItemLoader(ProteinBarsItem(), response)

        item.add_value('src', response.url)
        item.add_value('brand', "Slim 4 Life")
        item.add_xpath('name', "//h1[@class='product_title entry-title']/text()")
        item.add_xpath('price', "//span[@class='woocommerce-Price-amount amount']/text()")
        item.add_xpath('sku', "//span[@class='sku']/text()")
        item.add_xpath('images', "//meta[@property='og:image']/@content")
        item.add_xpath('tags', "//span[@class='posted_in']//a/text()")
        item.add_xpath('description', "//h2[text()='Description']/following-sibling::p[1]//text()")

        return item.load_item()

    def parse_items_maxim(self, response):
        lists = []

        for url in response.xpath("//*[@class='product-image-change']/a/@href").extract():
            lists.append(
                Request(url, callback=self.maxim)
            )

        next_page = response.xpath("//*[@class='action  next']/@href").extract_first()
        if next_page:
            lists.append(
                Request(next_page, callback=self.parse_items_maxim)
            )

        return lists

    def maxim(self, response):
        item = ItemLoader(ProteinBarsItem(), response)

        item.add_value('src', response.url)
        item.add_value('brand', "Maxim")
        item.add_xpath('name', "//h1[@class='page-title']/text()")
        item.add_xpath('price', "//span[@itemprop='price']/@data-price-amount")
        item.add_xpath('sku', "//div[@itemprop='sku']/text()")
        item.add_xpath('images', "//meta[@property='og:image']/@content")
        item.add_xpath('description', "//div[@class='product attribute description']//text()")
        item.add_xpath('description', "//td[@data-th='Voedingswaarde']//text()")
        item.add_xpath('ingredients', "//td[@data-th='Ingrediënten']//text()")

        return item.load_item()

    def parse_items_promax(self, response):
        lists = []
        base_url = "https://store.promaxnutrition.com"

        for url in response.xpath("//*[@class='product-title']/a/@href").extract():
            lists.append(
                Request(base_url+url, callback=self.promax)
            )

        return lists

    def promax(self, response):
        item = ItemLoader(ProteinBarsItem(), response)

        item.add_value("src", response.url)
        item.add_value("brand", "Promax")
        item.add_xpath("name", "//meta[@property='og:title']/@content")
        item.add_xpath("images", "//meta[@property='og:image']/@content")
        item.add_xpath("description", "//div[@class='short-description']/text()")
        item.add_xpath("sku", "//span[@itemprop='sku']/text()")
        item.add_xpath("calories", "//strong[text()='Calories']/../../td[2]//text()")
        item.add_xpath("calories_from_fat", "//*[text()='Calories from fat']/../../td[2]//text()")
        item.add_xpath("tags", "//ul[@class='checkmarks']//li/text()")

        total_fat = response.xpath("//*[contains(text(), 'Total Fat')]//text()").get()
        if total_fat:
            if len(response.xpath("//*[contains(text(), 'Total Fat')]/..//td")) > 2:
                item.add_xpath("total_fat", "//*[contains(text(), 'Total Fat')]/../td[2]//text()")
                item.add_xpath("total_fat_percentage", "//*[contains(text(), 'Total Fat')]/../td[3]//text()")
            else:
                item.add_value("total_fat", str(total_fat).split(" ")[-1])
                item.add_xpath("total_fat_percentage", "//*[contains(text(), 'Total Fat')]/../td[2]//text()")

        saturated_fat = response.xpath("//*[contains(text(), 'Saturated Fat')]//text()").get()
        if saturated_fat:
            if len(response.xpath("//*[contains(text(), 'Saturated Fat')]/..//td")) > 2:
                item.add_xpath("saturated_fat", "//*[contains(text(), 'Saturated Fat')]/../td[2]//text()")
                item.add_xpath("saturated_fat_percentage", "//*[contains(text(), 'Saturated Fat')]/../td[3]//text()")
            else:
                item.add_value("saturated_fat", str(saturated_fat).split(" ")[-1])
                item.add_xpath("saturated_fat_percentage", "//*[contains(text(), 'Saturated Fat')]/../td[2]//text()")

        trans_fat = response.xpath("//*[contains(text(), 'Trans Fat')]//text()").get()
        if trans_fat:
            if len(response.xpath("//*[contains(text(), 'Trans Fat')]/..//td")) > 2:
                item.add_xpath("trans_fat", "//*[contains(text(), 'Trans Fat')]/../td[2]//text()")
                item.add_xpath("trans_fat_percentage", "//*[contains(text(), 'Trans Fat')]/../td[3]//text()")
            else:
                item.add_value("trans_fat", str(trans_fat).split(" ")[-1])
                item.add_xpath("trans_fat_percentage", "//*[contains(text(), 'Trans Fat')]/../td[2]//text()")

        cholesterol = response.xpath("//*[contains(text(), 'Cholesterol')]//text()").get()
        if cholesterol:
            if len(response.xpath("//*[contains(text(), 'Cholesterol')]/..//td")) > 2:
                item.add_xpath("cholesterol", "//*[contains(text(), 'Cholesterol')]/../td[2]//text()")
                item.add_xpath("cholesterol_percentage", "//*[contains(text(), 'Cholesterol')]/../td[3]//text()")
            else:
                item.add_value("cholesterol", str(cholesterol).split(" ")[-1])
                item.add_xpath("cholesterol_percentage", "//*[contains(text(), 'Cholesterol')]/../td[2]//text()")

        sodium = response.xpath("//*[contains(text(), 'Sodium')]//text()").get()
        if sodium:
            if len(response.xpath("//*[contains(text(), 'Sodium')]/..//td")) > 2:
                item.add_xpath("sodium", "//*[contains(text(), 'Sodium')]/../td[2]//text()")
                item.add_xpath("sodium_percentage", "//*[contains(text(), 'Sodium')]/../td[3]//text()")
            else:
                item.add_value("sodium", str(sodium).split(" ")[-1])
                item.add_xpath("sodium_percentage", "//*[contains(text(), 'Sodium')]/../td[2]//text()")

        potassium = response.xpath("//*[contains(text(), 'Potassium')]//text()").get()
        if potassium:
            if len(response.xpath("//*[contains(text(), 'Potassium')]/..//td")) > 2:
                item.add_xpath("potassium", "//*[contains(text(), 'Potassium')]/../td[2]//text()")
                item.add_xpath("potassium_percentage", "//*[contains(text(), 'Potassium')]/../td[3]//text()")
            else:
                item.add_value("potassium", str(potassium).split(" ")[-1])
                item.add_xpath("potassium_percentage", "//*[contains(text(), 'Potassium')]/../td[2]//text()")

        total_carbohydrate = response.xpath("//*[contains(text(), 'Total Carbohydrate')]//text()").get()
        if total_carbohydrate:
            if len(response.xpath("//*[contains(text(), 'Total Carbohydrate')]/..//td")) > 2:
                item.add_xpath("total_carbohydrate", "//*[contains(text(), 'Total Carbohydrate')]/../td[2]//text()")
                item.add_xpath("total_carbohydrate_percentage", "//*[contains(text(), 'Total Carbohydrate')]/../td[3]//text()")
            else:
                item.add_value("total_carbohydrate", str(total_carbohydrate).split(" ")[-1])
                item.add_xpath("total_carbohydrate_percentage", "//*[contains(text(), 'Total Carbohydrate')]/../td[2]//text()")

        dietary_fiber = response.xpath("//*[contains(text(), 'Dietary Fiber')]//text()").get()
        if dietary_fiber:
            if len(response.xpath("//*[contains(text(), 'Dietary Fiber')]/..//td")) > 2:
                item.add_xpath("dietary_fiber", "//*[contains(text(), 'Dietary Fiber')]/../td[2]//text()")
                item.add_xpath("dietary_fiber_percentage", "//*[contains(text(), 'Dietary Fiber')]/../td[3]//text()")
            else:
                item.add_value("dietary_fiber", str(dietary_fiber).split(" ")[-1])
                item.add_xpath("dietary_fiber_percentage", "//*[contains(text(), 'Dietary Fiber')]/../td[2]//text()")

        sugars = response.xpath("//td[contains(text(), 'Sugar')]//text()").get()
        if sugars:
            if len(response.xpath("//*[contains(text(), 'Sugars')]/..//td")) > 2:
                item.add_xpath("sugars", "//*[contains(text(), 'Sugars')]/../td[2]//text()")
            else:
                item.add_value("sugars", str(sugars).split(" ")[-1])

        protein = response.xpath("//div[@class='nutritionalfacts']//td[contains(text(), 'Protein')]//text()").get()
        if protein:
            if len(response.xpath("//div[@class='nutritionalfacts']//td[contains(text(), 'Protein')]/..//td")) > 2:
                item.add_xpath("protein", "//div[@class='nutritionalfacts']//td[contains(text(), 'Protein')]/../td[2]//text()")
                item.add_xpath("protein_percentage", "//div[@class='nutritionalfacts']//td[contains(text(), 'Protein')]/../td[3]//text()")
            else:
                item.add_value("protein", str(protein).split(" ")[-1])
                item.add_xpath("protein_percentage", "//div[@class='nutritionalfacts']//td[contains(text(), 'Protein')]/../td[2]//text()")

        return item.load_item()

    def parse_items_metrx(self, response):
        lists = []
        base_url = "https://shop.metrx.com"

        for url in response.xpath("//div[@class='item_detail']/a/@href").extract():
            lists.append(
                Request(base_url+url, callback=self.metrx)
            )

        return lists

    def metrx(self, response):
        lists = []

        name = response.xpath("//img[@id='product_image']/@alt").extract_first()
        images = response.xpath("//meta[@property='og:image']/@content").get()

        for res in response.xpath("//div[@id='REG-groups']//li[@class='variant_pricing']"):
            item = ItemLoader(ProteinBarsItem(), res)

            size = res.xpath(".//div[@class='line-one']/text()").get()

            item.add_value("src", response.url)
            item.add_value("name", f"{name} - {size}")
            item.add_value("brand", "Met-Rx")
            item.add_xpath("price", ".//div[@class='line-two']/text()")
            item.add_value("images", images)
            item.add_value("nutrition_facts_image_url", response.xpath("//div[@class='nutrition']//img/@src").get())
            item.add_value("ingredients", response.xpath("//div[@class='ingredpop']//text()").get())

            lists.append(item.load_item())

        return lists

    def parse_items_proti(self, response):
        lists = []

        for url in list(set(response.xpath("//div[@class='card-img-container']/../@href").extract())):
            lists.append(
                Request(url, callback=self.proti)
            )

        next_page = response.xpath("//a[@data-title='Next']/@href").get()
        if next_page:
            lists.append(
                Request(next_page, callback=self.parse_items_proti)
            )
        return lists

    def proti(self, response):
        item = ItemLoader(ProteinBarsItem(), response)

        item.add_value('src', response.url)
        item.add_value('brand', "Proti")
        item.add_xpath('name', "//h1[@itemprop='name']/text()")
        item.add_xpath('price', "//meta[@itemprop='price']/@content")
        item.add_xpath('sku', "//dt[contains(text(), 'SKU:')]/../dd/text()")
        item.add_xpath('images', "//div[contains(@class, 'swiper-slide')]//img/@src")
        item.add_xpath('description', "//article[@itemprop='description']//text()")

        return item.load_item()

    def parse_items_nashua(self, response):
        lists = []

        for url in list(set(response.xpath("//div[@class='product-image']/a/@href").extract())):
            lists.append(
                Request(f"https://www.nashuanutrition.com{url}", callback=self.nugo)
            )

        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            print(f"https://www.nashuanutrition.com{next_page}")
            lists.append(
                Request(f"https://www.nashuanutrition.com{next_page}", callback=self.parse_items_nashua)
            )
        return lists

    def nashua(self, response):
        lists = []
        json_data = requests.get(f"{response.url}.js").json()

        for index, data in enumerate(json_data['variants']):
            item = ItemLoader(ProteinBarsItem(), response)

            item.add_value("src", response.url)
            item.add_value("product_id", str(data['id']))
            item.add_value("name", data['name'])
            item.add_value("brand", "Nashua Nutrition")

            description = bs4.BeautifulSoup(json_data['description'], features="lxml")
            item.add_value("description", description.get_text())
            item.add_value("sku", data['sku'])
            item.add_value("barcode", data['barcode'])
            item.add_value("available", "yes" if data['available'] else "no")
            item.add_value("price", str(data['price']/100))
            item.add_value("tags", ', '.join(json_data['tags']))
            item.add_value("vendor", json_data['vendor'])
            item.add_value("images", " , ".join(json_data['images']))

            item.add_xpath("protein", "//strong[text()='Protein']/../../td[2]//text()")
            item.add_xpath("sugars", "//strong[text()='Sugars']/../../td[2]//text()")
            item.add_xpath("sodium", "//strong[text()='Sodium']/../../td[2]//text()")
            item.add_xpath("cholesterol", "//strong[text()='Cholesterol']/../../td[2]//text()")
            item.add_xpath("trans_fat", "//strong[text()='   Trans. Fat']/../../td[2]//text()")
            item.add_xpath("saturated_fat", "//strong[text()='   Saturated Fat']/../../td[2]//text()")
            item.add_xpath("total_fat", "//strong[text()='Total Fat']/../../td[2]//text()")
            item.add_xpath("calories", "//strong[text()='Calories']/../../td[2]//text()")

            lists.append(item.load_item())
        return lists

    def parse_items_nugo(self, response):
        lists = []

        for url in list(set(response.xpath("//div[@id='collection']//a[@class='img-align']/@href").extract())):
            lists.append(
                Request(f"https://www.nugonutrition.com{url}", callback=self.nugo)
            )

        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            lists.append(
                Request(f"https://www.nugonutrition.com{next_page}", callback=self.parse_items_nugo)
            )
        return lists

    def nugo(self, response):
        lists = []
        json_data = requests.get(f"{response.url}.js").json()

        for index, data in enumerate(json_data['variants']):
            item = ItemLoader(ProteinBarsItem(), response)

            item.add_value("src", response.url)
            item.add_value("product_id", str(data['id']))
            item.add_value("name", data['name'])
            item.add_value("brand", "NuGo")

            description = bs4.BeautifulSoup(json_data['description'], features="lxml")
            item.add_value("description", description.get_text())
            item.add_value("sku", data['sku'])
            item.add_value("barcode", data['barcode'])
            item.add_value("available", "yes" if data['available'] else "no")
            item.add_value("price", str(data['price']/100))
            item.add_value("tags", ', '.join(json_data['tags']))
            item.add_value("vendor", json_data['vendor'])
            item.add_value("images", " , ".join(json_data['images']))

            for i in response.xpath("//div[@class='product-health-icons']//li"):
                if i.xpath('./h4/text()').get() == 'Protein':
                    item.add_value("protein", i.xpath('./span/text()').get())
                if i.xpath('./h4/text()').get() == 'Carbohydrate':
                    item.add_value("total_carbohydrate", i.xpath('./span/text()').get())
                if i.xpath('./h4/text()').get() == 'Sugar':
                    item.add_value("sugars", i.xpath('./span/text()').get())
                if i.xpath('./h4/text()').get() == 'Fiber':
                    item.add_value("dietary_fiber", i.xpath('./span/text()').get())
            item.add_xpath("nutrition_facts_image_url", "//div[@id='description-1']//img/@src")

            lists.append(item.load_item())
        return lists

    def parse_items_quest(self, response):
        lists = []

        for url in list(set(response.xpath("//a[@class='product-item__image']/@href").extract())):
            lists.append(
                Request(f"https://www.questnutrition.com{url}", callback=self.quest)
            )

        next_page = response.xpath("//div[@class='collection__loader spinner-container']/@data-next-page").get()
        if next_page and not ".com&view=infinite-scroll" in f"https://www.questnutrition.com{next_page}":
            lists.append(
                Request(f"https://www.questnutrition.com{next_page}", callback=self.parse_items_quest)
            )
        return lists

    def quest(self, response):
        lists = []
        json_data = requests.get(f"{response.url}.js").json()

        for index, data in enumerate(json_data['variants']):
            item = ItemLoader(ProteinBarsItem(), response)

            item.add_value("src", response.url)
            item.add_value("product_id", str(data['id']))
            item.add_value("name", data['name'])
            item.add_value("brand", "Quest Nutrition")

            description = bs4.BeautifulSoup(json_data['description'], features="lxml")
            item.add_value("description", description.get_text())
            item.add_value("sku", data['sku'])
            item.add_value("barcode", data['barcode'])
            item.add_value("available", "yes" if data['available'] else "no")
            item.add_value("price", str(data['price']/100))
            item.add_value("tags", ', '.join(json_data['tags']))
            item.add_value("vendor", json_data['vendor'])
            item.add_value("images", " , ".join(json_data['images']))

            item.add_xpath("protein", "//div[@class='grid-item grid-item-stats product-stats']//li[1]/span/text()")
            item.add_xpath("total_carbohydrate", "//div[@class='grid-item grid-item-stats product-stats']//li[2]/span/text()")
            item.add_xpath("sugars", "//div[@class='grid-item grid-item-stats product-stats']//li[3]/span/text()")
            item.add_xpath("dietary_fiber", "//div[@class='grid-item grid-item-stats product-stats']//li[4]/span/text()")

            lists.append(item.load_item())
        return lists

    def parse_items_detour(self, response):
        lists = []

        for url in list(set(response.xpath("//a[@class='product-item__link-wrap']/@href").extract())):
            lists.append(
                Request(f"https://www.detourbar.com{url}", callback=self.detour)
            )
        return lists

    def detour(self, response):
        lists = []
        json_data = requests.get(f"{response.url}.js").json()

        for index, data in enumerate(json_data['variants']):
            item = ItemLoader(ProteinBarsItem(), response)

            item.add_value("src", response.url)
            item.add_value("product_id", str(data['id']))
            item.add_value("name", data['name'])
            item.add_value("brand", "Detour")

            description = bs4.BeautifulSoup(json_data['description'], features="lxml")
            item.add_value("description", description.get_text())
            item.add_value("sku", data['sku'])
            item.add_value("barcode", data['barcode'])
            item.add_value("available", "yes" if data['available'] else "no")
            item.add_value("price", str(data['price']/100))
            item.add_value("tags", ', '.join(json_data['tags']))
            item.add_value("vendor", json_data['vendor'])
            item.add_value("images", " , ".join(json_data['images']))
            item.add_xpath("serving_size", "//td[text()='Serving Size']/following-sibling::td[1]/text()")
            item.add_xpath("amount_per_serving", "//td[text()='Amount Per Serving']/following-sibling::td[2]/text()")
            item.add_xpath("calories", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Calories']/following-sibling::td[1]/text()")
            item.add_xpath("calories_from_fat", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Calories from Fat']/following-sibling::td[1]/text()")
            item.add_xpath("total_fat", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Total Fat']/following-sibling::td[1]/text()")
            item.add_xpath("total_fat_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Total Fat']/following-sibling::td[2]/text()")
            item.add_xpath("saturated_fat", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Saturated Fat']/following-sibling::td[1]/text()")
            item.add_xpath("saturated_fat_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Saturated Fat']/following-sibling::td[2]/text()")
            item.add_xpath("trans_fat", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Trans Fat']/following-sibling::td[1]/text()")
            item.add_xpath("cholesterol", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Cholesterol']/following-sibling::td[1]/text()")
            item.add_xpath("cholesterol_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Cholesterol']/following-sibling::td[2]/text()")
            item.add_xpath("sodium", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Sodium']/following-sibling::td[1]/text()")
            item.add_xpath("sodium_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Sodium']/following-sibling::td[2]/text()")
            item.add_xpath("potassium", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Potassium']/following-sibling::td[1]/text()")
            item.add_xpath("potassium_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Potassium']/following-sibling::td[2]/text()")
            item.add_xpath("total_carbohydrate", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Total Carbohydrate']/following-sibling::td[1]/text()")
            item.add_xpath("total_carbohydrate_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Total Carbohydrate']/following-sibling::td[2]/text()")
            item.add_xpath("dietary_fiber", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Dietary Fiber']/following-sibling::td[1]/text()")
            item.add_xpath("dietary_fiber_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Dietary Fiber']/following-sibling::td[2]/text()")
            item.add_xpath("sugars", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Sugars']/following-sibling::td[1]/text()")
            item.add_xpath("protein", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Protein']/following-sibling::td[1]/text()")
            item.add_xpath("protein_percentage", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Protein']/following-sibling::td[2]/text()")
            item.add_xpath("vitamin_a", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Vitamin A']/following-sibling::td[1]/text()")
            item.add_xpath("vitamin_c", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Vitamin C']/following-sibling::td[2]/text()")
            item.add_xpath("calcium", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Calcium']/following-sibling::td[2]/text()")
            item.add_xpath("iron", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Iron']/following-sibling::td[2]/text()")
            item.add_xpath("thiamin", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Thiamin']/following-sibling::td[2]/text()")
            item.add_xpath("riboflavin", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Riboflavin']/following-sibling::td[2]/text()")
            item.add_xpath("niacin", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Niacin']/following-sibling::td[2]/text()")
            item.add_xpath("vitamin_b6", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Vitamin B6']/following-sibling::td[2]/text()")
            item.add_xpath("vitamin_b12", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Vitamin B12']/following-sibling::td[2]/text()")
            item.add_xpath("phosphorus", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Phosphorus']/following-sibling::td[2]/text()")
            item.add_xpath("magnesium", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Magnesium']/following-sibling::td[2]/text()")
            item.add_xpath("manganese", f"//div[@data-fade-index='variants-{index+1}']//td[text()='Manganese']/following-sibling::td[2]/text()")

            lists.append(item.load_item())
        return lists


import re
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