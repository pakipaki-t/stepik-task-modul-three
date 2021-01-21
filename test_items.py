# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:19:28 2021

@author: 
"""
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_check_button_basket_exist(browser):
    
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    
    assert button_basket, "button not found" 
     