print("WELCOME TO OUR USELESS STORE!")
print("*****************************")

item = input("what item are you purchasing? ")
price = input(f"what is the price of {item}? ")
quantity = input("how many {item} are you buying? ")


print(f"\nAdded {quantity} {item}(s) to shopping cart")
print(f"Subtotal: ${int(quantity) * float(price)}\n")