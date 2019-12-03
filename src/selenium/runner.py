"""
    Selenium-Tutorial.py
    ---------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from string import Template
from selenium.webdriver import Firefox

import context

url = "file:///C:/input.html"
exe_path = "C:/Selenium/WebDriver/bin/geckodriver"
output = "output.log"


def main(args):
    template = Template("//td[@data-m-label='$id']")
    data = find_elements([template.substitute(id="Date of Purchase"), template.substitute(id="My Investment"), template.substitute(id="Interest Rate"), template.substitute(id="Received Payments"), template.substitute(id="Finished")])

    data[0] = data[0][:-1]
    data[1] = list(map(lambda x: x[2:], data[1]))
    data[2] = data[2][:-1]
    data[2] = list(map(lambda x: x[:-1], data[2]))
    data[3] = list(map(lambda x: x[2:], data[3]))

    zipped = zip(data[0], data[1], data[2], data[3], data[4])
    list_of_zips = list(zipped)
    with open(output, "w") as file:
        for zipped in list_of_zips:
            file.write("$".join(zipped))
            file.write("\n")


def find_elements(xpaths):
    data = []
    with Firefox(executable_path=exe_path) as driver:
        driver.get(url)

        for xpath in xpaths:
            data.append(driver.find_elements_by_xpath(xpath))
        data = list(map(lambda x: list(map(lambda y: y.text, x)), data))

    return data


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == '__main__':
    run()
