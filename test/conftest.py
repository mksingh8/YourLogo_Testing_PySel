import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    print(" *** setup code is executed")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/manishkumarsingh/Documents/browserdrivers/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="/Users/manishkumarsingh/Documents/browserdrivers/geckodriver")

    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    print(" *** yield code executed")
    driver.close()
