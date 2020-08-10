## Selenium tutorial

See the [tutorial](Tutorial) for more information.

```
# Note: Install Python 3 and poetry

$: poetry install  # install all dependencies
```

### dist

```
$: pip install dist/selenium-x.y.z-py3-none.any.whl

$: poetry-template
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### selenium

```
$: poetry run python ./selenium/runner.py
```

### tests

```
$: poetry run pytest
```

```
$: poetry run pytest --cov=selenium --cov-report=html tests
#: Note: see coverage report in htmlcov/index.html
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.  

### setup.cfg

Configure Python libraries.  

### Linters

```
$: poetry run black .
```
