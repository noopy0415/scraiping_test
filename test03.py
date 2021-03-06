"""
Pythonでクックパッドのレシピ検索をスクレイピングする方法
Selenium + BeautifulSoup
"""

import requests as requests
from selenium import webdriver

import bs4

from with_selenium import chromedriver_options, get_recipe_page_with_selenium, get_recipes_by_driver_with_selenium

base_url = 'https://cookpad.com'


def get_recipe_page_with_requests(base_url, food):
    response = requests.get(f"{base_url}/search/{food}")
    html = response.text
    return html


def get_recipes_by_html_with_bs4(base_url, html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    recipe_previews = soup.find_all(class_="recipe-preview")

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find(class_="recipe-title").text
        recipe_url = recipe_preview.find(class_="recipe-title").attrs['href']

        recipes.append({
            "title": recipe_title,
            "url": f"{base_url}{recipe_url}"})
    return recipes


def main():
    food = 'とまと'

    with webdriver.Chrome(options=chromedriver_options()) as driver:
        driver = get_recipe_page_with_selenium(driver, food)['driver']
        recipes = get_recipes_by_html_with_selenium(driver)

    html = recipe_page['html']
    recipes = get_recipes_by_driver_with_selenium(recipe_page['driver'])

    # recipes = get_recipe_page_with_requests(base_url, food)
    # recipes = get_recipes_by_html_with_bs4(base_url, html)

    for recipe in recipes:
        print(f"{recipe['title']}, {recipe['url']}")


if __name__ == '__main__':
    main()
