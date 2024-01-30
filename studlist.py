student={}
ls={}
n=int(input("Enter the number of students:"))
for i in range(0,n):
  name=input("Enter the name of student:")
  age=input("Enter the age of student:")
  grade=input("Enter the grade of the student:")
  student[name]=[age,grade]
print(student)
