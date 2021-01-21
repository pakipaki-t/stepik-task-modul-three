# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:25:12 2021

@author: 
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default = "chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default = None,
                 help = "Choose language: ru, en,....(ets)")
    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_lenguage =request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {"intl.accept_lengufges": user_lenguage})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options= options)
    elif browser_name == "firefox":
        fp= webdriver.FirefoxProfile()
        fp.set_preference()
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(FirefoxProfile = fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
