import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_element(driver, actions, xpath, label):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    time.sleep(3)
    actions.move_to_element(element).click().perform()
    print(f"{label} clicked")
    time.sleep(3)


def home(driver, actions, scrollHeight):
    click_element(driver, actions, "//span[normalize-space()='Recently Viewed']", "Recently Viewed")
    time.sleep(2)

    click_element(driver, actions, "//span[normalize-space()='Purchased Books']", "Purchased Books")
    scrollHeight()
    time.sleep(3)