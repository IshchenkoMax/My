import unittest
from selenium import webdriver
from core.Links import main_url, path_to_file
from core.AllEmail import get_email_from_list
import time


class UserLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_user_login(self):
        d = self.driver
        email = get_email_from_list(path_to_file)
        d.get(main_url)
        time.sleep(4)
        # Login
        d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/ul/li[2]/a').click()
        d.find_element_by_id('email').send_keys(email)
        d.find_element_by_id('password').send_keys('12345678')
        d.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/button').click()
        time.sleep(5)
        url = d.current_url
        print(url)
        assert 'https://test.hp.dev.eleken.co/account/dashboard' == url

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()