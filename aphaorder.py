a=int(input("Enter the number of list to be displayed:"))
name=[]
for i in range(0,a):
  names=input("Enter the name:")
  name.append(names)
print("\nElements in the list are:",name)
print("\nSorted elements in list are:")
for i in sorted(name):
 print(i)
