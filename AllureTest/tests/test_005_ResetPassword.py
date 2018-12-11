from selenium import webdriver
import unittest
from core.Links import main_url, path_to_file
from core.AllEmail import get_email_from_list
import time


class ResetPassword(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_reset_password(self):
		d = self.driver
		email = get_email_from_list(path_to_file)
		d.get(main_url)
		time.sleep(4)
		d.find_element_by_link_text('Login').click()
		d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/div/form/div[3]/a').click()
		d.find_element_by_id("email").send_keys(email)
		d.find_element_by_id("email").submit()
		time.sleep(3)
		text = d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/h1[1]/span').text
		print(text)
		assert text == 'Recovery mail sent'

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
