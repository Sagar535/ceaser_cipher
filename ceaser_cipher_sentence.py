from ceaser_cipher_string import Ceaser_cipher_string
from cleanFunctions import CleanFunctions

cx = Ceaser_cipher_string()

class Ceaser_cipher_sentence:
	def genCipherSentence(self,key,sentence):
		array_sentence = sentence.split(' ')
		length = len(array_sentence)
		length1 = len(array_sentence[length-1])

		if (array_sentence[length-1][length1-1]=='.'):
			cl = CleanFunctions()
			array_sentence[length-1] = cl.remove_period(array_sentence[length-1])

		for i in range(0,length):
			array_sentence[i] = cx.genCipherString(key,array_sentence[i])

		print(' '.join(array_sentence))

csen = Ceaser_cipher_sentence()
csen.genCipherSentence('a','I hate to wait for answer.')
