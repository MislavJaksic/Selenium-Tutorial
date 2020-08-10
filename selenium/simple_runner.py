import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

geckodriver_exe_path = "C:/Selenium/WebDriver/bin/geckodriver"


def main(args):
    with webdriver.Firefox(executable_path=geckodriver_exe_path) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://google.com/ncr")
        driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
        first_result = wait.until(
            presence_of_element_located((By.CSS_SELECTOR, "h3>div"))
        )
        print(first_result.get_attribute("textContent"))


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
