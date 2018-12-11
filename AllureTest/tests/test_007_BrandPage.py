from selenium import webdriver
import unittest
from core.Links import inv_code_short, inv_code
import time


class BrandPage(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_brand_page(self):
		d = self.driver
		d.get(inv_code)
		time.sleep(4)
		value = d.find_element_by_xpath('//*[@id="invitationCode"]').get_attribute('value')
		print(value)
		assert value == inv_code_short

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
