
correct_username="nigam"
correct_password=12345

attempts=0
while attempts<3:
    username=input("Enter username")
    password=input("Enter login password")
    
    if (username==correct_username and password==correct_password):
        print("login succesfully")
        break
    else:
        print("username or password is \"incorrect\"\ntry again")
        
        attempts+=1
        print(f"Attempts left:{3-attempts}")
        
        if attempts==3:
            print("To many failed attempts : Acces blocked")