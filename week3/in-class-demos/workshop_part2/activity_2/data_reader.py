# Remember you file paths when you attempt use this file reader
# import the reuseable csv library - docs at: https://docs.python.org/3/library/csv.html
import csv

# Function to read data from CSV file
def read_sales_data(filename):
    # Read data from CSV file
    sales_data =[]

    with open (filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Units Sold"] = int(row['Units Sold'])
            row["Units Price"] = float(row['Unit Price'])
            row["Total Revenue"] = float(row['Total Revenue'])
            sales_data.append(row)
    
    return sales_data

sales_data = read_sales_data('sales_data_v2.csv')
# Calculate total revenue for each product
product_revenue = {}
for sale in sales_data:
    product = sale['Product']
    revenue = sale['Total Revenue']
    product_revenue[product] = product_revenue.get(product, 0)
    
# TODO: Identify the product with the highest total units sold

# TODO: Calculate average unit price for each product - watch out for division by zero


sales_data = read_sales_data('sales_data_v2.csv')
# Display results
print("Total revenue for each product:")
for product, revenue in product_revenue.items():
    print(f"{product}: ${revenue:.2f}")

print("\nThe product with the highest total units sold:")
print(max_units_sold_product)

print("\nAverage unit price for each product:")
for product, avg_price in product_unit_price.items():
    print(f"{product}: ${avg_price:.2f}")