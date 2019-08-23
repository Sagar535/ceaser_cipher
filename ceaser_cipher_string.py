from ceaser_cipher_char import Ceaser_cipher_char

cs = Ceaser_cipher_char()

class Ceaser_cipher_string:
	def genCipherString(self, key, string):
		ciphered_array = []
		j = 0

		for i in range(0,len(string)):
			length = len(key)

			r = i%length

			if(r==0):
				j = 0
				ciphered_array.append(cs.genCipher(key[j],string[i]))
			else:
				ciphered_array.append(cs.genCipher(key[j],string[i]))
				j+=1

		return ''.join(ciphered_array)

	def decipherString(self, key, ciphered_string):
		array = []
		j = 0

		for i in range(0, len(ciphered_string)):
			length = len(key)

			r = i%length

			if (r==0):
				j = 0
				array.append(cs.deCipher(key[j], ciphered_string[i]))
			else:
				array.append(cs.deCipher(key[i], ciphered_string[i]))
				j += 1

		return ''.join(array)
