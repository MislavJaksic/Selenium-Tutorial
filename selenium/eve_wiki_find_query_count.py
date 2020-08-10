"""
    Selenium-Tutorial.py
    ---------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

import data

geckodriver_exe_path = "C:/WebDriver/bin/geckodriver"


def main(args):
    with webdriver.Firefox(executable_path=geckodriver_exe_path) as driver:
        driver.get("https://wiki.eveuniversity.org/Main_Page")
        assert "EVE University Wiki" in driver.title

        dict = data.rename_pairs
        for query in dict:
            search(driver, query)

            count(driver)


def search(driver, query):
    print("Searching for: " + query)
    query_element = driver.find_element(By.CSS_SELECTOR, "#searchInput")
    search_element = driver.find_element(By.CSS_SELECTOR, "#searchButton")

    query_element.send_keys('"' + query + '"')
    search_element.click()


def count(driver):
    try:
        search_result_count = driver.find_element(
            By.CSS_SELECTOR, ".results-info > strong:nth-child(2)"
        )
        print("Count: " + search_result_count.text)
    except:
        print("Count: 0")


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
