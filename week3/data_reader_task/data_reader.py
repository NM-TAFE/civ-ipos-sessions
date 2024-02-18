import csv

# Function to read data from CSV file
def read_sales_data(filename):
# Task 1: Read data from CSV file
    sales_data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Units Sold'] = int(row['Units Sold'])
            row['Unit Price'] = float(row['Unit Price'])
            row['Total Revenue'] = float(row['Total Revenue'])
            sales_data.append(row)

    return sales_data

sales_data =  read_sales_data('sales_data.csv')

# Task 2: Calculate total revenue for each product
product_revenue = {}

for sale in sales_data:
    product = sale['Product']
    revenue = sale['Total Revenue']
    product_revenue[product] = product_revenue.get(product, 0) + revenue

# Task 3: Identify the product that generated the maximum revenue
max_revenue_product = max(product_revenue, key=product_revenue.get)

# Task 4: Calculate total revenue for each day
date_revenue = {}

for sale in sales_data:
    date = sale['Date']
    revenue = sale['Total Revenue']
    date_revenue[date] = date_revenue.get(date, 0) + revenue
# Task 5: Identify the day with the highest total revenue
max_revenue_date = max(date_revenue, key=date_revenue.get)

# Task 6: Calculate total units sold for each date
product_units_sold = {}

for sale in sales_data:
    product = sale['Product']
    units_sold = sale['Units Sold']
    product_units_sold[product] = product_units_sold.get(product, 0) + units_sold
# Task 7: Identify the product with the highest total units sold
max_units_sold_product = max(product_units_sold, key=product_units_sold.get)

# Task 8: Calculate average unit price for each product
product_unit_price
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

# print("\nAverage unit price for each product:")
# for product, avg_price in product_unit_price.items():
#     print(f"{product}: ${avg_price:.2f}")
