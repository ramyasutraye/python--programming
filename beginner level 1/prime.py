num=raw_input()
num=int(num)
if num>1:
	for i in range(2,num):
		if(num%i)==0:
			print("no")
			break
		else:
			print("yes")
