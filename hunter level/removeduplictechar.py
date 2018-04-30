str=raw_input()
newStr = ""
for i in str:
	if i not in newStr:
		newStr = newStr + i
print newStr
