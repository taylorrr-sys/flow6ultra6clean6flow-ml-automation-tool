from selenium import webdriver
from selenium.webdriver.common.by import By

class Automator:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigate(self, url):
        self.driver.get(url)

    def click_element(self, selector):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()