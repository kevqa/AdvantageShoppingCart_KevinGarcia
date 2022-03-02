from time import sleep
from selenium import webdriver
import datetime
import adshopcart_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'C:\Users\kevin\PycharmProjects\python_cctb\moodle_app\chromedriver.exe')

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)
    sleep(2)
    if driver.current_url == locators.adshopcart_url:
        print(f'The URL matches our data. {driver.current_url}')
        sleep(2)
    else:
        print(f'The URL does not match our data. Check your code.')
    try:
        assert 'Advantage Shopping' in driver.title
        print(f'Title matches our data!')
    except Exception as e:
        print(f'Title does not match our data. Check your code.')
        sleep(3)

def tearDown():
    if driver is not None:
        print(f'-------------------------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(1)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    sleep(0.5)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.5)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.5)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(1)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Andora')
    sleep(0.5)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.5)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(0.5)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(0.5)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
    sleep(0.5)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(2)

def name_and_cart():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(2)
    if driver.find_element(By.CLASS_NAME, 'ng-binding'):
        print(f'------------------------------------------')
        print(f'Identity detected.')
    else:
        print(f'Error. Check code.')
    sleep(0.5)
    driver.find_element(By.ID, 'menuCart').click()
    sleep(1)
    if driver.current_url == locators.cartpage_url:
        print(f'The current URL displays an empty shopping cart page.')
    else:
        print(f'Error detected. Check code')
    sleep(2)


def log_out_log_in():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='Sign out']").click()
    sleep(1)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)

def delete_account_retry_login():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(5)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    if driver.find_element(By.ID, 'signInResultMessage'):
        print(f'------------------------------------------')
        print(f'Account no longer accepted. Test passed')
    else:
        print(f'Error found. Check code.')

#----------------------------------------------------------------------------------------------------------------------#
setUp()
create_new_user()
name_and_cart()
log_out_log_in()
delete_account_retry_login()
tearDown()

