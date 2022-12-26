import random
class GenerateSecret : 
    def __init__(self) : 
        secret = ''
        pattern = 'W&&FIW&&FI#2J09-2#73**R9E#7d@sf(ksd$kfm2^37NMNJSJNDFUWUIDQBI'
        choice = int(input("Enter length for your secret\n"))
        for data in range(choice) : 
            limit = len(pattern)-1
            index = random.randint(0,limit)
            secret = secret+pattern[index]
        print(secret,'\n')
        Main()

class Exit : 
    def __init__(self) : 
        print("Good Bye !")
        quit()

class NotFound : 
    def __init__(self) : 
        print("Option not found !\n")
        Main()

class Main : 
    def __init__(self) : 
        print("Welcome Back !")
        print("App Menu")
        print("1. Generate Secret")
        print("2. Exit")
        option = int(input("Choose an option\n"))
        if option == 1 : GenerateSecret()
        elif option == 2 : Exit()
        else : NotFound()
Main()