from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from core.Links import main_url, path_to_file
from core.AllEmail import get_email_from_list


class Logout(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_logout(self):
		d = self.driver
		email = get_email_from_list(path_to_file)
		# open site
		d.get(main_url)
		d.implicitly_wait(5)
		d.find_element_by_link_text('Login').click()
		# Login
		d.find_element_by_id('email').send_keys(email)
		d.find_element_by_id('password').send_keys('12345678')
		d.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/button').click()
		# hover on the profile picture
		elem = d.find_element_by_css_selector('#root > div > div:nth-child(1) > div > div > div:nth-child(3) > div > div')
		ActionChains(d).move_to_element(elem).perform()

		d.find_element_by_link_text('Sign out').click()
		out = d.current_url
		print(out)
		assert out == 'https://test.hp.dev.eleken.co/account/login'

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
