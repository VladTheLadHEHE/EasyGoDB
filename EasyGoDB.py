# This key-value database module was created by Marco El-Korashy.

"""

--Project info--

Creator:
	Marco El-Korashy
	
Creator info:
	
	Discord: TheHippyHoppyHippo#5677
	
	YouTube: TheHippyHoppyHippo
		https://www.youtube.com/channel/UCt5T20F4vB-G354Vn-Qm0rQ
		
	GitHub: @HippyHippo
		https://github.com/HippyHippo
		
	Twitter: @MarcoElKorashy
	
Project type:
	NoSQL key-value database module managed by files
	
"""

#module(s)
import os

#initialization
try:
	os.makedirs("EasyGoDB/keys")
except FileExistsError:
	pass

#exceptions

#main base exception
class DatabaseError(Exception):
	def __init__(self, msg="An error has occurred with the database."):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for an empty database
class EmptyDatabaseError(DatabaseError):
	def __init__(self, msg="There has been no keys created in the database, yet."):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for not providing a string for a key
class KeyNameError(DatabaseError):
	def __init__(self, msg="The key for the object must be a string"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for when a key does not exists
class KeyNotFoundError(DatabaseError):
	def __init__(self, msg="That key does not exists."):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for when a key already exists (for the create command)
class KeyExistsError(DatabaseError):
	def __init__(self, msg="That key already exists."):
		self.msg=msg
		super().__init__(self.msg)
		
#input exceptions

# exception for no input & base exception for input exceptions
class NoInputError(DatabaseError):
	def __init__(self, msg="You must specify a key and/or value to create"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception when no key for an object has been provided
class NoKeyError(NoInputError):
	def __init__(self, msg="You must specify a key"):
		self.msg=msg
		super().__init__(self.msg)
# exception for when no value for an object has been provided
class NoValueError(NoInputError):
	def __init__(self, msg="You must specify a value"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for no input to set
class NoInputToSet(NoInputError):
	def __init__(self, msg="You must specify a key and/or value to set"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for no input to update
class NoInputToUpdate(NoInputError):
	def __init__(self, msg="You must specify a key and/or value to update"):
		self.msg=msg
		super().__init__(self.msg)
		
#functions

#create key function
def create(key, value):
	if key==None:
		raise NoKeyError
	else:
		pass
	if value==None:
		raise NoValueError
	else:
		pass
	try:
		if isinstance(key, str):
			try:
				try:
					with open("EasyGoDB/keys/{}.txt".format(key), "x") as file:
						try:
							file.write(str(value))
						finally:
							file.close()
						print('Key "{}" with value "{}" has been created'.format(key, value))
				except FileNotFoundError:
					if FileNotFoundError:
						try:
							os.makedirs("EasyGoDB/keys/")
						except FileExistsError:
							pass
						with open("EasyGoDB/keys/{}.txt".format(key), "x") as file:
							try:
								file.write(str(value))
							finally:
								file.close()
							print('Key "{}" with value "{}" has been created'.format(key, value))
			except FileExistsError:
				if FileExistsError:
					raise KeyExistsError('The key named "{}" has already been found in the database'.format(key))
		else:
			raise KeyNameError
	except TypeError:
		if TypeError:
			raise NoInputError
			
#update key function
def update(old_key, new_key, new_value):
	if old_key==None:
		raise NoKeyError
	else:
		pass
	if new_key==None:
		raise NoKeyError
	else:
		pass
	if new_value==None:
		raise NoValueError
	else:
		pass
	try:
		if isinstance(new_key, str):
			try:
				try:
					os.rename("EasyGoDB/keys/{}.txt".format(old_key), "EasyGoDB/keys/{}.txt".format(new_key))
					try:
						open("EasyGoDB/keys/{}.txt".format(new_key), "x")
					except FileExistsError:
						if FileExistsError:
							with open("EasyGoDB/keys/{}.txt".format(new_key), "w") as file:
								try:
									file.write(str(new_value))
								finally:
									file.close()
								print('Key "{}" has been updated to "{}" with value "{}".'.format(old_key, new_key, new_value))
				except FileNotFoundError:
					if FileNotFoundError:
						try:
							os.makedirs("EasyGoDB/keys/")
						except FileExistsError:
							pass
						os.rename("EasyGoDB/keys/{}.txt".format(old_key), "EasyGoDB/keys/{}.txt".format(new_key))
						try:
							open("EasyGoDB/keys/{}.txt".format(new_key), "x")
						except FileExistsError:
							if FileExistsError:
								with open("EasyGoDB/keys/{}.txt".format(new_key), "w") as file:
									try:
										file.write(str(new_value))
									finally:
										file.close()
									print('Key "{}" has been updated to "{}" with value "{}".'.format(old_key, new_key, new_value))
			except FileNotFoundError:
				if FileNotFoundError:
					raise KeyNotFoundError('"{}" has not been found in the database'.format(old_key))
		else:
			raise KeyNameError
	except TypeError:
		if TypeError:
			raise NoInputError

#change key function
def change_key(old_key, new_key):
	if old_key==None:
		raise NoKeyError
	else:
		pass
	if new_key==None:
		raise NoValueError
	else:
		pass
	try:
		if isinstance(old_key, str) and isinstance(new_key, str):
			try:
				try:
					os.rename("EasyGoDB/keys/{}.txt".format(old_key), "EasyGoDB/keys/{}.txt".format(new_key))
					print('Key "{}" has had its name changed to "{}".'.format(old_key, new_key))
				except FileNotFoundError:
					if FileNotFoundError:
						try:
							os.makedirs("EasyGoDB/keys/")
						except FileExistsError:
							pass
						os.rename("EasyGoDB/keys/{}.txt".format(old_key), "EasyGoDB/keys/{}.txt".format(new_key))
						print('Key "{}" has had its name changed to "{}".'.format(old_key, new_key))
			except FileExistsError:
				if FileExistsError:
					os.rename("EasyGoDB/keys/{}.txt".format(old_key), "EasyGoDB/keys/{}.txt".format(new_key))
					print('Key "{}" has had its name changed to "{}".'.format(old_key, new_key))
		else:
			raise KeyNameError
	except TypeError:
		if TypeError:
			raise NoInputError
			
#change value function
def change_value(key, new_value):
	if key==None:
		raise NoKeyError
	else:
		pass
	if new_value==None:
		raise NoValueError
	else:
		pass
	try:
		if isinstance(key, str):
			try:
				try:
					try:
						open("EasyGoDB/keys/{}.txt".format(key), "x")
					except FileExistsError:
						if FileExistsError:
							with open("EasyGoDB/keys/{}.txt".format(key), "w") as file:
								try:
									file.write(str(new_value))
								finally:
									file.close()
								print('Key "{}" has had its value changed to "{}".'.format(key, new_value))
				except FileNotFoundError:
					if FileNotFoundError:
						try:
							os.makedirs("EasyGoDB/keys/")
						except FileExistsError:
							pass
						try:
							open("EasyGoDB/keys/{}.txt".format(key), "x")
						except FileExistsError:
							if FileExistsError:
								with open("EasyGoDB/keys/{}.txt".format(key), "w") as file:
									try:
										file.write(str(new_value))
									finally:
										file.close()
									print('Key "{}" has had its value changed to "{}".'.format(key, new_value))
			except FileExistsError:
				if FileExistsError:
					try:
						open("EasyGoDB/keys/{}.txt".format(key), "x")
					except FileExistsError:
						if FileExistsError:
							with open("EasyGoDB/keys/{}.txt".format(key), "w") as file:
								try:
									file.write(str(new_value))
								finally:
									file.close()
								print('Key "{}" has had its value changed to "{}".'.format(key, new_value))
		else:
			raise KeyNameError
	except TypeError:
		if TypeError:
			raise NoInputError
		
#get key function
def get(key):
	if isinstance(key, str):
		try:
			with open("EasyGoDB/keys/{}.txt".format(key), "r") as file:
				try:
					print(file.read())
					return file.read()
				finally:
					file.close()
		except FileNotFoundError:
			raise KeyNotFoundError('No such key named "{}" has been found in the database'.format(key))
	else:
		raise KeyNameError
		
#delete key function
def delete(key):
	if isinstance(key, str):
		try:
			os.remove("EasyGoDB/keys/{}.txt".format(key))
			print(key, "has been deleted from the database.")
		except FileNotFoundError:
			if FileNotFoundError:
				raise KeyNotFoundError('No such key named "{}" has been found in the database'.format(key))
	else:
		raise KeyNameError
		
# get all key objects / get-all function
def get_all():
	if os.listdir("EasyGoDB/keys") == []:
		raise EmptyDatabaseError
	else:
		for file in os.listdir("EasyGoDB/keys"):
			with open("EasyGoDB/keys/{}".format(file), "r") as key:
				try:
					print("Key:", file[:-4])
					print("Value:", key.read())
					return file and key.read()
				finally:
					key.close()
					
# delete all keys function
def delete_all():
	if os.listdir("EasyGoDB/keys") == []:
		raise EmptyDatabaseError
	else:
		for file in os.listdir("EasyGoDB/keys"):
			os.remove("EasyGoDB/keys/{}".format(file))
		print("The database has been cleared.")

#help function
def help():
	print('Easy Go Database is a key-value database created by Marco El-Korashy. It uses .txt files and the OS module to manage the database. The way this database works is that the keys are the file names of the .txt files while the values are the internal contents of the .txt files.\nUse this "import EasyGoDB as db" for a shorter module name to use when using some of the functions of this module, like typing "db.get_all()" would be much faster than typing  "EasyGoDB.get_all()".')
	# line break
	print()
	# key creator function
	print("Create key function")
	print("Syntax: EasyGoDB.create('key', value)")
	print("Example: EasyGoDB.create('iD', 27362)")
	print("Function: Creates a new key with the specified key name & value and stores it in the database")
	# line break
	print()
	# key updater function
	print("Update key function")
	print("Syntax: EasyGoDB.update('old_key', 'new_key', new_value)")
	print("Example: EasyGoDB.update('iD', 'customer_iD', 34557)")
	print("Function: Updates the specified key that was created and stored in the database.")
	# line break
	print()
	# delete key function
	print("Delete key function")
	print("Syntax: EasyGoDB.delete('key')")
	print("Example: EasyGoDB.delete('customer_iD')")
	print("Function: Deletes/removes the specified key that was created and stored in the database.")
	# line break
	print()
	# get key function
	print("Get key function")
	print("Syntax: EasyGoDB.get('key')")
	print("Example: EasyGoDB.get('customer_iD')")
	print("Function: Returns the value of the specified key that was created and stored in the database.")
	# line break
	print()
	# get all keys function
	print("Get all keys function")
	print("EasyGoDB.get_all()")
	print("Function: Returns all keys that were created and stored in the database.")
	# line break
	print()
	# get all keys function
	print("Delete all keys function")
	print("EasyGoDB.delete_all()")
	print("Function: Removes all keys that were created and stored in the database.")
	# line break
	print()
	# change key function
	print("Change key function")
	print("Syntax: EasyGoDB.change_key('old_key', 'new_key')")
	print("Example: EasyGoDB.change_key('iD', 'customer_iD')")
	print("Function: Changes the name of a key.")
	# line break
	print()
	# change value function
	print("Change value function")
	print("Syntax: EasyGoDB.change_value('key', 'new_value')")
	print("Example: EasyGoDB.change_key('customer_iD', 56643)")
	print("Function: Changes the value of a key.")