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
from termcolor import colored
import time

chrome_options = Options()


chrome_options.add_argument("--headless")


class OrgainSpider(CrawlSpider):
    name = 'orgain'

    def __init__(self, *args, **kwargs):
        super(OrgainSpider, self).__init__(*args, **kwargs)
        self.url = 'https://orgain.com/collections/protein-bar'
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def start_requests(self):

        self.browser.get(self.url)

        pop_out = WebDriverWait(self.browser, 120).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'button.needsclick')))
        pop_out[0].click()

        cc_compliance = WebDriverWait(self.browser, 120).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'cc-compliance')))
        cc_compliance[0].click()

        lists = []

        if not self.url:
            return None
        else:
            lists.append(FormRequest(self.url, callback=self.parse_item))

        return lists

    def parse_item(self, response):

        products = response.xpath('//div[@class="product-card__wrapper"]/a/@href').extract()
        lists = []
        base_url = 'https://orgain.com/'
        for link in products:
            lists.append(
                Request(f"{base_url}{link}", callback=self.item)
            )

        return lists

    def item(self, response):
        lists = []
        flavors = response.xpath("//select[@id='SingleOptionSelector-0']/option/text()").extract()
        minerals = [
            'protein',
            'calcium',
            'calories',
            'cholesterol',
            'iron',
            'magnesium',
            'manganese',
            'niacin',
            'phosphorus',
            'potassium',
            'protein',
            'riboflavin',
            'sodium',
            'sugars',
            'thiamin',
        ]

        for flavor in flavors:
            item = ItemLoader(ProteinBarsItem(), response)
            item.add_value('available', 'yes')
            item.add_value('brand', 'Orgain')
            item.add_xpath('name', "//div/h1[@class='product-form__title']")
            price = response.xpath("//div/span[@class='product-form__price-price']/text()").get()
            item.add_value('price', price)
            item.add_xpath('description', "//div[contains(@class, 'product-form__description')]/p")

            stats_desktop = response.xpath("//div[@class='product-stats__wrapper stats-desktop']/div[1]")
            product_stats = stats_desktop.xpath("//div[@class='product-stats']")
            product_minerals = []
            product_amount = []
            product_unit = []
            for i in range(1):
                product_minerals = product_stats[i].xpath("//p[@class='product-stats__text']/text()").getall()[:5]
                product_amount = product_stats[i].xpath("//div[@class='product-stats__main']/p[1]/text()").getall()[:5]
                product_unit = product_stats[i].xpath("//div[@class='product-stats__main']/p[2]/text()").getall()[:5]

            for i in range(5):
                if product_minerals[i].lower() in minerals:
                    item.add_value(product_minerals[i].lower(), f"{product_amount[i]}{product_unit[i]}")

            item.add_xpath('images', "//div[@class='product-images__list']/div/div/img/@src")
            lists.append(item.load_item())

        return lists

    # def crawl_reviews(self, url):
    #     self.browser.get(url)
    #     button_is_clickable = True
    #     review_array = []
    #     reviews = []
    #     try:
    #         # pop_out = WebDriverWait(self.browser, 120).until(
    #         #     EC.presence_of_all_elements_located(
    #         #         (By.CSS_SELECTOR, 'div.popup')))
    #         # pop_out[0].find_element_by_css_selector("div.close").click()
    #
    #         reviews = WebDriverWait(self.browser, 120).until(
    #             EC.presence_of_all_elements_located(
    #                 (By.CSS_SELECTOR, 'div.pr-review')))
    #
    #     except NoSuchElementException:
    #         print(colored('NoSuchElementException in popout', 'red'))
    #
    #     except ElementNotInteractableException:
    #         print(colored('ElementNotInteractableException in popout', 'red'))
    #
    #     except ElementClickInterceptedException:
    #         print(colored('ElementClickInterceptedException in popout', 'red'))
    #
    #     while button_is_clickable is True:
    #         order_list = WebDriverWait(self.browser, 120).until(
    #             EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.bv-content-list-reviews')))
    #         reviews = order_list[0].find_elements_by_css_selector("li.bv-content-item")
    #
    #         for review in reviews:
    #             name = review.find_element_by_xpath("//div[@class='bv-content-author-name']/button/h3")
    #             body = review.find_element_by_xpath("//div[@class='bv-content-summary-body-text']/p")
    #             star = review.find_element_by_css_selector("span.bv-content-rating meta:nth-child(1)").get_attribute(
    #                 "content")
    #             title = review.find_element_by_css_selector("h3.bv-content-title")
    #             print(colored(f"reviewers name {name.text} - {star} - {title.text}", 'yellow'))
    #             review_contents = {
    #                 'name': name.text,
    #                 'body': body.text,
    #                 'stars': star,
    #                 'title': title.text,
    #             }
    #             review_array.append(review_contents)
    #
    #         try:
    #             next_btn = WebDriverWait(self.browser, 10).until(
    #                 EC.presence_of_all_elements_located(
    #                     (By.CSS_SELECTOR, 'li.bv-content-pagination-buttons-item-next a')))
    #             next_btn[0].click()
    #             time.sleep(5)
    #         except NoSuchElementException:
    #             button_is_clickable = False
    #             print(colored('NoSuchElementException', 'red'))
    #
    #         except ElementNotInteractableException:
    #             button_is_clickable = False
    #             print(colored('ElementNotInteractableException', 'red'))
    #
    #         except TimeoutException:
    #             button_is_clickable = False
    #             print(colored('TimeoutException', 'red'))
    #
    #         except ElementClickInterceptedException:
    #             # button_is_clickable = False
    #             print(colored('ElementClickInterceptedException', 'red'))
    #
    #     return json.dumps(review_array)
