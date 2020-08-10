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

import data

geckodriver_exe_path = "C:/WebDriver/bin/geckodriver"


def main(args):
    with webdriver.Firefox(executable_path=geckodriver_exe_path) as driver:
        driver.get("https://wiki.eveuniversity.org/Main_Page")

        rename_pairs = data.rename_pairs
        renameables = data.renameables
        user_login(driver)

        for query in renameables:
            search(driver, query)

            links_titles = get_search_result_links_titles(driver)

            for link_title in links_titles:
                edit_page(driver, link_title, query, rename_pairs)


def user_login(driver):
    try:
        login_name = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#pt-userpage > a:nth-child(1)")
            )
        )
        time.sleep(10)
        print("Login is a success! Welcome " + login_name.text + ".")
    except:
        print("User did not login.")
        driver.quit()
        exit()


def search(driver, query):
    print("Searching for: " + query)
    query_element = driver.find_element(By.CSS_SELECTOR, "#searchInput")
    search_element = driver.find_element(By.CSS_SELECTOR, "#searchButton")

    query_element.send_keys('"' + query + '"')
    search_element.click()


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


def edit_page(driver, link_title, query, rename_pairs):
    go_ahead = get_page(driver, link_title)

    if go_ahead:
        unprotected = open_edit_page(driver)
        if unprotected:
            open_advanced_options(driver)
            open_find_and_replace(driver)
            close_advanced_options(driver)

            input_find_and_replace_data(driver, query, rename_pairs)

            summary_edit_save(driver, query, rename_pairs)


def get_page(driver, link_title):
    print("Getting page " + link_title[0] + " with title " + link_title[1])
    driver.get(link_title[0])
    try:
        WebDriverWait(driver, 15).until(EC.title_contains((link_title[1])))
        go_ahead = 1
    except:
        print("Titles do not match. Skipping.")
        go_ahead = 0

    return go_ahead


def open_edit_page(driver):
    try:
        edit_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#ca-edit > span:nth-child(1) > a:nth-child(1)")
            )
        )
        unprotected = 1
        edit_element.click()
    except:
        print("Failed to find edit_element")
        unprotected = 0

    return unprotected


def open_advanced_options(driver):
    try:
        advanced_dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "span.tab:nth-child(1) > a:nth-child(1)")
            )
        )
        advanced_dropdown_element.click()
    except:
        print("Failed to find the Advanced Button")
        driver.quit()
        exit()


def open_find_and_replace(driver):
    try:
        find_replace_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "div.group:nth-child(5) > span:nth-child(1) > a:nth-child(1)",
                )
            )
        )
        find_replace_element.click()
    except:
        print("Failed to find the Find and Replace Button")
        driver.quit()
        exit()


def close_advanced_options(driver):
    open_advanced_options(driver)


def input_find_and_replace_data(driver, query, rename_pairs):
    search_for_element = driver.find_element(
        By.CSS_SELECTOR, "#wikieditor-toolbar-replace-search"
    )
    replace_with_element = driver.find_element(
        By.CSS_SELECTOR, "#wikieditor-toolbar-replace-replace"
    )
    replace_all_element = driver.find_element(
        By.CSS_SELECTOR, "button.ui-button:nth-child(3)"
    )

    search_for_element.send_keys(query)
    replace_with_element.send_keys(rename_pairs[query])
    replace_all_element.click()


def summary_edit_save(driver, query, rename_pairs):
    summary_element = driver.find_element(By.CSS_SELECTOR, "#wpSummary")
    minor_edit_element = driver.find_element(By.CSS_SELECTOR, "#wpMinoredit")
    save_element = driver.find_element(By.CSS_SELECTOR, "#wpSave")

    summary_element.send_keys("Renamed " + query + " to " + rename_pairs[query])
    minor_edit_element.click()
    save_element.click()


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
