from selenium import webdriver
import unittest
from core.Links import main_url
import time


class RunMainPage(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_run_main_page(self):
		d = self.driver
		d.get(main_url)
		time.sleep(4)
		d.save_screenshot('/Users/Max/PycharmProjects/My/HP/screens/MainPageScreen.png')
		print(d.title)
		assert 'Handprinter' in d.title

	def tearDown(self):
		self.driver.close()
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
