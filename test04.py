import time

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Chrome()

    driver.get('http://www.google.com')

    driver.find_element_by_name('q').send_keys('八幡平')
    driver.find_element_by_name('q').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3').click()

    time.sleep(5)

    # driver.close()

if __name__ == '__main__':
    main()
