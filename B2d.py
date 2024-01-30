bin_num=str(input("Enter the binary number:"))
dec_num=0
for i in bin_num:
	dec_num=dec_num*2+int(i)
print("Decimal of",bin_num,"is",dec_num)
