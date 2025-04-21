from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def click_element(driver, actions, xpath, description):
    scroll_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(2)
    actions.move_to_element(scroll_element).click().perform()
    print(f"{description} clicked")
    time.sleep(2)


def fill_contact_us_form(driver, wait):
    first_name_xpath = "//input[@placeholder='First Name']"
    last_name_xpath = "//input[@placeholder='Last Name']"
    email_xpath = "//input[@placeholder='Enter your email...']"
    query_xpath = "//textarea[@placeholder='Query...']"

    first_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, first_name_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_name_input)
    time.sleep(2)

    first_name_input.send_keys("first_name")
    driver.find_element(By.XPATH, last_name_xpath).send_keys("last_name")
    driver.find_element(By.XPATH, email_xpath).send_keys("test@gmail.com")
    driver.find_element(By.XPATH, query_xpath).send_keys("test query")
    print("Contact Us form filled successfully.")
    time.sleep(2)


def test_landing_page(driver, actions, wait):
    click_element(driver, actions, "//a[normalize-space()='Students']", "Students")
    click_element(driver, actions, "//a[normalize-space()='Educators']", "Educators")
    click_element(driver, actions, "//a[normalize-space()='Content Creators']", "Content Creators")
    click_element(driver, actions, "//a[normalize-space()='Institutions']", "Institutions")
    click_element(driver, actions, "(//a[normalize-space()='What is ST?'])[2]", "What is ST")
    click_element(driver, actions, "//a[normalize-space()='How it Works?']", "How it Works")
    click_element(driver, actions, "//div[@class='styles_footer__text__yyKoR']//a[normalize-space()='Platform']",
                  "Platform")
    click_element(driver, actions, "//div[@class='styles_footer__text__yyKoR']//a[normalize-space()='About Us']",
                  "About Us")
    click_element(driver, actions, "//a[normalize-space()='Contact Us']", "Contact Us")

    fill_contact_us_form(driver, wait)

    click_element(driver, actions, "//a[@href='/faq']", "FAQs")
    click_element(driver, actions, "//a[normalize-space()='Privacy policy']", "Privacy Policy")
    click_element(driver, actions, "//a[normalize-space()='Terms and conditions']", "Terms and Conditions")
    click_element(driver, actions, "(//a[normalize-space()='Refund policy'])[1]", "Refund Policy")
