from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def getLable(text1,text2):
    driver = webdriver.Chrome('chromedriver')
    driver.get("https://www.duplichecker.com/comparison")
    element = driver.find_element_by_id("txt1")
    element.send_keys(text1)
    element = driver.find_element_by_id("txt2")
    element.send_keys(text2)
    # element = driver.find_element_by_id("fv13")
    # element.click()
    # element = driver.find_element_by_id("fv23")
    # element.click()
    element = driver.find_element_by_id("chk_broken_link")
    element.click()
    #element.send_keys(Keys.RETURN)
    #driver.close()
    driver.wait()

getLable('Hello , work hello hello','Hi Word hello hello')