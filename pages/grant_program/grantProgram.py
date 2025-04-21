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


def grantProgram(driver, actions, scrollHeight):

    click_element(driver, actions,
                  "//a[@href='/s/dashboard']//div[@class='styles_nav_icon__d5kT9']//button[@class='p-button p-component p-button-icon-only p-button-text']//*[name()='svg']",
                  "Grant Program")
    click_element(driver, actions, "//span[normalize-space()='simpli']", "Simpli (Grant Program)")
    click_element(driver, actions, "//span[normalize-space()='Books']", "Books (Grant Program)")
    click_element(driver, actions, "//span[normalize-space()='On Rent']", "On Rent(Books(Grant Program))")
    click_element(driver, actions, "//button[@aria-label='Lifetime']", "Lifetime(Books(Grant Program))")

    click_element(driver, actions, "//span[normalize-space()='Grant History']", "Grant History (Grant Program)")
    click_element(driver, actions, "//span[normalize-space()='History of Purchases']",
                  "History of Purchases (Grant Program)")
    click_element(driver, actions, "//span[normalize-space()='My Orders']", "My Orders (Grant Program)")
    click_element(driver, actions, "//span[normalize-space()='My Wallet']", "My Wallet (Grant Program)")
