MENU = {"sandwich": 10, "tea": 7}

def restaurant():
    total = 0
    order = input("Order: ")

    while order != "":
        if order in MENU:
            total += MENU[order]
            print(f"{order} costs {MENU[order]}, total is {total}")
        else:
            print(f"Sorry, we are fresh out of {order} today")
    
        order = input("Order: ")

    print(f"Your total is {total:10}")

restaurant()
        
