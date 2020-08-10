"""
    Selenium-Tutorial.py
    ---------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

geckodriver_exe_path = "C:/Selenium/WebDriver/bin/geckodriver"


def main(args):
    with webdriver.Firefox(executable_path=geckodriver_exe_path) as driver:
        driver.get(
            "https://wiki.eveuniversity.org/index.php?title=Special:DeadendPages&limit=500&offset=0"
        )

        links_titles = get_special_links_titles(driver)
        for link_title in links_titles:
            get_page_categories(driver, link_title)


def get_special_links_titles(driver):
    links_titles = []
    try:
        search_results = driver.find_element(By.CSS_SELECTOR, ".special")
        result_blocks = search_results.find_elements(By.TAG_NAME, "li")
        for result_block in result_blocks:
            link_element = result_block.find_element(By.XPATH, "a")
            link = link_element.get_attribute("href")
            title = link_element.get_attribute("title")
            links_titles.append([link, title])
    except:
        print("No links have been found.")

    return links_titles


def get_page_categories(driver, link_title):
    get_page(driver, link_title)

    get_categories(driver)


def get_page(driver, link_title):
    print("Getting page " + link_title[0] + " with title " + link_title[1])
    driver.get(link_title[0])
    try:
        WebDriverWait(driver, 15).until(EC.title_contains((link_title[1])))
    except:
        print("Titles do not match. Skipping.")


def get_categories(driver):
    try:
        categories_elements = driver.find_element(
            By.CSS_SELECTOR, "#mw-normal-catlinks > ul:nth-child(2)"
        )

        categories = categories_elements.find_elements(By.TAG_NAME, "li")
        for category in categories:
            link_element = category.find_element(By.XPATH, "a")
            text = link_element.text
            print(text)
    except:
        print("No links have been found.")


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
