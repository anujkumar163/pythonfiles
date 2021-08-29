def decore1(anuj):
    def inner():
        b=anuj()
        multi=b*5
        return multi
    return inner
def decor(anuj):
    def inner():
        a=anuj()
        add=a+5
        return add
    return inner

def anuj():
    return 10
anuj = decor(decore1(anuj))
print(anuj())
