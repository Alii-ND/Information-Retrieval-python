from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def getLable(text1):
    driver = webdriver.Chrome('chromedriver')
    driver.get("https://www.google.com")
    element = driver.find_element_by_id("inputText1")
    element.send_keys(text1)
    element = driver.find_element_by_id("inputText2")
    element.send_keys(text2)
    element = driver.find_element_by_id("fv13")
    element.click()
    element = driver.find_element_by_id("fv23")
    element.click()
    element = driver.find_element_by_id("checkBtn")
    element.click()
    #element.send_keys(Keys.RETURN)
    #driver.close()
    driver.wait()

getLable('Hello , work hello hello','Hi Word hello hello')