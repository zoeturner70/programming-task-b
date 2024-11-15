import random

def daily_sales(available_items, inventory_records, current_day):


    # If it's is not on the 7th day 
    if current_day % 7 != 0: 
        # Sets daily sales to a random integer from 0 to 200
        daily_sales = random.randint(0, 200)
        # Works out what items are still available after the daily sales
        available_items = available_items - daily_sales
    
        # Appends list "inventory_records" 
        # Information is added to each column 
        inventory_records += [[current_day, daily_sales, 0, available_items]]



    return available_items