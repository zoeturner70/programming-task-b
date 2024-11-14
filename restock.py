def restock_inventory(available_items, inventory_records, current_day):

    # Creates variable called restock_units
    # Sets it to start at zero
    restock_units = 0 

    # For the first day, 
    # all items are to be restocked
    if current_day == 0:
        restock_units = 2000
        

    # Every seven days,
    # take away the available items from 2000 to work out what's to be restocked
    elif current_day % 7 == 0:
        restock_units = 2000 - available_items
        # Now it has been restocked,
        # the available items is set back to 2000
        available_items = 2000
        
    # Appends list "inventory_records" 
    # Information is added to each column 
    inventory_records += [[current_day, 0, restock_units, available_items]]




    return available_items
