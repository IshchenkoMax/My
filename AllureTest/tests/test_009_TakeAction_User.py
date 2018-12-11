from selenium import webdriver
import unittest
from core.Links import main_url, path_to_file
from core.AllEmail import get_email_from_list
import time


class TakeActionUser(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_take_action_user(self):
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
		# Take Action
		# Move to Actions page
		d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/ul/li[4]/a').click()
		time.sleep(4)
		# # Press on Action
		d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[1]/a/div/div').click()
		time.sleep(4)
		# Press on "Take Action" btn
		d.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[2]/div/div[2]/div[2]/button').click()
		time.sleep(5)
		text = d.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[2]/div/div[1]/p/span').text
		print(text)
		assert text == 'Your handprint just increased!'

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
