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

chrome_options = Options()
chrome_options.add_argument("--headless")


class GrenadeSpider(CrawlSpider):
    name = 'grenade'

    def __init__(self, *args, **kwargs):
        super(GrenadeSpider, self).__init__(*args, **kwargs)
        self.url = 'https://www.grenade.com/us/grenade-carb-killa/'
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
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
                Request(f"{base_url}{category}", callback=self.item)
            )
        return lists

    def item(self, response):
        print('item')
        print(response)
        lists = []
        item = ItemLoader(ProteinBarsItem(), response)
        amount_per_serving = response.xpath(
            '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[1]/th[2]/text()').get()
        item.add_value("amount_per_serving",
                       amount_per_serving[amount_per_serving.find("(") + 1:amount_per_serving.find(")")])
        item.add_value("brand", 'Carb Killa')
        item.add_value("vendor", 'Grenade')
        item.add_value("available", 'yes')
        item.add_value('src', response.url)
        item.add_xpath("images", '//meta[@property="og:image"]/@content')

        item.add_xpath('name', '//*[@id="maincontent"]/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/h1/text()')
        item.add_xpath('calories',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[2]/td[2]/text()')
        item.add_xpath('cholesterol',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[6]/td[2]/text()')
        item.add_xpath('cholesterol_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[6]/td[3]/text()')
        item.add_xpath('description', '//*[@id="maincontent"]/div[2]/div/div[4]/div[2]/div[1]/div[3]/div/p[1]')
        item.add_xpath('dietary_fiber',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[10]/td[2]/text()')
        item.add_xpath('dietary_fiber_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[10]/td[3]/text()')
        item.add_xpath('ingredients', '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[1]/div/div/p[1]/text()')
        item.add_xpath('potassium',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[8]/td[2]/text()')
        item.add_xpath('potassium_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[8]/td[3]/text()')
        item.add_xpath('price', '//*[@id="maincontent"]/div[2]/div/div[4]/div[2]/div[1]/div[2]/div/span/text()')
        item.add_xpath('protein',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[14]/td[2]/text()')
        item.add_xpath('protein_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[14]/td[3]/text()')
        item.add_xpath('saturated_fat',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[4]/td[2]/text()')
        item.add_xpath('saturated_fat_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[4]/td[3]/text()')
        item.add_xpath('sodium',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[7]/td[2]/text()')
        item.add_xpath('sodium_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[7]/td[3]/text()')
        item.add_xpath('sugars',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[11]/td[2]/text()')
        item.add_xpath('total_carbohydrate',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[9]/td[2]/text()')
        item.add_xpath('total_carbohydrate_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[9]/td[3]/text()')
        item.add_xpath('total_fat',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[3]/td[2]/text()')
        item.add_xpath('total_fat_percentage',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[3]/td[3]/text()')
        item.add_xpath('trans_fat',
                       '/html/body/div[1]/section/div[1]/div[1]/div[30]/div[2]/table/tbody/tr[5]/td[3]/text()')
        item.add_xpath('shipping_info', '//*[@id="open-shipping-modal"]/text()')
        item.add_value('reviews', self.review_string_arr)
        lists.append(item.load_item())

        return lists

    def crawl_reviews(self):
        self.browser.get(self.url)
        button_is_clickable = True
        while button_is_clickable is True:
            try:
                button = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, 'more-reviews')))
                button[0].click()
                print('button')
                print(button)
                # button[0].click()
            except NoSuchElementException:
                button_is_clickable = False

            except ElementNotInteractableException:
                button_is_clickable = False

            except ElementClickInterceptedException: continue

        reviews = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.review-body-text')))

        for review in reviews:
            body = review.find_element_by_css_selector("span[class='partial']")
            print(body)
            self.review_string_arr.append(body.text)