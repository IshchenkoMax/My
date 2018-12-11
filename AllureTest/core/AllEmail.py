import random


def get_email_from_list(file_name):
	with open(file_name, 'r') as fil:
		return random.choice(fil.readlines())


def generate_random_email(file_name):
	em = (str(random.randint(1, 19999)) + "-" + "Max!?QA@eleken.co\n")
	with open(file_name, "a") as write_file:
		write_file.write(em)
		write_file.close()
		return em
