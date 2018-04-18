word=raw_input()
for letter in word:
    if word.count(letter) > 1:
        a=1
        break
else:
        a=2
if a==1:
	print "No"
else:
	print "Yes"
