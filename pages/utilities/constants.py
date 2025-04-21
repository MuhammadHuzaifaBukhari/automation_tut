from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def scrollHeight():
    return browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

hover_roles_elements =[
    (By.CSS_SELECTOR, "body > div:nth-child(1) > main:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > p:nth-child(2)"),
    (By.CSS_SELECTOR, "body > div:nth-child(1) > main:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"),
    (By.CSS_SELECTOR, "body > div:nth-child(1) > main:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"),
    (By.CSS_SELECTOR, "body > div:nth-child(1) > main:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")

]

def hover_over_roles(elements):
    for selector in elements:
        try:
            element = wait.until(EC.presence_of_element_located(selector))
            actions.move_to_element(element).perform()
            time.sleep(2)  # Adjust the sleep time as needed to see the hover effect
        except Exception as e:
            print(f"An error occurred while hovering over the element: {e}")
        