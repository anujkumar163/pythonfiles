products = {}
#{3242:['samsung A50', 15000,20, 'Mobile', 'Jordaar Phone Hai']}
cart = []
#[3242,5432]->[]
def printoptions():
    print("1. Add Product")
    print("2. View Product")
    print("3. Add to cart")
    print("4. View cart")
    print("5. Delete cart")
    print("6. checkout")
    print("7. Logout")
    ch = int(input("Enter your choice:"))
    return ch
def addProduct():
    pid = int(input("Enter Product ID:"))
    pname = input("Enter Product Name:")
    price = float(input("Enter Price:"))
    qty = int(input("Enter stock:"))
    cat = input("Enter category:")
    desc = input("Enter Description:")

    products[pid] = [pname,price,qty,cat,desc]
    print("Product Added!")
    
def addToCart():
    pid = int(input("Enter Product ID:"))
    if pid in products.keys():
        cart.append(pid)
        print("cart updated!")
    else:
        print("Invalid Product ID!")

def Viewcart():
    for i in cart:
        if i in products.keys():
            print(products[i][0], products[i][1])

def checkout():
    tAmount = 0
    j = 1
    for i in cart:
        if i in products.keys():
            val = products[i]#[]
            print(j, val[0], val[1])
            price = val[1]
            tAmount = tAmount + price
            j += 1
            
     print("==============")
     print("Bill Amount:", tAmount)
     cart.clear()

def viewProduct():
    print(products)

while True:
    choice = printoptions()
    if choice == 1:
        addProduct()
    elif choice == 2:
        viewProduct()
    elif choice == 3:
        addTocart()
    elif choice == 4:
        Viewcart()
    elif choice == 6:
        checkout()
    elif choice == 7:
        break




















    
    



























        

        
