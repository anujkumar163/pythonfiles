print("--!--welcome to anuj Travel agency--!--")
import pickle
'''import os
os.system("clr")
names =["anuj", "abhay", "ajeet"]
print("original llist")
print(names)
pickle.dump(names, open("names.txt", "wb"))
names.remove("anuj")
print("changed list")
print(names)
n = pickle.load(open("names.txt", "rb"))
print("original List")
print(n)'''

def user_detail():
    n = input("enter your name")
    a = int(input("enter your age"))
user_detail()
f1 = open("userdetail", "wb")
i = []

n=input("enter your name")
a=int(input("enter your age"))
adhar=int(input("enter your adharcard no."))
i.append(n)
i.append(a)
i.append(adhar)
pickle.dump(i, f1)
print("updated!")
#print(i)
f1.close()


f2=open("userdetail", "rb")
data = pickle.load(f2)
print(data)
f2.close()
