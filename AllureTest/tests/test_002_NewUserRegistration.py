from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from core.AllEmail import generate_random_email
from core.Links import main_url, reg_link
from selenium.webdriver.common.by import By
from core.Links import path_to_file
from selenium import webdriver
import unittest
import time


class NewUserReg(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_new_user_reg(self):
		em = generate_random_email(path_to_file)
		d = self.driver
		wait = WebDriverWait(d, 500)
		# open main page
		d.get(main_url)
		d.implicitly_wait(4)
		d.find_element_by_xpath(reg_link).click()
		# fill the registration form
		d.find_element_by_id('fullName').send_keys('Max Ishchenko') # name
		d.find_element_by_id('email').send_keys(em)                    # email
		d.find_element_by_id('password').send_keys('12345678')         # pass

		d.find_element_by_class_name('ant-select-selection__placeholder').click() # choose the country part
		d.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[1]').click()
		d.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/button').click()
		d.find_element_by_css_selector('#root > div > div:nth-child(1) > div > div > div:nth-child(3) > div > div').click()
		time.sleep(3)
		# wait until the page is loaded
		wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Groups')))
		# check current URL
		url = d.current_url
		print(url)
		assert 'https://test.hp.dev.eleken.co/account/dashboard' in url

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
