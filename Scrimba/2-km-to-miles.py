# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
name = input("Enter your name: ")
km = input("Enter any number in kilomethers")
miles = float(km) * 0.621
msg = f'Hi {name}.capitalize(), {km} kilometers is {miles} miles!'
print(msg)