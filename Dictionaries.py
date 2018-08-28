#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop. 
d={}
x=int(input("enter no of keys in dictionary"))
for i in range(x):
    a=int(input("press 1 for key to be number and 2 for string"))
    if a==1:
        v=int(input("enter key(num)"))
        b=int(input("press 1 for value to be number and 2 for string"))
        if b==1:
            c=int(input("enter value(num)"))
            d[v]=c
        elif b==2:
            c=input("enter value(string)")
            d[v]=c
        else:
            break
    elif a==2:
        f=input("enter key(string)")
        b=int(input("press 1 for value to be number and 2 for string"))
        if b==1:
            c=int(input("enter value(num)"))
            d[f]=c
        elif b==2:
            c=input("enter value(string)")
            d[f]=c
        else:
            break
    else:
        break
print(d)
o=int(input("press 1 for value to be shown for num key and 2 for string key"))
if o==1:
      n=int(input("enter key(num)"))
      for i in d:
                if n==i:
                    print(d[i])
elif o==2:
      v=input("enter key(string) u want to show value of")
      for i in d:
                if v==i:
                    print(d[i])
#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. 
dict={}
x1=int(input("enter no of students"))
for i in range(x1):
    a1=input("enter student name")
    dict[a1]={}
    c=int(input("enter marks scored in ds"))
    dict[a1]['ds']=c
    b=int(input("enter marks scored in adbms"))
    dict[a1]['adbms']=b
    e=int(input("enter marks scored in python"))
    dict[a1]['python']=e
print(dict)
a2=input("enter the student name u want to display the marks")
if a2 in dict:
    print(dict[a2])
    
