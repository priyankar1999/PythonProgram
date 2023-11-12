import unittest
from unittest.mock import patch
from io import StringIO
from orders import process_orders

class TestOrderProcessing(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_monthly_revenue(self, mock_stdout):
        monthly_revenue, _, _ = process_orders('orders.csv')
        for month, revenue in monthly_revenue.items():
            print(f"Monthly Revenue for {month}: ${revenue:.2f}")

        expected_output = (
            "Monthly Revenue for 2023-05: $85.00\n"
            "Monthly Revenue for 2023-06: $65.00\n"
            "Monthly Revenue for 2023-07: $115.00\n"
            "Monthly Revenue for 2023-08: $90.00\n"
            "Monthly Revenue for 2023-09: $65.00\n"
            "Monthly Revenue for 2023-10: $70.00\n"
            "Monthly Revenue for 2023-11: $85.00\n"
            "Monthly Revenue for 2023-12: $25.00\n"
        )
        self.assertEqual(sorted(mock_stdout.getvalue().split('\n')), sorted(expected_output.split('\n')))

    @patch('sys.stdout', new_callable=StringIO)
    def test_product_revenue(self, mock_stdout):
        _, product_revenue, _ = process_orders('orders.csv')
        for product, revenue in product_revenue.items():
            print(f"Revenue for {product}: ${revenue:.2f}")

        expected_output = (
            "Revenue for Product_A: $220.00\n"
            "Revenue for Product_B: $180.00\n"
            "Revenue for Product_C: $200.00\n"
        )
        self.assertEqual(sorted(mock_stdout.getvalue().split('\n')), sorted(expected_output.split('\n')))

    @patch('sys.stdout', new_callable=StringIO)
    def test_customer_revenue(self, mock_stdout):
        _, _, customer_revenue = process_orders('orders.csv')
        for customer, revenue in customer_revenue.items():
            print(f"Revenue for Customer {customer}: ${revenue:.2f}")

        expected_output = (
            "Revenue for Customer Customer_1: $220.00\n"
            "Revenue for Customer Customer_2: $180.00\n"
            "Revenue for Customer Customer_3: $200.00\n"
        )
        self.assertEqual(sorted(mock_stdout.getvalue().split('\n')), sorted(expected_output.split('\n')))

    @patch('sys.stdout', new_callable=StringIO)
    def test_top_customers(self, mock_stdout):
        _, _, customer_revenue = process_orders('orders.csv')
        top_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:10]
        for i, (customer, revenue) in enumerate(top_customers, start=1):
            print(f"{i}. Customer {customer}: ${revenue:.2f}")

        expected_output = (
            "Top 10 Customers by Revenue:\n"
            "1. Customer Customer_1: $220.00\n"
            "2. Customer Customer_3: $200.00\n"
            "3. Customer Customer_2: $180.00"
        )
        self.assertEqual(sorted(mock_stdout.getvalue().split('\n')), sorted(expected_output.split('\n')))

if __name__ == '__main__':
    unittest.main()
