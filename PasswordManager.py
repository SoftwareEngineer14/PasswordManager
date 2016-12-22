import os

accounts = {}
AddOption = 0
AddMultipleOption = 1
RemoveOption = 2
RemoveMultipleOption = 3
RemoveAllOption = 4
ViewAllAccountsOption = 5
ViewAllServicesOption = 6
LookUpOption = 7
CheckAccountOption = 8
NumServicesOption = 9
ChangeUserNameOption = 10
ChangePasswordOption = 11
QuitOption = 12
validOptions = ["a", "am", "r", "rm", "ra", "v", "vs", "l", "ca", "gm", "cu", "cp", "q"]

def CommandOptions():
	print("--------------------------------------")
	print("Command Options:")
	print("")
	print("Enter ({0:s}-{1:s}) to add account".format(validOptions[AddOption], validOptions[AddOption].upper()))
	print("Enter ({0:s}-{1:s}) to add multiple accounts".format(validOptions[AddMultipleOption], validOptions[AddMultipleOption].upper()))
	print("Enter ({0:s}-{1:s}) to remove account".format(validOptions[RemoveOption], validOptions[RemoveOption].upper()))
	print("Enter ({0:s}-{1:s}) to remove multiple accounts".format(validOptions[RemoveMultipleOption], validOptions[RemoveMultipleOption].upper()))
	print("Enter ({0:s}-{1:s}) to remove all accounts".format(validOptions[RemoveAllOption], validOptions[RemoveAllOption].upper()))
	print("Enter ({0:s}-{1:s}) to view all accounts".format(validOptions[ViewAllAccountsOption], validOptions[ViewAllAccountsOption].upper()))
	print("Enter ({0:s}-{1:s}) to view all services".format(validOptions[ViewAllServicesOption], validOptions[ViewAllServicesOption].upper()))
	print("Enter ({0:s}-{1:s}) to look up account".format(validOptions[LookUpOption], validOptions[LookUpOption].upper()))
	print("Enter ({0:s}-{1:s}) to check if account is in accounts".format(validOptions[CheckAccountOption], validOptions[CheckAccountOption].upper()))
	print("Enter ({0:s}-{1:s}) to get number of accounts".format(validOptions[NumServicesOption], validOptions[NumServicesOption].upper()))
	print("Enter ({0:s}-{1:s}) to change username".format(validOptions[ChangeUserNameOption], validOptions[ChangeUserNameOption].upper()))
	print("Enter ({0:s}-{1:s}) to change password".format(validOptions[ChangePasswordOption], validOptions[ChangePasswordOption].upper()))
	print("Enter ({0:s}-{1:s}) to quit".format(validOptions[QuitOption], validOptions[QuitOption].upper()))
	print("--------------------------------------\n")
	
def MoveFile():
	if os.path.exists("C:\\Users\\earlj\\Desktop\\PasswordManager\\accounts.txt"):
		os.remove("accounts.txt")
	os.rename("newFile.txt", "accounts.txt")
	
def WriteAccountsToFile():
	tempFile = open("newFile.txt", "w")
	for account in accounts:
		tempFile.write(account + ";")
		tempFile.write(accounts[account][0] + ";")
		tempFile.write(accounts[account][1] + "\n")
	tempFile.close()
	
def ReadAccountsFromFile():
	if os.path.exists("C:\\Users\\earlj\\Desktop\\PasswordManager\\accounts.txt") and os.path.getsize("C:\\Users\\earlj\\Desktop\\PasswordManager\\accounts.txt") > 0:
		accountsFile = open("accounts.txt", "a+")
		accountsFile.seek(0, 0)
		lines = accountsFile.readlines()
		if len(lines) > 0:
			for line in lines:
				line = line.strip('\n')
				accountInfo = line.split(";")
				accounts[accountInfo[0]] = (accountInfo[1], accountInfo[2])
		accountsFile.close()

ReadAccountsFromFile()
CommandOptions()
userChoice = input("Enter command option> ")
userChoice = userChoice.lower()

