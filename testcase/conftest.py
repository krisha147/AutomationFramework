import pytest
from selenium import webdriver
from Dataset import test_data


@pytest.fixture(scope="class")
def browser_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get(test_data.Url)
    request.cls.driver = driver

    yield
    driver.close()
