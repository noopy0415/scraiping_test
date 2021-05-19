from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test03 import base_url


def chromedriver_options():
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
    return options


def get_recipe_page_with_selenium(driver, food):
    '''
    クックパッドでfoodの検索結果のhtmlを返す関数
    '''
    driver.get(f'{base_url}')

    # 検索動作
    driver.find_element(By.XPATH, '//*[@id="keyword"]').send_keys(food)
    # driver.find_element_by_name('keyword').send_keys(food)
    driver.find_element_by_name('keyword').send_keys(Keys.ENTER)
    # driver.find_element_by_name('commit').click()
    url = driver.find_elements_by_xpath('//a[starts-with(@id,"recipe_title_")]')[0].get_attribute('href')
    title = driver.find_elements_by_xpath('//a[starts-with(@id,"recipe_title_")]')[0].text
    html = driver.page_source
    return {"html": html, "driver": driver}


def get_recipes_by_driver_with_selenium(driver):
    recipe_previews = driver.find_elements_by_class_name('recipe-preview')

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element_by_class_name('recipe-title')
        recipe_url = recipe_preview.find_element_by_class_name('recipe-title')

        recipes.append({
            "title": recipe_title,
            "url": f"https://cookpad.com{recipe_url}"})
    return recipes
