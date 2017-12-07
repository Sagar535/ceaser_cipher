class CleanFunctions:
	def remove_period(self, string):
		length = len(string)
		array_string = list(string)
		
		array_string[length-1] = ''

		string = ''.join(array_string)

		return string
