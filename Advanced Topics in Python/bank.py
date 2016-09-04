class BankAccount():
	"""Bank Account Class"""
	def withdraw():
		pass

	def deposit():
		pass

class SavingsAccount(BankAccount):
	"""SavingsAccount class"""
	def __init__(self):
		self.balance = 500
		
	def deposit(self, amount):
		self.amount = amount
		if self.amount > 0:
			self.balance += amount
			return self.balance
		else:
			return "Invalid deposit amount"
		
	def withdraw(self, amount):
	    if amount > self.balance:
	        return ("Cannot withdraw beyond the current account balance")
	    elif self.balance == 500:
	    	return "Cannot withdraw beyond the minimum account balance"
	    elif amount < 0:
	    	return "Invalid withdraw amount"
	    else:
	    	self.balance -= amount
	    	return self.balance

class CurrentAccount(BankAccount):
	"""CurrentAccount class"""
	def __init__(self):
		self.balance = 0
		
	def deposit(self, amount):
		self.amount = amount
		if self.amount < 0:
			return "Invalid deposit amount"
		else:
			self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.amount = amount
		if amount < 0:
			return "Invalid withdraw amount"
		elif amount > self.balance:
			return "Cannot withdraw beyond the current account balance"
		else:
			self.balance -= amount
		return self.balance
		