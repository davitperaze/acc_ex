# zoommer.ge add to cart

## How to use?

To run automated test you must satisfy some requirements.

Requirements:

1. Python 3 [Get it here](https://www.python.org/)
2. Allure reports [Get it here](https://docs.qameta.io/allure/#_get_started)
3. Chrome Webdriver [Get it here](https://chromedriver.chromium.org/downloads)

### Install Allure Report

To install Allure Report on Windows OS, run in CLI:

```bash
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
scoop install allure
```

For Mac OS run in terminal:

```bash
brew install allure
```

### Setup virtual environment for the project

To set up environments use commands:

```bash

# Windowws
python -m venv .env
.\env\Scripts\activate
pip install -r requirements.txt



# Mac
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt

```

## Run test

To run tests simply use `pytest` command in cli.

After test is complete, allure report starts automatically in the default browser.
If allure report fails opening, run:

```bash
allure serve reports/allure/
```

