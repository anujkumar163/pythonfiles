'''x = 20
def func():
    global x
    x = 30
    print('func calling')
    print(x)
print(x)
func()
print(x)'''

'''def gensq(num):
    num = [2,3,4,5]
    if i in num:
        print(i*i) 
gensq()'''

items = [2,3,4,5]
def gensq(num):
    return num*num
m = map(gensq, item)
print(list(m))
    
