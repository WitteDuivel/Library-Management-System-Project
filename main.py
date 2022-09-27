"""
Project Name: "LIBRARY MANAGEMENT SYSTEM"
Project Author: "Vivek Chakravorty"
"""

from lmsmodules import Librarian, Staff, Student

# Here lies all the constants
WELCOME_MESSAGE = """Welcome to The Library!"""
EXIT = """ You can just type \"exit\" in given input box to exit out of the program."""
POSSIBLE_ERRORS = """
	1. Spelling mistake
	2. Invalid input
	"""

print(WELCOME_MESSAGE)

#xx todo login

def login() -> bool:
	"""This function provides the login system for logging in the user into the database."""
	librarian_or_not = input(f"Are you a librarian or other user?(librarian/user)\n{EXIT}\n").lower()
	if librarian_or_not == "librarian":
		Librarian.login()
	elif librarian_or_not == "user":
		staff_or_student = input(f"Are you a staff member or a student?(staff/student)\n{EXIT}\n").lower()
		if staff_or_student == "staff":
			Staff.login()
		elif staff_or_student == "student":
			Student.login()
		elif staff_or_student == "exit":
			raise SystemExit
	elif librarian_or_not == "exit":
		raise SystemExit


def register() -> None:
	"""This function provides the registration system for the library management system."""
	# todo make a function for an existing librarian to generate a unique one time code for any new librarian to
	#be able to register
	librarian_or_not = input(f"Are you a librarian or other user?(librarian/user)\n{EXIT}\n").lower()
	if librarian_or_not=="librarian":
		Librarian.register()
	elif librarian_or_not=="user":
		staff_or_student = input(f"Are you a staff member or a student?(staff/student)\n{EXIT}\n").lower()
		if staff_or_student=="staff":
			Staff.register()
		elif staff_or_student=="student":
			Student.register()
		elif staff_or_student=="exit":
			raise SystemExit
	elif librarian_or_not=="exit":
		raise SystemExit


while True:
	login_or_register = input(f"Do you want to login or register?(login/register)\n{EXIT}\n").lower()
	if login_or_register=="login":
		login()  # todo login system
	elif login_or_register=="register":
		pass  # todo register system
	elif login_or_register=="exit":
		raise SystemExit

