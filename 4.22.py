pal = input("Enter word")
pal1 = pal.replace(" ","")
if pal1 == pal1[::-1]:
    print("ok")
else:
    print("no")
	