def register():
	"""takes all the needed information of the user and registers them into the library database"""
	# todo make a registration system
	student_id = not None  # fixme this is a test subject
	student_passwd = not None  # fixme this is a test subject
	login(username=student_id, user_passwd=student_passwd)


def login(username = None, user_passwd = None) -> bool:
	"""checks the credentials of the student against the database"""
	while True:
		if username is None and user_passwd is None:
			student_id = input("Enter your Staff id here please: ")
			student_passwd = input("Enter your password here: ")
			if student_id is not None and student_passwd is not None:
				# todo query to check the credentials of the student against the database
				return True  # fixme if credentials verify against the database return True otherwise return false
			else:
				print("Invalid! One or more fields are empty, please input the appropriate credentials.")
		elif username is not None and user_passwd is not None:
			# todo query to directly login in the user into the database including the given credentials
			return True  # fixme this just needs nesting after the query or something


def logout():
	raise SystemExit


def studentMethods():
	pass  # todo student methods
