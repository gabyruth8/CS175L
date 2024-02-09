#CS175
#Gabriella Velasquez
#restaurant

while True:
    vegetarian = input("Is anyone in your party vegetarian? ").lower()
    vegan = input("Is anyone in your party vegan? ").lower()
    gluten_free = input("Is anyone in your party gluten-free? ").lower()

    print("\nHere are your restaurant choices:")

    if vegetarian == "no":
        if vegan == "no":
            if gluten_free == "no":
                print("Main Street Pizza Company")
                print("Corner Café")
                print("Mama's Fine Italian")
                print("The Chef's Kitchen")

    if vegetarian == "yes":
        if vegan == "no":
            if gluten_free == "no":
                print("Main Street Pizza Company")
                print("Corner Café")
                print("Mama's Fine Italian")
                print("The Chef's Kitchen")

    if vegetarian == "no":
        if vegan == "no":
            if gluten_free == "yes":
                print("Main Street Pizza Company")
                print("Corner Café")
                print("The Chef's Kitchen")

    if vegetarian == "yes":
        if vegan == "no":
            if gluten_free == "yes":
                print("Main Street Pizza Company")
                print("Corner Café")
                print("The Chef's Kitchen")

    if vegetarian == "no":
        if vegan == "yes":
            if gluten_free == "no":
                print("Corner Café")
                print("The Chef's Kitchen")

    if vegetarian == "no":
        if vegan == "yes":
            if gluten_free == "yes":
                print("Corner Café")
                print("The Chef's Kitchen")

    if vegetarian == "yes":
        if vegan == "yes":
            if gluten_free == "no":
                print("Corner Café")
                print("The Chef's Kitchen")

    if vegetarian == "yes":
        if vegan == "yes":
            if gluten_free == "yes":
                print("Corner Café")
                print("The Chef's Kitchen")

    another.search = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ").lower()
    
    if another.search != 'yes':
        break
    
                 


