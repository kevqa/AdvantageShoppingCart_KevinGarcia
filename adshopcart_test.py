import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class adshopcartPositiveTestCases(unittest.Testcase):

    @staticmethod
    def Advantage_Shopping():
        methods.setUp()
        methods.create_new_user()
        methods.name_and_cart()
        methods.log_out_log_in()
        methods.delete_account_retry_login()
        methods.product_check()
        methods.top_checks()
        methods.contact_section()
        methods.tearDown()