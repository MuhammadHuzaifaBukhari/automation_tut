from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sign_in(driver):
    wait = WebDriverWait(driver, 10)
    
    # Wait and click on the sign-in button
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "styles_signin__btn__Kbr2z")))
    sign_in_button.click()
    time.sleep(2)

    # Ensure email input is interactable and scroll into view
    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-inputtext.p-component.styles_inputStyle__Wnor9")))
    email_input.send_keys("adnan.arshad@simplitaught.com")

    # Ensure password input is interactable and scroll into view
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='8+ Characters']")))
    password_input.send_keys("admin1234")
    time.sleep(5)

    # Wait and click on the sign-in button
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Sign in']")))
    submit_button.click()
    print("Sign in successful")
    time.sleep(5)