while userChoice != validOptions[QuitOption]:
	while userChoice not in validOptions:
		print("Not a valid command option. Please enter a valid command option.")
		userChoice = input("Enter command option> ")
		userChoice = userChoice.lower()
	if userChoice == validOptions[AddOption]:
		serviceName = input("Enter service name> ")
		if serviceName in accounts:
			changeAccount = input("{0:s} account already exists. Would you like to change the user name or password for {1:s} account (y/Y)/(n/N)?".format(serviceName, serviceName))
			changeAccount = changeAccount.lower()
			if changeAccount == "y":
				changeType = input("Enter 'un' to change user name or 'pw' to change password.")
				changeType = changeType.lower()
				if changeType == "un":
					newUserName = input("Enter a new username> ")
					password = accounts[serviceName][1]
					while newUserName == "":
						newUserName = input("You entered an empty username.\nPlease enter a valid username> ")
					accounts[serviceName] = (newUserName, password)
					if accounts[serviceName] == (newUserName, password):
						print("Successfully changed account user name for {0:s} to {1:s}\n".format(serviceName, newUserName))
				elif changeType == "pw":
					userName = accounts[serviceName][0]
					newPassword = input("Enter a new password> ")
					while newPassword == "":
						newPassword = input("You entered an empty password.\nPlease enter a valid password> ")
					accounts[serviceName] = (userName, newPassword)
					if accounts[serviceName] == (userName, newPassword):
						print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
			elif changeAccount == "n":
				break
		userName = input("Enter username for {0:s} service> ".format(serviceName))
		password = input("Enter password for {0:s} service> ".format(serviceName))
		accounts[serviceName] = (userName, password)
		if accounts[serviceName] == (userName, password):
			print("Account for {0:s} successfully added to accounts list!\n".format(serviceName))
		else:
			print("Account for {0:s} could not be added to the accounts list at this time\n".format(serviceName))
	elif userChoice == validOptions[AddMultipleOption]:
		serviceName = input("Enter service name (e to end)> ")
		while serviceName != "e":
			if serviceName in accounts:
				changeAccounts = input("{0:s} account already exists. Would you like to change the user name or password for {1:s} account (y/Y)/(n/N)?".format(serviceName, serviceName))
				changeAccounts = changeAccount.lower()
				if changeAccount == "y":
					changeType = input("Enter 'un' to change user name or 'pw' to change password.")
					changeType = changeType.lower()
					if changeType == "un":
						newUserName = input("Enter a new username> ")
						password = accounts[serviceName][1]
						while newUserName == "":
							newUserName = input("You entered an empty username.\nPlease enter a valid username> ")
						accounts[serviceName] = (newUserName, password)
						if accounts[serviceName] == (newUserName, password):
							print("Successfully changed account user name for {0:s} to {1:s}\n".format(serviceName, newUserName))
					elif changeType == "pw":
						userName = accounts[serviceName][0]
						newPassword = input("Enter a new password> ")
						while newPassword == "":
							newPassword = input("You entered an empty password.\nPlease enter a valid password> ")
						accounts[serviceName] = (userName, newPassword)
						if accounts[serviceName] == (userName, newPassword):
							print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
				else:
					break
			else:
				userName = input("Enter username for {0:s} service> ".format(serviceName))
				password = input("Enter password for {0:s} service> ".format(serviceName))
				accounts[serviceName] = (userName, password)
				if accounts[serviceName] == (userName, password):
					print("Account for {0:s} successfully added to accounts list!\n".format(serviceName))
				else:
					print("Account for {0:s} could not be added to the accounts list at this time\n".format(serviceName))
			serviceName = input("Enter service name (e to end)> ")
	elif userChoice == validOptions[RemoveOption]:
		if len(accounts) <= 0:
			print("No accounts available to remove. Add accounts prior to removing them from the list.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name not in accounts list. Please enter a service that is in the accounts list.")
				serviceName = input("Enter service name> ")
			remove = input("You have choosen to remove the {0:s} account from the list! Are you sure you would like to do this (y/Y)/(n/N)? ".format(serviceName))
			remove = remove.lower()
			if remove == "y":
				del accounts[serviceName]
				if serviceName not in accounts:
					print("{0:s} account was successfully removed from the accounts list.\n".format(serviceName))
				else:
					print("Failed to remove {0:s} account from the accounts list.\n".format(serviceName))
			elif remove == "n":
				print("Account removal cancelled by user.\n")
	elif userChoice == validOptions[RemoveMultipleOption]:
		if len(accounts) <= 0:
			print("No accounts available to remove. Add accounts prior to removing them from the liset.\n")
		else:
			serviceName = input("Enter service name (e to end)> ")
			while serviceName != "e":
				while serviceName not in accounts:
					print("Service name not in accounts list. Please enter a service that is in the accounts list.")
					serviceName = input("Enter service name> ")
				remove = input("You have choosen to remove the {0:s} account from the list! Are you sure you would like to do this(y/Y)/(n/N)? ".format(serviceName))
				remove = remove.lower()
				if remove == "y":
					del accounts[serviceName]
					if serviceName not in accounts:
						print("{0:s} account was successfully removed from the accounts list.\n".format(serviceName))
					else:
						print("Failed to remove {0:s} account from the accounts list.\n".format(serviceName))
				elif remove == "n":
					print("Account removal cancelled by user.\n")
				serviceName = input("Enter service name (e to end)> ")
	elif userChoice == validOptions[RemoveAllOption]:
		if len(accounts) <= 0:
			print("No accounts available to remove. Add accounts prior to removing them from the list.\n")
		else:
			remove = input("You have choosen to remove all accounts! Are you sure you would like to do this (y/Y)/(n/N)? ")
			remove = remove.lower()
			if remove == "y":
				accounts.clear()
				if len(accounts) <= 0:
					print("All accounts have successfully been removed!\n")
				else:
					print("Not all account were successfully removed! Please try again.")
					print("{0:d} accounts were not successfully removed.\n".format(len(accounts)))
			elif remove == "n":
				print("Accounts removal cancelled by user.\n")
	elif userChoice == validOptions[ViewAllAccountsOption]:
		counter = 1
		if len(accounts) <= 0:
			print("No accounts to display! Please add accounts to view all accounts.\n")
		else:
			print("\nAll Accounts View\n")
			for account in accounts:
				print("Account {0:d}: ".format(counter))
				print("\tService: " + account)
				print("\tUser Name: " + accounts[account][0])
				print("\tPassword: " + accounts[account][1] + "\n")
				counter += 1
			counter = 1
			print("")
	elif userChoice == validOptions[ViewAllServicesOption]:
		counter = 1
		if len(accounts) <= 0:
			print("No accounts to display! Please add accounts to view all services.\n")
		else:
			print("\nAll Services View\n")
			for service in accounts:
				print("\tService {0:d}: {1:s}".format(counter, service))
				counter += 1
			counter = 1
			print("")
	elif userChoice == validOptions[LookUpOption]:
		if len(accounts) <= 0:
			print("No accounts to look-up! Please add accounts to look up account.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = accounts[serviceName][1]
			print("\t{0:s} User Name: {1:s}".format(serviceName, userName))
			print("\t{0:s} Password: {1:s}\n".format(serviceName, password))
	elif userChoice == validOptions[CheckAccountOption]:
		serviceName = input("Enter service name> ")
		if serviceName in accounts:
			print("Service name {0:s} is in the accounts list.".format(serviceName))
		else:
			print("Service name {0:s} is not in the accounts list.".format(serviceName))
	elif userChoice == validOptions[NumServicesOption]:
		print("Number of accounts: {0:d}\n".format(len(accounts)))
	elif userChoice == validOptions[ChangeUserNameOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a user name.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = input("Enter current username> ")
			password = accounts[serviceName][1]
			while userName != accounts[serviceName][0]:
				userName = input("Incorrect user name! Please enter the correct username for {0:s}".format(serviceName))
			print("User name has been verified!\n")
			newUserName = input("Enter a new username> ")
			if newUserName != "":
				accounts[serviceName] = (newUserName, password)
			if accounts[serviceName] == (newUserName, password):
				print("Successfully changed account user name for {0:s} to {1:s}\n".format(serviceName, newUserName))
	elif userChoice == validOptions[ChangePasswordOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a password.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = input("Enter current password> ")
			while password != accounts[serviceName][1]:
				password = input("Incorrect password! Please enter the correct password for {0:s}".format(serviceName))
			print("Password has been verified!\n")
			newPassword = input("Enter a new password> ")
			if newPassword != "":
				accounts[serviceName] = (userName, newPassword)
			if accounts[serviceName] == (userName, newPassword):
				print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
	CommandOptions()
	userChoice = input("Enter command option> ")
	userChoice = userChoice.lower()
	
WriteAccountsToFile()

MoveFile()
	
exit()
