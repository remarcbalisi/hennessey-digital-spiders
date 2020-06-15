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


class OathmegaSpider(CrawlSpider):
    name = 'oatmega'

    def __init__(self, *args, **kwargs):
        super(OathmegaSpider, self).__init__(*args, **kwargs)
        self.url = 'https://shop.oatmega.com/Bars/c/Oatmega@Bars'
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def start_requests(self):
        lists = []

        if not self.url:
            return None
        else:
            lists.append(FormRequest(self.url, callback=self.parse_item))

        return lists

    def parse_item(self, response):
        products = response.xpath('//div[@class="item_detail"]/div/a/@href').extract()
        lists = []
        base_url = 'https://shop.oatmega.com'
        for link in products:
            lists.append(
                Request(f"{base_url}{link}", callback=self.item)
            )

        return lists

    def item(self, response):
        lists = []
        variants = response.xpath('//div[@class="variant_row"]/form/div[@class="product"]/div[1]/text()').getall()
        prices = response.xpath('//div[@class="reg_price"]/span[2]/text()').getall()
        counter = 0
        reviews = self.crawl_reviews(response.url)
        for variant in variants:
            item = ItemLoader(ProteinBarsItem(), response)
            item.add_value('amount_per_serving', variant)
            item.add_value('available', 'yes')
            name = response.xpath('//h1[@class="page_title"]/text()').get()
            item.add_value('name', f"OatMega {name} - {variant}")
            item.add_value('brand', 'Oatmega')
            item.add_xpath('description', '//*[@id="product_detail"]/div[2]/div/div[3]/p[2]/text()')
            item.add_xpath('images', '//*[@id="product_detail"]/div[1]/div[2]/img/@src')
            ingredients = response.xpath('//*[@id="ingredients_display"]/p[1]/text()').get()
            item.add_value('ingredients', ingredients.replace('INGREDIENTS: ', ''))
            item.add_value('price', prices[counter])
            item.add_value('src', response.url)
            item.add_xpath('nutrition_facts_image_url', '//*[@id="nutrition_display"]/div/img/@src')
            item.add_value('reviews', reviews)
            lists.append(item.load_item())
            counter += 1

        return lists

    def crawl_reviews(self, url):
        self.browser.get(url)
        button_is_clickable = True
        review_array = []

        try:
            pop_out = WebDriverWait(self.browser, 120).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'div.popup')))
            pop_out[0].find_element_by_css_selector("div.close").click()

        except NoSuchElementException:
            print(colored('NoSuchElementException in popout', 'red'))

        except ElementNotInteractableException:
            print(colored('ElementNotInteractableException in popout', 'red'))

        except ElementClickInterceptedException:
            print(colored('ElementClickInterceptedException in popout', 'red'))

        while button_is_clickable is True:
            order_list = WebDriverWait(self.browser, 120).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.bv-content-list-reviews')))
            reviews = order_list[0].find_elements_by_css_selector("li.bv-content-item")

            for review in reviews:
                name = review.find_element_by_xpath("//div[@class='bv-content-author-name']/button/h3")
                body = review.find_element_by_xpath("//div[@class='bv-content-summary-body-text']/p")
                star = review.find_element_by_css_selector("span.bv-content-rating meta:nth-child(1)").get_attribute(
                    "content")
                title = review.find_element_by_css_selector("h3.bv-content-title")
                print(colored(f"reviewers name {name.text} - {star} - {title.text}", 'yellow'))
                review_contents = {
                    'name': name.text,
                    'body': body.text,
                    'stars': star,
                    'title': title.text,
                }
                review_array.append(review_contents)

            try:
                next_btn = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 'li.bv-content-pagination-buttons-item-next a')))
                next_btn[0].click()
                time.sleep(5)
            except NoSuchElementException:
                button_is_clickable = False
                print(colored('NoSuchElementException', 'red'))

            except ElementNotInteractableException:
                button_is_clickable = False
                print(colored('ElementNotInteractableException', 'red'))

            except TimeoutException:
                button_is_clickable = False
                print(colored('TimeoutException', 'red'))

            except ElementClickInterceptedException:
                # button_is_clickable = False
                print(colored('ElementClickInterceptedException', 'red'))

        return json.dumps(review_array)
