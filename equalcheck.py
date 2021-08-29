num = [1,2,3,4,4,5,6]
'''if 1 == 2:
    print(True)
else:
    print(False)
if 4==4:
    print(True)
else:
    print(False)'''

'''for i in range(len(num)-1):
    if num[i] == num[i+1]:
        print("yes")'''
for i in range(len(num)-1):
    if num[i] == 3 and num[i+1] == 3:
        print("yes")
