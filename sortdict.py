student={}
ls={}
n=int(input("Enter the limit:"))
for i in range(0,n):
  name=input("Enter the name:")
  marks=input("Enter the marks:")
  grade=input("Enter the grade:")
  student[name]=[marks,grade]
ls=list(student.items())
s=list(student.items())
ls.sort()
print("Sorting in ascending order:",ls)
s.sort(reverse=True)
print("Sorting in descending order:",s)
a=dict(ls)
b=dict(s)
print("The sorted dictionary of ascending:",a)
print("The sorted dictionary of descending:",b)
