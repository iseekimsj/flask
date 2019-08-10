from bs4 import BeautifulSoup
from selenium import webdriver


class NaverLogin:

    def __init__(self, url):
        self.driver = webdriver.Chrome('./data/chromedriver')
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def auto_login(self):
        self.driver.find_element_by_name('id').send_keys('iseekimsj')
        self.driver.find_element_by_name('pw').send_keys('*********')
        self.driver.implicitly_wait(3)

        self.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(3)

        self.driver.get('https://order.pay.naver.com/home')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        notices = soup.select('div.p_inr > div.p_info > a > span')

        for i in notices:
            print(i.text.strip())








