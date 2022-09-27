def register():
	"""takes all the needed information of the user and registers them into the library database"""
	# todo make a registration system
	staff_id = not None  # fixme this is a test subject
	staff_passwd = not None  # fixme this is a test subject
	login(username=staff_id, user_passwd=staff_passwd)


def login(username = None, user_passwd = None) -> bool:
	"""checks the credentials of the staff against the database"""
	while True:
		if username is None and user_passwd is None:
			staff_id = input("Enter your Staff id here please: ")
			staff_passwd = input("Enter your password here: ")
			if staff_id is not None and staff_passwd is not None:
				# todo query to check the credentials of the staff against the database
				return True  # fixme if credentials verify against the database return True otherwise return false
			else:
				print("Invalid! One or more fields are empty, please input the appropriate credentials.")
		elif username is not None and user_passwd is not None:
			# todo query to directly login in the user into the database including the given credentials
			return True  # fixme this just needs nesting after the query or something


def logout():
	raise SystemExit


def staffMethods():
	pass  # todo staff methods
