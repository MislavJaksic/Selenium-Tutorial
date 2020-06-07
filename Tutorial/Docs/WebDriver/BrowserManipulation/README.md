## [Browser manipulation](https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/)

### Browser navigation

```python
driver.get("https://selenium.dev")

driver.current_url

driver.back()

driver.forward()

driver.refresh()

driver.title
```

### Windows and tabs

```python
driver.current_window_handle


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the driver
with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))


# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')


#Close the tab or window
driver.close()

#Switch back to the old tab or window
driver.switch_to.window(original_window)


driver.quit()


# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
def tearDown(self):
    self.driver.quit()

try:
    #WebDriver code here...
finally:
    driver.quit()

with webdriver.Firefox() as driver:
  # WebDriver code here...
```

### Frames and Iframes

```python
# Store iframe web element
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

# switch to selected iframe
driver.switch_to.frame(iframe)

# Now click on button
driver.find_element(By.TAG_NAME, 'button').click()


# Switch frame by id
driver.switch_to.frame('buttonframe')

# Now, Click on the button
driver.find_element(By.TAG_NAME, 'button').click()


# Switch to the second frame
driver.switch_to.frame(1)


// Return to the top level
driver.switchTo().defaultContent();
```

### Window management

```python
# Access each dimension individually
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# Or store the dimensions and query them later
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")


driver.set_window_size(1024, 768)


# Access each dimension individually
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# Or store the dimensions and query them later
position = driver.get_window_position()
x1 = position.get('x')
y1 = position.get('y')
```

### Set window position

```python
# Move the window to the top left of the primary monitor
driver.set_window_position(0, 0)

driver.maximize_window()

driver.minimize_window()

driver.fullscreen_window()
```
