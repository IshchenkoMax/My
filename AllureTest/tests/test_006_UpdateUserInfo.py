import random
from selenium import webdriver
import unittest
from core.Links import main_url, path_to_file
from core.AllEmail import get_email_from_list
import time


class UpdateUserInfo(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_update_user_info(self):
		d = self.driver
		email = get_email_from_list(path_to_file)
		x = str(random.randint(1, 19999))
		d.get(main_url)
		time.sleep(4)
		# Login
		d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/ul/li[2]/a').click()
		d.find_element_by_id('email').send_keys(email)
		d.find_element_by_id('password').send_keys('12345678')
		d.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/button').click()
		time.sleep(4)
		# move to profile
		d.find_element_by_css_selector(
			'#root > div > div:nth-child(1) > div > div > div:nth-child(3) > div > div').click()
		time.sleep(4)
		d.find_element_by_link_text('Profile settings').click()

		# Change Name
		old_name = d.find_element_by_id('fullName').get_attribute('value')

		d.find_element_by_id('fullName').clear()
		d.find_element_by_id('fullName').send_keys(x + 'Name')
		d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[3]/div/form/button[1]').click()

		time.sleep(3)

		d.refresh()

		time.sleep(3)

		new_name = d.find_element_by_id('fullName').get_attribute('value')
		print(old_name + ' сменили на ' + new_name)
		assert old_name != new_name
		time.sleep(5)

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
