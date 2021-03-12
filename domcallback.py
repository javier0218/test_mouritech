# Execercise Nro. 2

from selenium import webdriver
from selenium.webdriver.common.by import By

element_driver = webdriver.Chrome()


def function_dom_child(element_driver, p_callback):
    p_callback(element_driver)

    all_children_by_css = element_driver.find_elements_by_css_selector("*")

    for children in all_children_by_css:
        function_dom_child(children, p_callback)

