## [Driver requirements](https://selenium.dev/documentation/en/webdriver/driver_requirements/)

Through `WebDriver`, Selenium supports:
* `Chrome`/`Chromium`
* `Firefox`
* `Internet Explorer`
* `Opera`
* `Safari`

`WebDriver` emulates user's interactions.  

### Adding Executables to your PATH

Selenium needs an executable to communicate with the browser:
1) create a folder: `C:\WebDriver\bin` or `/opt/WebDriver/bin`
2) add directory to PATH
    * `Windows`: `$: setx /m path "%path%;C:\WebDriver\bin\"`
    * `macOS` or `Linux`: `$: export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile`
3) test in command line: `$: chromium` or `$: geckodriver`

### Quick reference

Choose a `WebDriver` binary.  

### Chromium/Chrome

TODO

### Firefox

Launch `geckodriver` with a context manager.  
Instead of adding it to the PATH, you can specify the PATH programmatically.  

```python
from selenium.webdriver import Firefox

with Firefox(executable_path='/path/to/geckodriver') as driver:
   ...
```

### Edge

TODO
