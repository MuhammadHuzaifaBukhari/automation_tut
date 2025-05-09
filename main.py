from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='automation.log',
    filemode='a'
)
from selenium.common.exceptions import TimeoutException

from pages.landing_page.landingPage import test_landing_page
from pages.auth.auth import sign_in
from pages.grant_program.grantProgram import grantProgram
from pages.home.home import home

sys.path.append(r'D:\SimpliTaught QA\ST Automation11\pages\auth')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome with Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = webdriver.Chrome(service=s, options=chrome_options)

simplitaught_home_page_url = 'https://simplitaught.com/'

driver.get(simplitaught_home_page_url)
driver.maximize_window()

wait = WebDriverWait(driver, 60)
actions = ActionChains(driver)


# ----------------------Landing Page----------------------------------------#
def scrollHeight():
    return driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

def hover_over_roles(hover_roles_elements):
    for selector in hover_roles_elements:
        try:
            element = wait.until(EC.visibility_of_element_located(selector))
            # Scroll to element dynamically
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(1)  # Optional: wait a bit for any animation or lazy-load
            actions.move_to_element(element).perform()
            time.sleep(1)  # Optional: to observe the hover effect
        except Exception as e:
            print(f"An error occurred while hovering over the element: {e}")


hover_roles_elements = [
    (By.XPATH,"(//div)[28]"),
    (By.XPATH,"(//div)[36]"),
    (By.XPATH,"(//div)[44]"),
    (By.XPATH,"(//div)[52]"),

]



#------------------main landing page-------------#
#---------learn more---------#
learnMore = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='styles_bannerBtns__FYrdf'] button[class='p-button p-component p-button-info']"))).click()
time.sleep(10)

#read more/read less
try:
    # Click on "Read more..."
    read_more = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Read more...']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", read_more)
    actions.move_to_element(read_more).click().perform()
    logging.info("learn more link clicked via JavaScript.")
    time.sleep(2)

    # Click on "Read less"
    read_less = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Read less'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", read_less)
    actions.move_to_element(read_less).click().perform()
    print("Clicked 'Read less'")

    # Wait and go back if needed
    time.sleep(2)
    driver.back()

except TimeoutException:
    logging.error("Read more and read less aren't found on the page.")
except Exception as e:
    print("An error occurred:", e)

# #-------hover on roles---------#
hover_over_roles(hover_roles_elements)
#
#---------View all---------#
viewAllSubjects = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View all'])[1]"))
)
driver.execute_script("arguments[0].scrollIntoView();", viewAllSubjects)
actions.move_to_element(viewAllSubjects).click().perform()
print("Clicked 'View all'")
time.sleep(5)
# #featured Subjects(Business and Economics)
# businessEconomicsElement = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > main:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)"))
# )
# driver.execute_script("arguments[0].scrollIntoView();", businessEconomicsElement)
# actions.move_to_element(businessEconomicsElement).click().perform()
# time.sleep(5)
#
#----------main logo----------#
mainLogoElement = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='SimpliTaught']"))
)
driver.execute_script("arguments[0].scrollIntoView();", mainLogoElement)
actions.move_to_element(mainLogoElement).click().perform()
time.sleep(5)

#---------learn more about AI and ML------#
learnAiAndMlElement = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='styles_resources__list__sLorX']//a[1]"))
)
driver.execute_script("arguments[0].scrollIntoView();", learnAiAndMlElement)
actions.move_to_element(learnAiAndMlElement).click().perform()
time.sleep(5)
#close icon
closeIconElement = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='p-button-icon p-c pi pi-times']"))
)
driver.execute_script("arguments[0].scrollIntoView();", closeIconElement)
actions.move_to_element(closeIconElement).click().perform()
time.sleep(5)

test_landing_page(driver, actions, wait)
# #----------------------Sign In----------------------------------------#
sign_in(driver)
time.sleep(3)
# #----------------------Home----------------------------------------#
home(driver, actions, scrollHeight)
# #----------------------Grant Program----------------------------------------#
grantProgram(driver, actions, scrollHeight)