WDYWTD = """
Hello Librarian!
What would you like to do?
1. Overview of the Account
2. Edit Profile Data
3. Show Due Date of a Book
4. Show Reservation Status of a book
5. Calculate fine for a user
6. Take a book
7. Manage the data of the books
8. Show the borrowers records
9. Show the return records

ENTER THE CORRESPONDING NUMBER TO THE DESIRED ACTION OR TYPE 29 TO CLOSE THIS PROGRAM
"""


def register():
	"""takes all the needed information of the user and registers them into the library database"""
	# todo make a registration system
	librarian_id = not None  # fixme this is a test subject
	librarian_passwd = not None  # fixme this is a test subject
	login(username=librarian_id, user_passwd=librarian_passwd)


def login(username = None, user_passwd = None) -> bool:
	"""checks the credentials of the librarian against the database"""
	while True:
		if username is None and user_passwd is None:
			librarian_id = input("Enter your Librarian id here please: ")
			lib_passwd = input("Enter your password here: ")
			if librarian_id and lib_passwd is not None:
				# todo query to check the credentials of the librarian against the database
				return True  # fixme if credentials verify against the database return True otherwise return false
			else:
				print("Invalid! One or more fields are empty, please input the appropriate credentials.")
		elif username is not None and user_passwd is not None:
			# todo query to directly login in the user into the database including the given credentials
			return True  # fixme this just needs nesting after the query or something


def logout():
	raise SystemExit


def librarianMethods(username = None, user_passwd = None):
	"""contains all the functions associated with the librarian"""
	while True:
		try:
			global wdywtd
			wdywtd = int(input(WDYWTD))
		except TypeError:
			continue
		else:
			dict_of_actions[wdywtd](username, user_passwd)  # fixme will need to pass username and user password


def userProfileOverview(username = None, user_passwd = None):
	# todo query to give an overview to the user of its data in the database
	while True:
		try:
			now_what = int(input("what would you like to do now?\n1. Edit Profile\n2. Go Back\n29. Exit the Library"))
		except TypeError:
			print("Just Enter the corresponding number to your desired action")
			continue
		else:
			if now_what==1:
				userProfileEdit(username, user_passwd)  # fixme will need to pass username and user password


def userProfileEdit(username = None, user_passwd = None):
	# fixme query to let the user edit their profile
	pass


dict_of_actions = {1: userProfileOverview, 2: userProfileEdit}

librarianMethods()
