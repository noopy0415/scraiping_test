'''
Pythonでクックパッドのレシピ検索をスクレイピングする方法
Selenium + BeautifulSoup
'''
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import chromedriver_binary
from bs4 import BeautifulSoup


def main():
    base_url = 'https://cookpad.com'
    page_url = '/search'
    food = 'とまと'

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # ヘッドレス
    # options.add_argument("--disable-gpu")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--allow-running-insecure-content")
    # options.add_argument("--disable-web-security")
    # options.add_argument("--disable-desktop-notifications")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--lang=ja")

    options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
    options.add_argument("--enable-javascript")  # JS無効

    with webdriver.Chrome(options=options) as driver:
        driver.get(f'{base_url}')

        # 検索動作
        driver.find_element(By.XPATH, '//*[@id="keyword"]')
        # driver.find_element_by_name('keyword').send_keys(food)
        driver.find_element_by_name('keyword').send_keys(Keys.ENTER)
        # driver.find_element_by_name('commit').click()
        time.sleep(5)
        html = driver.page_source

    print(html)


if __name__ == '__main__':
    main()
