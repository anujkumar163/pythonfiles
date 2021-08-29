list = (1,2,3)
newlist2 = (3,4,5)
newlist = ()
for item in list:
    if item not in newlist:
        newlist.append(item)
newlist()        
