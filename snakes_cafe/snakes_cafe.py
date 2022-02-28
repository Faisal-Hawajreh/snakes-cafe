


print(
    """
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To Show your Order, type "bill" **
        ** To quit at any time, type "quit" **
        **************************************
        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears
        ***********************************
        ** What would you like to order? **
        ***********************************
    """
    )
menu = [
    "Wings","Cookies" ,"Spring Rolls",
    "Salmon","Steak","Meat Tornado","A Literal Garden",
    "Ice Cream", "Cake", "Pie",
    "Coffee", "Tea", "Unicorn Tears"]


bill = []
NewItem = []
for item in range(100):
    Order = input("> ")
    count = 1
    if(Order == "quit"):
        break
    elif(Order == "bill"):
        print("*** bill ***")
        for idx,item in enumerate(bill):
            itemNum = bill.count(item)
            if(item in bill[idx+1:]):
                continue
            else:
                print(f'{itemNum} of {item}')
        print("\n** Additional Order **")
        for idx,item in enumerate(NewItem):
            itemNum = NewItem.count(item)
            if(item in NewItem[idx+1:]):
                continue
            else:
                print(f'{itemNum} of {item}')
        if(NewItem == []):
            print("** No Additional Order **")
        print("*** Enjoy!! ***")
    elif(Order not in menu):
        print("** It does not exist in the Menu, But we will bring it for you as Additional Order! **")
        for item in NewItem:
            if(Order == item): count +=1
        print(f'\n** {count} order of {Order} have been added to Additional Order **')
        NewItem.append(Order)
    else:
        for item in bill:
            if(Order == item): count +=1
        print(f'** {count} order of {Order} have been added to your meal **')
        bill.append(Order)

