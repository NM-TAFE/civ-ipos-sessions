# Remember you file paths when you attempt use this file reader
# import the csv library

# Function to read data from CSV file
def read_sales_data(filename):
# Task 1: Read data from CSV file
    pass

sales_data =  read_sales_data('sales_data.csv')

# Task 2: Calculate total revenue for each product
product_revenue = {}



# Task 3: Identify the product that generated the maximum revenue
max_revenue_product = max(product_revenue, key=product_revenue.get)

# Task 4: Calculate total revenue for each day
date_revenue = {}


# Task 5: Identify the day with the highest total revenue
max_revenue_date = max(date_revenue, key=date_revenue.get)

# Task 6: Calculate total units sold for each date
product_units_sold = {}


# Task 7: Identify the product with the highest total units sold
max_units_sold_product = max(product_units_sold, key=product_units_sold.get)

# Task 8: Calculate average unit price for each product - watch out for division by zero
print("\nAverage unit price for each product:")
product_unit_price = {}


# Display results
print("Total revenue for each product:")
# code here

print("\nThe product that generated the maximum revenue:")
print(max_revenue_product)

print("\nTotal revenue for each day:")
# code here

print("\nThe day with the highest total revenue:")
print(max_revenue_date)

print("\nTotal units sold for each product:")
# code here

print("\nThe product with the highest total units sold:")
print(max_units_sold_product)

print("\nAverage unit price for each product:")
# code here