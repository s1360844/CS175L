#CS175
#Jared Mishen
#Restaurant


keep_going = 'yes'

 


while keep_going == 'yes':
    vegetarian = input("Is anyone in your party vegetarian? ".lower())
    vegan = input("Is anyone in your party vegan? ".lower())
    gluten_free = input("Is anyone in your party gluten-free? ".lower())
    print("Here are your restaurant choices.")

    if(vegetarian == "yes") and (vegan == "no") and (gluten_free == "yes"):
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef’s Kitchen")

    elif(vegetarian == "yes") and (vegan == "no") and (gluten_free == "no"):
        print("Main Street Pizza")
        print("Mama's Fine Italian")
        print("Corner Café")
        print("The Chef’s Kitchen")

    elif(vegetarian == "no") and (vegan == "no") and (gluten_free == "no"):
        print("Joe’s Gourmet Burgers")
        print("Main Street Pizza Company")
        print("Mama’s Fine Italian")
        print("Corner Café")
        print("The Chef’s Kitchen")


    else:
        print("Corner Café")
        print("The Chef’s Kitchen")

 

    keep_going = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ")

   

 

