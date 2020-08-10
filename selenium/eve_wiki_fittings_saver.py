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
            "https://wiki.eveuniversity.org/index.php?title=Special:Search&limit=500&offset=0&profile=default&search=%22shipFitting%22"
        )

        links_titles = get_search_result_links_titles(driver)
        for link_title in links_titles:
            get_page_fittings(driver, link_title)


def get_search_result_links_titles(driver):
    links_titles = []
    try:
        search_results = driver.find_element(By.CSS_SELECTOR, ".mw-search-results")
        result_blocks = search_results.find_elements(
            By.CLASS_NAME, "mw-search-result-heading"
        )
        for result_block in result_blocks:
            link_element = result_block.find_element(By.XPATH, "a")
            link = link_element.get_attribute("href")
            title = link_element.get_attribute("title")
            links_titles.append([link, title])
    except:
        print("No links have been found.")

    return links_titles


def get_page_fittings(driver, link_title):
    get_page(driver, link_title)

    # press_etf_fitting_buttons(driver)

    write_fittings_to_file(driver)


def get_page(driver, link_title):
    print("Getting page " + link_title[0] + " with title " + link_title[1])
    driver.get(link_title[0])
    try:
        WebDriverWait(driver, 15).until(EC.title_contains((link_title[1])))
    except:
        print("Titles do not match. Skipping.")


# def press_etf_fitting_buttons(driver):
#     try:
#         ship_fitting_elements = driver.find_elements(By.CLASS_NAME, "shipFitting")
#
#         for ship_fitting_element in ship_fitting_elements:
#             etf_button = ship_fitting_element.find_element(
#                 By.CSS_SELECTOR,
#                 "div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1)",
#             )
#             etf_button.click()
#     except:
#         print("No buttons have been found.")


def write_fittings_to_file(driver):
    try:
        ship_fitting_elements = driver.find_elements(By.CLASS_NAME, "shipFitting")

        for ship_fitting_element in ship_fitting_elements:
            etf_info = ship_fitting_element.find_element(
                By.CSS_SELECTOR,
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
            )
            with open("fittings.txt", "a") as file:
                file.write(etf_info.get_attribute("innerHTML"))
                file.write("--- --- --- ---\n")

    except:
        print("No etf elements have been found.")


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
