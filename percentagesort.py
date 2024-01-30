student=[]
n=int(input("Enter the limit:"))
Total=int(input("Enter the total no of classes:"))
for i in range(n):
     name=input("Enter the name of student:")
     a=int(input("Enter the no of classes present:"))
     percent=(a/Total)*100
     student.append([percent,name])
student.sort()
print(student)


