class Binary:

	def __init__(self, text):
		self.text = text
		self.alpha = list(map(chr, range(97, 123)))
		self.ref = {x: f'{self._iterate(x)}' for x in self.alpha}
		self.ref[' '] = ' - 00100000 -'

	def _iterate(self, n):
		base = bin(self.alpha.index(n)+1)[2::]
		bincode = ''
		for i in range(5-len(base)):
			bincode += '0'
		return f'{bincode}{base}'

	def get_binary(self):
		result = []
		for i in self.text:
			if i.isupper():
				result.append(f'010{self.ref[i.lower()]}')
			else:	
				result.append(f'011{self.ref[i]}')
		return ' '.join(result)

binary = Binary("Hi I am Anvay Mayekar and I love programming")
print(binary.get_binary())