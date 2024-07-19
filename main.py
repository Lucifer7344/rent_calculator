# inputs
# 1. total rent
# 2. total snacks ordered
# 3. electricity bill
# 4. charge per unit
# 5. total number of flatmates

# outputs

x=int(input("Enter the total flat rent: "))
y=int(input("Enter the total snacks ordered: "))
z=int(input("Enter the total number of flatmates: "))
a=int(input("Enter the charge per unit: "))
b=int(input("Enter the electricity unit : "))
total_bill=a*b
Total=(x+y+total_bill)/z
print("The total rent per flatmate is: ",Total)
