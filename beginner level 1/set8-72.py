w=raw_input()
v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
if any(char in v for char in w):
	print "yes"
else:
	print "no"
