import unittest
from unittest.mock import patch
from io import StringIO
import orders

class TestOrderProcessing(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_monthly_revenue(self, mock_stdout):
        orders.main()
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
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_product_revenue(self, mock_stdout):
        orders.main()
        expected_output = (
            "Revenue for Product_A: $220.00\n"
            "Revenue for Product_B: $180.00\n"
            "Revenue for Product_C: $200.00\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_customer_revenue(self, mock_stdout):
        orders.main()
        expected_output = (
            "Revenue for Customer Customer_1: $220.00\n"
            "Revenue for Customer Customer_2: $180.00\n"
            "Revenue for Customer Customer_3: $200.00\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_top_customers(self, mock_stdout):
        orders.main()
        expected_output = (
            "Top 10 Customers by Revenue:\n"
            "1. Customer Customer_1: $220.00\n"
            "2. Customer Customer_3: $200.00\n"
            "3. Customer Customer_2: $180.00\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
