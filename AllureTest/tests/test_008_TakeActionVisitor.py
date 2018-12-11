from selenium import webdriver
import unittest
from core.Links import main_url
import time


class TakeActionVisitor(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_take_action_visitor(self):
		d = self.driver
		d.get(main_url)
		time.sleep(3)
		d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[1]/div[2]/ul/li[2]/a').click()
		time.sleep(4)
		d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[1]/a/div/div').click()
		time.sleep(2)
		test = d.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[2]/div/div[2]/h1').text
		print(test)
		assert test == 'Carpool with someone'

	# def tearDown(self):
	# 	self.driver.quit()
	# 	self.driver.close()


if __name__ == "__main__":
	unittest.main()
