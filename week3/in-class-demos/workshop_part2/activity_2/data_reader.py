# Remember you file paths when you attempt use this file reader
# import the reuseable csv library - docs at: https://docs.python.org/3/library/csv.html

# Function to read data from CSV file
def read_sales_data(filename):
# Task 1: Read data from CSV file
    pass

# Task 2: Calculate total revenue for each product

# Task 3: Identify the product with the highest total units sold

# Task 4: Calculate average unit price for each product - watch out for division by zero



# Display results
print("Total revenue for each product:")
for product, revenue in product_revenue.items():
    print(f"{product}: ${revenue:.2f}")

print("\nThe product with the highest total units sold:")
print(max_units_sold_product)

print("\nAverage unit price for each product:")
for product, avg_price in product_unit_price.items():
    print(f"{product}: ${avg_price:.2f}")