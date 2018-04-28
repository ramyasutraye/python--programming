num=raw_input()
num=int(num)
binary=bin(num)
newbinary=binary[2:]
ones=newbinary.count("1")
print ones
