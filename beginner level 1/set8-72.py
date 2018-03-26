word=raw_input()
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
if any(char in vowels for char in word):
	print "yes"
else:
	print "no"
