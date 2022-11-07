#print("1.*Loops are great*")
#print("2.**Loops are great**")
#print("3.***Loops are great***")
#print("4.****Loops are great****")
#print("5.*****Loops are great*****")

i=0
while i < 5:
    i+= 1
    s = '*'
    print(f"{i}.{s*i}Loops are great{s*i}")