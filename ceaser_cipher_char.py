class Ceaser_cipher_char:

	def genCipher(self, key, char):
		key = key.lower()
		ASCII_key = ord(key)

		ceaser_key = ASCII_key - 96

		is_capital = False

		ASCII_char = ord(char)

		if(ASCII_char>=65 and ASCII_char<=90):
			is_capital = True

		final_value = ASCII_char + ceaser_key

		if(is_capital):
			if(final_value>90):
				final_value = final_value - 26
		else:
			if(final_value>122):
				final_value = final_value - 26

		ciphered_char = chr(final_value)

		return ciphered_char

	def deCipher(self, key, char):
		key = key.lower()
		ASCII_key = ord(key)

		ceaser_key = ASCII_key - 96

		is_capital = False

		ASCII_char = ord(char)

		if(ASCII_char>=65 and ASCII_char<=90):
			is_capital = True

		final_value = ASCII_char - ceaser_key

		if(is_capital):
			if(final_value>90):
				final_value = final_value + 26
		else:
			if(final_value>122):
				final_value = final_value + 26

		deciphered_char = chr(final_value)

		return deciphered_char
