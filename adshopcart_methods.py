from time import sleep
from selenium import webdriver
import datetime
import adshopcart_locators as locators

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
        sleep(2)

def tearDown():
    if driver is not None:
        print(f'-------------------------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

#----------------------------------------------------------------------------------------------------------------------#
setUp()
tearDown()

