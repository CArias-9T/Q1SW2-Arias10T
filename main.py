from pyscript import display

# variables for index

restaurant_name = 'Overloaded'
owner_name = 'Caleb Arias'
year_established = 2023
popular_item_price = 450.00
has_delivery = True
product_names = ['Overloaded Signature Sandwich', 'Loaded Fries', 'Baked Macaroni', 'Buffalo Chicken Wings', 'Coke Float', 'Root Beer Float']
business_hours = ['9:00 AM', '8:00 PM']
menu_prices = [450.00, 200.00, 250.00, 300.00, 80.00, 85.00] 
common_allergens = ['Dairy', 'Eggs', 'Peanuts']
tax_rate = 0.12

# displays

#header
display(f"{restaurant_name}, a restaurant by {owner_name}!", target='ownername')
display(f"• Est. {year_established} •", target='established')

#products
display(f"{product_names[0]} (Click for info)", target='productname0')
display(f"{popular_item_price} ₱", target='price0')
display(f"{product_names[1]} (Click for info)", target='productname1')
display(f"{menu_prices[1]} ₱", target='price1')
display(f"{product_names[2]} (Click for info)", target='productname2')
display(f"{menu_prices[2]} ₱", target='price2')
display(f"{product_names[3]} (Click for info)", target='productname3')
display(f"{menu_prices[3]} ₱", target='price3')
display(f"{product_names[4]} (Click for info)", target='productname4')
display(f"{menu_prices[4]} ₱", target='price4')
display(f"{product_names[5]} (Click for info)", target='productname5')
display(f"{menu_prices[5]} ₱", target='price5')

#footer

display(f"Caleb Arias | 10-Topaz | We are open around {business_hours[0]} to {business_hours[1]}!", target='footer')