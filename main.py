favthings = {"color": "red", "food": "Burger", "movie": "Click"}

#catagory = input("Which catagory do you want to access, Color, Food, or Movies: ").lower()

    
more = False



while more == False:
    print("The catagories you have are: ")
    for key in favthings.keys():
        print(key)
    print(" \n")
    catagory = input("Which catagory do you want to access: ").lower()    

    if catagory in favthings:
        favorite_item = favthings[catagory]
        print(f"My favorite {catagory} is {favorite_item}!")
    else:
        print("Invalid category!")

        
    addnewcat = input("Would you like to add a new favorite catagories list? (y/n) ")
    if addnewcat == "y":
        newcatname = input("Enter new catagory name: ")
        nameincat = input(f"Enter your favorite for {newcatname}: ")
        favthings[newcatname] = nameincat
    else:
        print("Ok!")

    yn = input("Do you want to see another catagory?: (Y/n)").lower()
    
  
    if yn == "y":
        more = False
    else: 
        more = True    

print("All done, Thanks for using!")
print("The catagories you finished with are: ")
for key, value in favthings.items():
    print(f"{key}:{value}")
    print("\n")
