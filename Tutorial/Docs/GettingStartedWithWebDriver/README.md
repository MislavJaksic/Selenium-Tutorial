## [Browsers](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/)

Selenium supports:
* `Chrome`
* `Firefox`
* `Internet Explorer`
* `Opera`
* `Safari`
* `HtmlUnitDriver`

## [Third party drivers and plugins](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/third_party_drivers_and_plugins/)

Selenium plugins:
* `Mozilla GeckoDriver`
* `Google Chrome Driver`
* `Opera`
* `Microsoft Edge Driver`
* `SafariDriver`

## [Locating elements](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/locating_elements/)

```python
cheese = driver.find_element(By.ID, "cheese")  # find by ID
cheddar = cheese.find_elements_by_id("cheddar")  # find by ID in narrower scope
# ===
cheddar = driver.find_element_by_css_selector("#cheese #cheddar")

mucho_cheese = driver.find_elements_by_css_selector("#cheese li")  # find multiple
```

Recommended selection strategies:
* id: unique
* css selector: prefered over xpath
* link text: works on links only
* partial link text: works on links only

Relative locators are:
* above
* below
* toLeftOf
* toRightOf
* near

## [Performing actions on the AUT*](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/performing_actions_on_the_aut/)

Application under test or AUT.  

```python
name = "Charles"
driver.find_element(By.NAME, "name").send_keys(name)  # set element text

source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")
ActionChains(driver).drag_and_drop(source, target).perform()  # drag-an-drop

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()  # click on an element
```
