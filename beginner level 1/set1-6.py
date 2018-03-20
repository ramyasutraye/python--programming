year=raw_input()
if year.isdigit():
	year=int(year)
	if(year%4==0):
		print("yes")
	else:
		print("no")
else:
	print("Invalid input")
		
