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
    filename='AI_Assistant.log',
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

#-------------Assistant----------------#
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
    # 1. Click assistant avatar
    assistant_xpath = ("//span[@class='styles_avatar_box__VgQtb']//div//div//div"
                       "//*[name()='svg']//*[name()='g' and contains(@clip-path,'url(#__lot')]"
                       "//*[name()='g' and contains(@clip-path,'url(#__lot')]"
                       "//*[name()='g'][5]/*[name()='g'][1]/*[name()='path'][2]")
    wait_and_click(By.XPATH, assistant_xpath, "Click assistant avatar")
    time.sleep(5)

    # 2. Click type message SVG icon
    type_message_selector = "svg[width='40px'][height='40px'][viewBox='0 -0.5 17 17']"
    wait_and_click(By.CSS_SELECTOR, type_message_selector, "Click type message SVG")
    time.sleep(2)

    # 3. Type message
    try:
        query_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Ask me?']"))
        )
        query_input.send_keys("I wanna learn medical science")
        logging.info("Message typed into input box.")
        time.sleep(2)
    except (TimeoutException, WebDriverException) as e:
        log_and_raise_error("Typing message in input box", e)

    # 4. Click send button
    send_btn_selector = ".p-button-icon.p-c.pi.pi-send"
    wait_and_click(By.CSS_SELECTOR, send_btn_selector, "Click send button")

except Exception as e:
    logging.critical(f"Unhandled exception occurred: {e}")

print("press enter to exit")
input()

