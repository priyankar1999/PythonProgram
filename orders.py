import csv
from collections import defaultdict
from datetime import datetime
import os

def process_orders(csv_file):
    # Initialize dictionaries to store data
    monthly_revenue = defaultdict(float)
    product_revenue = defaultdict(float)
    customer_revenue = defaultdict(float)

    # Read the CSV file and process data
    required_columns = ['order_date', 'customer_id', 'product_name', 'product_price', 'quantity']

    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            # Check if all required columns are present
            if not all(column in reader.fieldnames for column in required_columns):
                print(f"Missing required columns in the CSV file. Expected columns: {', '.join(required_columns)}")
                exit(1)

            for row in reader:
                order_date = datetime.strptime(row['order_date'], '%Y-%m-%d')

                product_price = float(row['product_price'])
                quantity = int(row['quantity'])

                # Compute monthly revenue
                month_key = f'{order_date.year}-{order_date.month:02d}'
                monthly_revenue[month_key] += product_price * quantity

                # Compute product revenue
                product_revenue[row['product_name']] += product_price * quantity

                # Compute customer revenue
                customer_revenue[row['customer_id']] += product_price * quantity

    except FileNotFoundError:
        print(f"File {csv_file} not found.")
        exit(1)

    # Return the processed data
    return monthly_revenue, product_revenue, customer_revenue

if __name__ == "__main__":
    # Use this block for any standalone execution logic if needed
    csv_file = 'orders.csv'
    monthly_revenue, product_revenue, customer_revenue = process_orders(csv_file)

    # Print results
    for month, revenue in monthly_revenue.items():
        print(f"Monthly Revenue for {month}: ${revenue:.2f}")

    for product, revenue in product_revenue.items():
        print(f"Revenue for {product}: ${revenue:.2f}")

    for customer, revenue in customer_revenue.items():
        print(f"Revenue for Customer {customer}: ${revenue:.2f}")

    # Identify the top 10 customers by revenue
    top_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:10]

    print("Top 10 Customers by Revenue:")
    for i, (customer, revenue) in enumerate(top_customers, start=1):
        print(f"{i}. Customer {customer}: ${revenue:.2f}")
