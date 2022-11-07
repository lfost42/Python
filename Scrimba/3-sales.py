sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

# You sell lemonade over two weeks, the lists show number of lemonades sold per week
# Profit for each lemonade sold is $1.50
# Add the number of another day to week 2 list by capturing a number as an input
# Combine the two lists into the list called 'sales'
# Calculate/print how much you have earned on
	# Best Day
	# Worst Day
	# Separately and in total


new = float(input("How much lemonade did you sell at the end of week 2? "))
sales_w2.append(int(new))
sales = sales_w1 + sales_w2

print(f"Best Day = ${max(sales) * 1.5}")
print(f"Worst Day = ${min(sales) * 1.5}")
print(f"Combined Profit = ${(max(sales) * 1.5) + (min(sales) * 1.5)}")