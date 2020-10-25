## [Waits](https://www.selenium.dev/documentation/en/webdriver/waits/)

WebDriver has a blocking API.  
Browsers are asynchronous in nature.  
Be conscious of race conditions.  
Waits also you to avoid race conditions.  

### Explicit wait

Don't mix explicit and implicit waits!  
Freeze until the condition resolves.  

```python
from selenium.webdriver.support.ui import WebDriverWait

driver.navigate("file:///race_condition.html")
el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_tag_name("p"))
assert el.text == "Hello from JavaScript!"
```

#### Expected conditions

Predefine, common conditions:
* alert is present
* element exists
* element is visible
* title contains
* title is
* element staleness
* visible text

### Implicit wait

Don't mix explicit and implicit waits!  
Freeze for a set amount of time.  

```python
driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
```

### FluentWait

Freeze for a set amount of time and set frequency with which to check the condition.  

```python
driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
```
