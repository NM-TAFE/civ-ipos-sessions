import csv
import random
from datetime import datetime, timedelta

# Function to generate random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Generate sample data
products = ['Product A', 'Product B', 'Product C', 'Product D']
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

sales_data = []

for _ in range(100):  # Generate 100 sales records
    date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    product = random.choice(products)
    units_sold = random.randint(1, 20)
    unit_price = round(random.uniform(10, 50), 2)
    total_revenue = round(units_sold * unit_price, 2)
    sales_data.append([date, product, units_sold, unit_price, total_revenue])

# Write data to CSV file
with open('sales_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Product', 'Units Sold', 'Unit Price', 'Total Revenue'])
    writer.writerows(sales_data)

print("Sales data generated successfully and saved to 'sales_data.csv'.")
