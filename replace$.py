string=input("Enter the string to be replaced:")
print("String before replacing:",string)
z=string[0]
replaced=z+string[1:].replace(z,"$")
print("string after replacing:",replaced)
