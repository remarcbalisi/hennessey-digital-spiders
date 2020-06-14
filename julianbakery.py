import scrapy
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest, Selector
from scrapy.loader import ItemLoader
from .protein_bars_item import ProteinBarsItem

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions \
    import TimeoutException, \
    NoSuchElementException, \
    ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
chrome_options.add_argument("--headless")


class GrenadeSpider(CrawlSpider):
    name = 'julianbakery'

    def __init__(self, *args, **kwargs):
        super(GrenadeSpider, self).__init__(*args, **kwargs)
        self.url = 'https://julianbakery.com/shop/?fwp_categories=protein-bar&fwp_load_more=5'
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def start_requests(self):
        lists = []

        if not self.url:
            return None
        else:
            lists.append(FormRequest(self.url, callback=self.parse_item))

        return lists

    def parse_item(self, response):
        lists = []
        products = response.xpath('/html/body/main/section/div/div[2]/div[2]/div[1]/div[2]/div/div/a/@href').extract()
        for product_url in products:
            lists.append(
                Request(product_url, callback=self.item)
            )

        return lists

    def item(self, response):
        lists = []
        item = ItemLoader(ProteinBarsItem(), response)
        price = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[2]/div/div/p/span/text()').get()
        currency = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[2]/div/div/p/span/span/text()').get()

        item.add_xpath('name', '//*[@id="product-508"]/section[1]/div/div/div[1]/h1/text()')
        item.add_value('price', f"{currency}{price}")
        item.add_xpath('description',
                       '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[2]/p/text()')
        item.add_xpath('protein',
                       '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[2]/div[2]/div/span[1]')
        item.add_xpath("images", '//meta[@property="og:image"]/@content')
        item.add_value("available", 'yes')
        item.add_value("brand", 'Julian Bakery')
        item.add_value("brand", 'Julian Bakery')

        calcium = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[17]/span[1]/text()').get()
        calories = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[4]/span[2]/text()').get()
        cholesterol = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[9]/span[1]/text()').get()
        cholesterol_percentage = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[9]/span[2]/text()').get()
        dietary_fiber = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[12]/span[1]/text()').get()
        dietary_fiber_percentage = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[12]/span[2]/text()').get()
        iron = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[18]/span[1]/text()').get()
        potassium = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[19]/span[1]/text()').get()
        potassium_percentage = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[19]/span[2]/text()').get()
        saturated_fat = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[7]/span[1]/text()').get()
        saturated_fat_percentage = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[7]/span[2]/text()').get()
        serving_size = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[2]/text()').get()
        sodium = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[10]/span[1]/text()').get()
        total_sugars = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[13]/span/text()').get()
        total_carbohydrate = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[11]/span[1]/text()').get()
        total_fat = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[6]/span[1]/text()').get()
        trans_fat = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[8]/span/text()').get()

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
        item.add_xpath('ingredients',
                       '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/p[1]/text()')
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
        item.add_xpath('sodium',
                       '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[10]/span[2]/text()')
        item.add_value('src', response.url)
        if total_sugars is not None:
            item.add_value('sugars', total_sugars.split(' ')[2])
        if total_carbohydrate is not None:
            item.add_value('total_carbohydrate', total_carbohydrate.replace(' ', ''))
        item.add_xpath('total_carbohydrate_percentage',
                       '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[11]/span[2]/text()')
        if total_fat is not None:
            item.add_value('total_fat', total_fat.replace(' ', ''))
        item.add_xpath('total_fat_percentage',
                       '//div[contains(concat(" ", normalize-space(@class), " "), " product ")]/section[1]/div/div/div[1]/div[5]/div/div[6]/span[2]/text()')
        if trans_fat is not None:
            item.add_value('trans_fat', trans_fat.split(' ')[2])
        item.add_value('vendor', 'Julian Bakery')
        item.add_value('reviews', self.crawl_reviews(response.url))

        lists.append(item.load_item())

        return lists

    def crawl_reviews(self, url):
        self.browser.get(url)
        reviews = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.review')))

        review_array = []
        for review in reviews:
            name = review.find_element_by_xpath("//div[@class='comment_container']/div/p/strong")
            body = review.find_element_by_xpath("//div[@class='description']/p")
            star = review.find_element_by_xpath("//div[contains(@class, 'star-rating')]").get_attribute(
                "aria-label")
            star_count = star.split()[1]
            title = ''
            review_contents = {
                'name': name.text,
                'body': body.text,
                'stars': star_count,
                'title': title,
            }
            review_array.append(review_contents)
        return json.dumps(review_array)
