Words=[]
limit=int(input("Enter the limit of words to be inserted:"))
longest=None
length=0
for i in range(limit):
   word=input("Enter the words:")
Words.append(word)
for i in Words:
	if(len(i)>length):
	  longest=i
	  length=len(i)
print("the longest word is:",longest,"and the length is:",len(longest))


