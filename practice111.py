'''s1 = "listen"
s2 = "slient"
x = s1.replace("listen", "slient")
y = s1.replace9('s1', 's2')
print(x)
print(y)'''
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("the string are anagram.")
    else:
        print("the string aren't anagrams.")
s1 = "listen"
s2 = "slient"
check(s1, s2)
