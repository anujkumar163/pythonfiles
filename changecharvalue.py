string = input('enter string')
def change(string):
    return string[-1:] + string[1:-1] + string[:1]
print(change(string))
