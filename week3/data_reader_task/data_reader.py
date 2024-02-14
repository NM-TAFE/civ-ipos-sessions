import csv

# Function to read data from CSV file

# Task 1: Read data from CSV file

# Task 2: Calculate total revenue for each product

# Task 3: Identify the product that generated the maximum revenue

# Task 4: Calculate total revenue for each day

# Task 5: Identify the day with the highest total revenue

# Task 6: Calculate total units sold for each product


# Task 7: Identify the product with the highest total units sold

# Task 8: Calculate average unit price for each product

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
for product, units_sold in product_units_sold.items():
    print(f"{product}: {units_sold}")

print("\nThe product with the highest total units sold:")
print(max_units_sold_product)

print("\nAverage unit price for each product:")
for product, avg_price in product_unit_price.items():
    print(f"{product}: ${avg_price:.2f}")
