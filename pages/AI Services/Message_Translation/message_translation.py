from logging import exception

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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='Message_translation.log',
    filemode='a'
)
def log_and_raise_error(action_description, exception):
    logging.error(f"Failed during: {action_description} | Error: {exception}")
    raise exception

from pages.auth.auth import sign_in
sys.path.append(r'D:\SimpliTaught QA\ST Automation11\pages\auth')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome with Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


simplitaught_home_page_url = 'https://simplitaught.com/'

driver.get(simplitaught_home_page_url)
driver.maximize_window()

wait = WebDriverWait(driver, 60)
actions = ActionChains(driver)


#-----------------------Sign in------------------#
sign_in(driver)
time.sleep(5)

#---------message translation(global chat)-------#
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

try:
    chat_button = (".p-button.p-component.styles_notifyBtn__H26hJ.p-button-icon-only.p-button-text.p-button-rounded")
    wait_and_click(By.CSS_SELECTOR, chat_button, "Click chat button")
    time.sleep(5)
except Exception as e:
    logging.critical(f"error in clicking chat button: {e}")

try:
    global_chat_element = ("//span[normalize-space()='Global Chat Community']")
    wait_and_click(By.XPATH, global_chat_element, "Click global chat element")
    time.sleep(5)
except Exception as e:
    logging.critical(f"error in clicking global chat element: {e}")

try:
    # user_chat_element = ("body > div:nth-child(1) > main:nth-child(2) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
    user_chat_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > main:nth-child(2) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > span:nth-child(1)"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", user_chat_element)
    actions.move_to_element(user_chat_element).click().perform()
    time.sleep(5)
except Exception as e:
    logging.critical(f"error in finding the user to be clickable:{e}")

    type_message_element = ("//textarea[contains(@placeholder,'Message')]")
    wait_and_click("By.XPATH", type_message_element, "click to type message")
    time.sleep(1)

try:
    message_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@placeholder,'Message')]"))
    )
    message_input.send_keys("Hello, How are you?")
    time.sleep(2)
    logging.info("message typed into input box")
except(TimeoutException, WebDriverException) as e:
        log_and_raise_error("message typing into box", e)
try:
    send_message_to_user = "//*[name()='path' and contains(@d,'M16.1391 2')]"
    wait_and_click(By.XPATH, send_message_to_user, "click send button")
except Exception as e:
    logging.critical(f"send message in chat failed as {e}")


print("click enter to exit")
input()


