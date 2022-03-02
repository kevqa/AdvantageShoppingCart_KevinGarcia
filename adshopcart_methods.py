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
    sleep(4)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(8)
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
    sleep(1)
    driver.refresh()
    sleep(2)

def product_check():
    if driver.page_source.find('SPEAKERS'):
        print(f'------------------------------------------')
        print(f'Hey SPEAKERS!')
    else:
        print(f'Check code, please.')
    sleep(1)
    if driver.page_source.find('TABLETS'):
        print(f'Hey TABLETS!')
    else:
        print(f'Check code, please.')
    sleep(1)
    if driver.page_source.find('LAPTOPS'):
        print(f'Hey LAPTOPS!')
    else:
        print(f'Check code, please.')
    sleep(1)
    if driver.page_source.find('MICE'):
        print(f'Hey MICE!')
    else:
        print(f'Check code, please.')
    sleep(1)
    if driver.page_source.find('HEADPHONES'):
        print(f'Hey HEADPHONES!')
    else:
        print(f'Check code, please.')
    sleep(1)

def top_checks():
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    print(f'------------------------------------------')
    print(f'Moving to CONTACT US.')
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    print(f'Moving to POPULAR ITEMS.')
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    print(f'Moving to SPECIAL OFFER.')
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
    print(f'Moving to OUR PRODUCTS.')
    sleep(2)
    if driver.page_source.find('dvantage'):
        print(f'------------------------------------------')
        print(f'Logo...dvantage, detected!')
    else:
        print(f'Check code, please.')
    sleep(1)
    if driver.page_source.find('DEMO'):
        print(f'Logo...DEMO, detected!')
    else:
        print(f'Check code, please.')
    sleep(2)

def contact_section():
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    print(f'------------------------------------------')
    print(f'Returning back to CONTACT US.')
    sleep(2)
    Select(driver.find_element(By.XPATH, "//*[@name='categoryListboxContactUs']")).select_by_visible_text('Laptops')
    sleep(2)
    Select(driver.find_element(By.XPATH, "//*[@name='productListboxContactUs']")).select_by_visible_text('HP Chromebook 14 G1(ENERGY STAR)')
    sleep(2)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(2)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(2)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(2)
    if driver.page_source.find('SPEAKERS'):
        print(f'Message has been delivered.')
        print(f'Continue Shopping button is activated')
    else:
        print(f'Error in code. Check again.')
    sleep(2)



#----------------------------------------------------------------------------------------------------------------------#
setUp()
create_new_user()
name_and_cart()
log_out_log_in()
delete_account_retry_login()
product_check()
top_checks()
contact_section()
tearDown()

