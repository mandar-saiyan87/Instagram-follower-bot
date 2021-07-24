'''
Script to follow all followers of an Instagram accounts.
Instagram doesn't allow to follow more than 60 accounts per hour.
So script can be re-run to follow remaining accounts.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ------------------------------------- URL AND CREDS CONSTANTS ----------------------- #

CHROME_DRIVER = 'chromedriver_win32\chromedriver.exe'
URL = 'https://www.instagram.com/'
INSTA_USER = 'YOUR_USERNAME'
INSTA_PASS = 'YOUR_PASSWORD'

# ------------------------------- INSTAFOLLOWER CLASSES AND METHODS ------------------- #

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.driver.get(URL)

    def login(self, user, passwd):
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]').click()
        time.sleep(15)
        self.driver.find_element_by_name('email').send_keys(user)
        self.driver.find_element_by_name('pass').send_keys(passwd)
        self.driver.find_element_by_name('login').click()
        time.sleep(20)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def find_followers(self, account_name):
        self.driver.get(f'https://www.instagram.com/{account_name}/')
        time.sleep(20)

        self.followers = self.driver.find_elements_by_css_selector('ul li .-nal3 ')
        self.follower = self.driver.find_element_by_partial_link_text('follower').text.split(' ')[0].replace(',', '')
        self.follower_count = int(self.follower)
        # if self.follower_count > 10:
        #     self.follower_count -= 5
        time.sleep(15)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(15)

        self.follower_popup = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        self.follower_nos_1 = 0
        self.follower_nos_2 = 1

        # while self.follower_nos < self.follower_count and self.follower_count > 5:
        while self.follower_count > 8 and self.follower_nos_1 != self.follower_nos_2:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.follower_popup)
            time.sleep(7)
            self.total_follow_list = len(self.follower_popup.find_elements_by_css_selector('li'))
            print(self.total_follow_list)
            self.follower_nos_1 = self.follower_nos_2
            self.follower_nos_2 = self.total_follow_list
            print(f'{self.follower_nos_1}:{self.follower_nos_2}')

    def follow(self):
        self.follow_list = self.follower_popup.find_elements_by_css_selector('li button')
        for self.follow_status in self.follow_list:
            if self.follow_status.text == 'Follow':
                self.follow_status.click()
            time.sleep(2)
        self.driver.find_element_by_css_selector('.WaOAr button').click()

    def logout(self):
        self.driver.find_element_by_css_selector('.ctQZg ._8-yf5 ').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('gmFkV').click()
        time.sleep(20)
        self.driver.find_element_by_css_selector('.zwlfE button').click()
        time.sleep(20)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[9]').click()
        self.driver.quit()

    def no_element_error(self):
        pass


# -------------------------------------- INITIATE AND RUN INSTA_BOT ---------------------------------- #

similar_account = input('Account which followers to follow: ')
insta_bot = InstaFollower()
time.sleep(10)
insta_bot.login(INSTA_USER, INSTA_PASS)
time.sleep(10)
insta_bot.find_followers(similar_account)
time.sleep(15)
insta_bot.follow()
time.sleep(15)
insta_bot.logout()

