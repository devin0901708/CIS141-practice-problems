'''
A store charges $5 for shipping on any order under $50. 
If the order amount is $50 or more, shipping is free. 
Ask the user for the order total and print the total cost, 
including shipping.
'''
price = float(input("How much was your order? "))
shipping = price + 5
if price < 50:
    print(f"${shipping:.2f}")
else:
    print(f"${price:.2f}")
