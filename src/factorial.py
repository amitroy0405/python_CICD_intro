# factorial.py

import time

final_list = []

class Factorial:

	def __init__(self, number):
		self.number = number

	def get_factorialValue(self, n=1):
		time.sleep(.1)
		n = 1
		for i in range(1, self.number+1):
			n = n * i
		return n

	def sum_factorial(self):
		for i in  range(self.number):
			final_list.append(self.get_factorialValue(i))
		result = sum(final_list)
		# print("Final SUM = {}".format(result))
		return result

# if __name__ == "__main__":
# 	sum_factorial()

