from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import sys
import logging
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='Message_translation.log',
    filemode='a'
)

def log_and_raise_error(action_description, exception):
    logging.error(f"Failed during: {action_description} | Error: {exception}")
    raise exception

def wait_and_click(by, identifier, action_desc, wait_time=10):
    try:
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((by, identifier))
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        actions.move_to_element(element).click().perform()
        logging.info(f"Successfully completed action: {action_desc}")
        return element
    except (TimeoutException, WebDriverException) as e:
        log_and_raise_error(action_desc, e)

# Setup Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Visit SimpliTaught
driver.get('https://simplitaught.com/')

# Required after import to resolve relative path
sys.path.append(r'D:\SimpliTaught QA\ST Automation11\pages\auth')
from pages.auth.auth import sign_in

# Actions and wait setup
actions = ActionChains(driver)
wait = WebDriverWait(driver, 60)

# -------- Sign In --------
sign_in(driver)
time.sleep(5)

# -------- Chat Operations --------
chat_sequence = [
    (By.CSS_SELECTOR, ".p-button.p-component.styles_notifyBtn__H26hJ.p-button-icon-only.p-button-text.p-button-rounded", "Click chat button"),
    (By.XPATH, "//span[normalize-space()='Global Chat Community']", "Click global chat element"),
]

for by, locator, desc in chat_sequence:
    try:
        wait_and_click(by, locator, desc)
        time.sleep(5)
    except Exception as e:
        logging.critical(f"{desc} failed: {e}")

# -------- Select User Chat --------
try:
    user_chat_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Erik Berglof')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", user_chat_element)
    actions.move_to_element(user_chat_element).click().perform()
    time.sleep(5)
except Exception as e:
    logging.critical(f"Error selecting user chat: {e}")

# -------- Type Message --------
try:
    message_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@placeholder,'Message')]"))
    )
    message_input.send_keys("Hello, How are you abc?")
    logging.info("Message typed successfully.")
    time.sleep(2)
except (TimeoutException, WebDriverException) as e:
    log_and_raise_error("Typing message", e)

# -------- Send Message --------
try:
    send_button_xpath = "//*[name()='path' and contains(@d,'M16.1391 2')]"
    wait_and_click(By.XPATH, send_button_xpath, "Click send button")
except Exception as e:
    logging.critical(f"Sending message failed: {e}")

# -------- Translation Flow --------
translation_flow = [
    (By.XPATH, "(//span[contains(text(),'Translate')])[9]", "Click translate button"),
    (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder'])[1]", "Open language dropdown"),
    (By.XPATH, "(//div[contains(text(),'Arabic')])[1]", "Select Arabic language"),
    (By.XPATH, "//button[@aria-label='Translate']", "Confirm translation")
]

for by, locator, desc in translation_flow:
    try:
        wait_and_click(by, locator, desc)
        time.sleep(3 if "language" in desc else 10)
    except Exception as e:
        logging.error(f"{desc} failed: {e}")

input("\nPress ENTER to exit...")

