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
        pass


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
