import numpy as np

# This array documents the last 5 sales for each of Superstore's four cash registers.
salesArray = np.array([[150.68, 207.99, 107.88, 58.99, 60.59],
                       [20.89, 98.99, 258.62, 19.76, 101.59],
                       [70.66, 190.10, 134.54, 200.14, 15.59],
                       [10.52, 201.59, 140.55, 13.99, 45.98]])

# Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
total_sales = np.sum(salesArray)
print(f"Total sales for the store: ${total_sales:.2f}")
print("")
# Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
smallest_sale = np.min(salesArray)
largest_sale = np.max(salesArray)
print(f"Smallest sale: ${smallest_sale:.2f}")
print(f"Largest sale: ${largest_sale:.2f}")
print("")

# Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")
sales_gr_eq_100 = salesArray >= 100
print(sales_gr_eq_100)
print("")

# Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
register_sales = np.sum(salesArray, axis=1)
print("Total sales per register:")
print(register_sales)
print("")

# Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#         Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")
credit_fees = salesArray * 0.02
print("Credit card fees per sale:")
print(credit_fees)
total_fees = np.sum(credit_fees)
print(f"Total credit card fees: ${total_fees:.2f}")
print("")

# Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")
profit_array = salesArray - credit_fees
print("Profit per sale after credit card fees:")
print(profit_array)
print()

# Step 7: Print the sales only for the second and fourth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")
sales_register_2_and_4 = salesArray[[1, 3], :]
print("Sales for the second and fourth cash register:")
print(sales_register_2_and_4)
print("")

# Step 8: Superstore has added a 5th cash register whose data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89, 13.59, 107.89, 176.88, 56.78])
updated_salesArray = np.vstack([salesArray, newRegister])
print("Updated sales array with the new register:")
print(updated_salesArray)
print("")

# Step 9: Register #3 had an error and recorded its fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#         Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")
print("Sales array with error:")
print(salesArray)
salesArray[2, 3] = 20.14
print("")
print("Sales array after correction:")
print(salesArray)
