import time

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    # options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
    # options.add_argument("--enable-javascript")  # JS無効
    return options


def search_recipe(base_url, driver, food):
    driver.get(base_url)
    driver.find_element_by_name('keyword').send_keys(food)
    driver.find_element_by_name('keyword').send_keys(Keys.ENTER)


def get_recipes(driver):
    recipe_previews = driver.find_elements_by_class_name('recipe-preview')
    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element_by_class_name('recipe-title').text
        recipe_url = recipe_preview.find_element_by_class_name('recipe-title').get_attribute('href')

        recipes.append({
            "title": recipe_title,
            "url": recipe_url})
    return recipes


def main():
    base_url = 'https://cookpad.com'
    food = 'とまと'

    with webdriver.Chrome(options=chromedriver_options()) as driver:
        search_recipe(base_url, driver, food)
        recipes = get_recipes(driver)

    for recipe in recipes:
        print(f"レシピ名 {recipe['title']}, URL:{recipe['url']}")


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
