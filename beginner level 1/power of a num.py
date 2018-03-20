i,n=raw_input().split()
if i.isdigit() and n.isdigit():
	i=int(i)
	n=int(n)
	print(i**n)
else:
	print("Invalid")
