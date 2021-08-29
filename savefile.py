print ("Welcome!")
print ("Would you like to register")
loop = True

while (loop == True):
    username = input ("username: ")
    password = input ("password: ")
    print ("register here if you don't have an account")
    username1 = input ("name: ")
    print ("this is what you use to login to the system")
    username2 = input ("username: ")
    username3 = input ("password: ")

    if (username == "rohit" and password == "rodude") :
        print ("hello and welcome " + username )
        loop = False
        loop = True

    else:
        print ("invalid username and password")

    while(loop == True):

        command = str(input(username + "{} > >"))
        if(command.lower() == "exit"):
            loop=False

        elif(command.lower() == "hi"):
            print("Hi " + username + "!")

        else:
            print ("'" + command + "' is an invalid command!")
