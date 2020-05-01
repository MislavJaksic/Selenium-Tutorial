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

geckodriver_exe_path = "C:/Selenium/WebDriver/bin/geckodriver"


def main(args):
    with webdriver.Firefox(executable_path=geckodriver_exe_path) as driver:
        login(driver)

        schedule(driver)

        cart(driver)


def login(driver):
    driver.get("https://www.konzum.hr/web/sign_in")
    assert "Prijava - Konzum" in driver.title

    email_element = driver.find_element(By.CSS_SELECTOR, "#spree_user_email")
    password_element = driver.find_element(By.CSS_SELECTOR, "#password")
    remember_element = driver.find_element(By.CSS_SELECTOR, "label.color-space-gray")
    login_element = driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(1)")

    email_element.send_keys("REDACTED")
    password_element.send_keys("REDACTED")
    remember_element.click()

    login_element.click()


def schedule(driver):
    driver.get("https://www.konzum.hr/web/raspolozivi-termini")
    assert "Raspoloživi termini - Konzum" in driver.title

    try:
        schedule_element = driver.find_element(
            By.CSS_SELECTOR, ".col- > h2:nth-child(1)"
        )
        if schedule_element.text == "Trenutno nema dostupnih termina":
            print("There are no available appointments.")
    except:
        print("You can schedule your pickup!")


def cart(driver):
    driver.get("https://www.konzum.hr/web/cart")
    assert "Košarica - Konzum" in driver.title

    article_elements = driver.find_elements(By.CSS_SELECTOR, "article.product-in-order")
    print("Articles in cart: " + str(len(article_elements)))
    removable_count = 0
    for article_element in article_elements:
        rightmost_element = article_element.find_element(
            By.CSS_SELECTOR,
            "div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > form:nth-child(1) > button:nth-child(4)",
        )
        if rightmost_element.text == "UKLONI":
            removable_count = removable_count + 1

    print("Removable articles in cart: " + str(removable_count))


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
