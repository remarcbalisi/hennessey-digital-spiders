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
import time
from termcolor import colored

chrome_options = Options()
chrome_options.add_argument("--headless")


class MusclePharmSpider(CrawlSpider):
    name = 'musclepharm'

    def __init__(self, *args, **kwargs):
        super(MusclePharmSpider, self).__init__(*args, **kwargs)
        self.url = 'https://musclepharm.com/collections/protein/products/combat-crunch-1?variant=37547061770'
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.review_string_arr = []

    def start_requests(self):
        lists = []

        if not self.url:
            return None
        else:
            lists.append(Request(self.url, callback=self.parse_item))

        return lists

    def parse_item(self, response):

        self.crawl_reviews()

        lists = []
        variants = response.xpath(
            '//select[@id="product-select-10077302986productproduct-template"]/option/text()').getall()
        for variant in variants:
            item = ItemLoader(ProteinBarsItem(), response)
            sold_out = response.xpath(
                '//*[@id="shopify-section-product-template"]/div[1]/div[2]/div[1]/div/div[3]/p/span[1]/text()').get()
            item.add_value('brand', 'Muscle Pharm')
            item.add_value('calories', '210')
            item.add_xpath('description',
                           '//*[@id="shopify-section-product-template"]/div[1]/div[2]/div[1]/div/div[3]/div[2]/p/span')
            item.add_xpath('description',
                           '//*[@id="shopify-section-product-template"]/div[1]/div[2]/div[1]/div/div[3]/div[2]/p/span')
            item.add_xpath('images', "//meta[@property='og:image']/@content")
            item.add_value('name', f"COMBAT CRUNCH PROTEIN BARS {variant}")
            item.add_xpath('price',
                           '//*[@id="shopify-section-product-template"]/div[1]/div[2]/div[1]/div/div[3]/p/span[2]/span/span/text()')
            item.add_value('protein', '20g')
            item.add_value('available', 'yes' if sold_out is None else 'no')
            item.add_value('reviews', json.dumps(self.review_string_arr))
            lists.append(item.load_item())

        return lists

    def crawl_reviews(self):
        print(colored('crawling reviews', 'yellow'))
        self.browser.get(self.url)

        cc_compliance = WebDriverWait(self.browser, 120).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'cc-compliance')))

        modal = WebDriverWait(self.browser, 120).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'animation__AnimatedModal-sc-1umet7i-0')))

        modal[0].find_element_by_css_selector("button.needsclick").click()
        time.sleep(3)
        cc_compliance[0].click()

        WebDriverWait(self.browser, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'opw-paginator-li')))
        pages_array = ['1', '2', '3', '4', '5']
        for i in range(7):
            pages = WebDriverWait(self.browser, 60).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'opw-paginator-li')))
            anchor = pages[i].find_element_by_css_selector('a.opw-paginator-a')
            if anchor.text in pages_array:
                next_page_anchor = pages[i].find_element_by_css_selector('a.opw-paginator-a')
                try:
                    next_page_anchor.click()
                except ElementClickInterceptedException:
                    time.sleep(10)
                time.sleep(10)
                review_card_containers = WebDriverWait(self.browser, 60).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'review-card-container')))
                for rcc in review_card_containers:
                    name = rcc.find_element_by_css_selector(".review-author")
                    body = rcc.find_element_by_css_selector("div.opinew-review-text-container, p")
                    class_attrib = rcc.find_elements_by_css_selector(
                        f"div.opinew-review-card-upper span i.opw-noci-star-full")

                    review_contents = {
                        'name': name.text,
                        'body': body.text,
                        'stars': len(class_attrib),
                        'title': '',
                    }

                    self.review_string_arr.append(review_contents)