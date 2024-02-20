# #EB Bill
# unit=int(input("Enter the Unit : "))

# if 



# Input the consumption units
units = float(input("Enter the number of units consumed: "))

# Define the rate slabs
rate_1 = 2.5
rate_2 = 3.5
rate_3 = 4.5
rate_4 = 5.5
rate_5 = 6.5

# Initialize the total bill
total_bill = 0

# Calculate the bill based on the rate slabs
if units <= 250:
    total_bill = units * rate_1
elif 250 < units <= 500:
    total_bill = 250 * rate_1 + (units - 250) * rate_2
elif 500 < units <= 750:
    total_bill = 250 * rate_1 + 250 * rate_2 + (units - 500) * rate_3
elif 750 < units <= 1000:
    total_bill = 250 * rate_1 + 250 * rate_2 + 250 * rate_3 + (units - 750) * rate_4
else:
    total_bill = 250 * rate_1 + 250 * rate_2 + 250 * rate_3 + 250 * rate_4 + (units - 1000) * rate_5

# Print the total bill
print(f"The total electricity bill is Rs. {total_bill:.2f}")
