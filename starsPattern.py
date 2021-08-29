#Interviews numbers and stars pattern question:

'''rows = int(input('Enter the number of rows'))
for i in range(rows):
    for j in range(i):
        print('*', end="")
    print('')   
           
#2 same for number prient

rows=int(input('enter a numbers of rows'))
for i in range(rows):
    for j in range(i):
        print(i, end="")
    print("")'''    
#3 same but half pyramid pattern of numbers.

'''rows=int(input('enter a no. of rows'))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end="")
    print('')    
        
rows = int(input('enter a rows'))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i, end="")
    print("")'''    


#inverted pyramid pattern of numbers.
    
'''rows=6
b=0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end="")
    print('\r')'''    

#inverted Pyramid star pattern
'''rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")

rows=5
for i in range(rows+1,0,-1):
    for j in range(0, i-1):
        print(i, end="")
    print("")    


#square pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()'''




# Diamond-shaped pattern of stars
'''n = int(input('enter n values'))
for i in range(n):
    print(' '*(n-i-1)+' *'*(i+1))
for i in range(n-1):
    print(' '*(i+1)+ ' *'*(n-i-1))'''

#stars in form of A

for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0)or((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

    
for row in range(7):
    for col in range(5):
        if(col==0 or col==4) or ((row==0 or row==3) and (col>0 and col<4)):
            print("#", end="")
        else:
            print(end=" ")
    print()        
            
                  
            














