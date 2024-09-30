###
# Project:      CalculatingMealAmount.py
# Author:       Michael Keeton
# Created:      09/29/2024
# Description:  A program that calculates the total
#               amount of a meal purchased at a restaurant.
###

def main():
    # Create lists to store meal item names & prices
    meal_item_names = []
    meal_item_prices = []
    more_items = 'Y'
    # Ask user to input meal item names & prices while more_items is 'Y'
    while more_items.upper() == 'Y':
        meal_item_names.append(input('Enter meal item name: '))
        meal_item_prices.append(float(input('Enter meal item price: ')))
        more_items = input('More items? (Y/N): ')
    
    # Calculate subtotal, sales tax, gratuity & total.
    meal_subtotal = sum(meal_item_prices)
    meal_sales_tax = meal_subtotal * 0.07
    meal_tip = meal_subtotal * 0.18
    meal_total = meal_subtotal + meal_sales_tax + meal_tip
    
    # Print receipt.
    num_items = len(meal_item_names)
    for i in range(num_items):
        print('{:s} ${:.2f}'.format(meal_item_names[i], meal_item_prices[i]))
    print('Subtotal - ${:.2f}'.format(meal_subtotal))
    print('Sales Tax - ${:.2f}'.format(meal_sales_tax))
    print('Tip - ${:.2f}'.format(meal_tip))
    print('Total - ${:.2f}'.format(meal_total))
    
main()
