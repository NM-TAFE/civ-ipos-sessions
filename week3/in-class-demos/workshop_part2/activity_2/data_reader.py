# Remember you file paths when you attempt use this file reader
# import the reuseable csv library - docs at: https://docs.python.org/3/library/csv.html

# Function to read data from CSV file
def read_sales_data(filename):
# Task 1: Read data from CSV file
    pass

# Task 2: Calculate total revenue for each product

# Task 3: Identify the product that generated the maximum revenue

# Task 4: Calculate total revenue for each day

# Task 5: Identify the day with the highest total revenue

# Task 6: Calculate total units sold for each date

# Task 7: Identify the product with the highest total units sold

# Task 8: Calculate average unit price for each product - watch out for division by zero

# Can we build a resusable helper function???
# def helper(dict_name, key_1, key_2):
#     # Remove spaces
#     variable_1 = key_1.replace(" ", " ")
#     variable_2 = key_2.replace(" ", " ")

#     # Create a variable with the modified string as its name
#     globals()[variable_1] = "Some value"

# Display results
print("Total revenue for each product:")
for product, revenue in product_revenue.items():
    print(f"{product}: ${revenue:.2f}")

print("\nThe product that generated the maximum revenue:")
print(max_revenue_product)

print("\nTotal revenue for each day:")
for date, revenue in date_revenue.items():
    print(f"{date}: ${revenue:.2f}")

print("\nThe day with the highest total revenue:")
print(max_revenue_date)

print("\nTotal units sold for each product:")
for date, revenue in date_revenue.items():
    print(f"{date}: ${revenue:.2f}")

print("\nThe product with the highest total units sold:")
print(max_units_sold_product)

print("\nAverage unit price for each product:")
for product, avg_price in product_unit_price.items():
    print(f"{product}: ${avg_price:.2f}")