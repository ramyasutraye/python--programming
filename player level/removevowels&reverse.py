str=raw_input()
newstr=str.translate(None,"aeiouAEIOU")
revstr=newstr[::-1]
print revstr
