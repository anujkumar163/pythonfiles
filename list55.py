'''fruits= ['apple','banana','cherry']
newlist =[]
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)'''

'''fruits = ['apple', 'banana','cherry']
newlist = [x for x in fruits if 'a' in x]
print(newlist)'''
'''newlist = [x for x in range(10)]
print(newlist)'''

def my_function(food):
    for x in food:
        print(x)
        
'''fruits = ['apple', 'banana', 'chery']
my_function(fruits)'''

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
