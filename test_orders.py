import unittest
import os

from order_processing import monthly_revenue, product_revenue, customer_revenue, top_customers

class TestOrderProcessing(unittest.TestCase):

    def test_monthly_revenue(self):
        script_path = 'order_processing.py'
        csv_path = 'orders.csv'

        os.system(f'python {script_path}')

        # Check if monthly revenue dictionary is not empty
        self.assertTrue(monthly_revenue, "Monthly revenue dictionary is empty.")

        # Check if the total revenue for January 2023 is calculated correctly
        self.assertAlmostEqual(monthly_revenue['2023-01'], 110.00, places=2)

        # Check if the total revenue for February 2023 is calculated correctly
        self.assertAlmostEqual(monthly_revenue['2023-02'], 120.00, places=2)

        # Check if the total revenue for March 2023 is calculated correctly
        self.assertAlmostEqual(monthly_revenue['2023-03'], 180.00, places=2)

        # Check if the total revenue for April 2023 is calculated correctly
        self.assertAlmostEqual(monthly_revenue['2023-04'], 25.00, places=2)

        # Check if the total revenue for May 2023 is calculated correctly
        self.assertAlmostEqual(monthly_revenue['2023-05'], 90.00, places=2)

        # Add more assertions based on your specific data and calculations

    def test_product_revenue(self):
        script_path = 'order_processing.py'
        csv_path = 'orders.csv'

        os.system(f'python {script_path}')

        # Check if product revenue dictionary is not empty
        self.assertTrue(product_revenue, "Product revenue dictionary is empty.")

        # Check if the total revenue for Product_A is calculated correctly
        self.assertAlmostEqual(product_revenue['Product_A'], 330.00, places=2)

        # Check if the total revenue for Product_B is calculated correctly
        self.assertAlmostEqual(product_revenue['Product_B'], 120.00, places=2)

        # Check if the total revenue for Product_C is calculated correctly
        self.assertAlmostEqual(product_revenue['Product_C'], 150.00, places=2)

        # Add more assertions based on your specific data and calculations

    def test_customer_revenue(self):
        script_path = 'order_processing.py'
        csv_path = 'orders.csv'

        os.system(f'python {script_path}')

        # Check if customer revenue dictionary is not empty
        self.assertTrue(customer_revenue, "Customer revenue dictionary is empty.")

        # Check if the total revenue for Customer_1 is calculated correctly
        self.assertAlmostEqual(customer_revenue['Customer_1'], 330.00, places=2)

        # Check if the total revenue for Customer_2 is calculated correctly
        self.assertAlmostEqual(customer_revenue['Customer_2'], 240.00, places=2)

        # Check if the total revenue for Customer_3 is calculated correctly
        self.assertAlmostEqual(customer_revenue['Customer_3'], 300.00, places=2)

        # Add more assertions based on your specific data and calculations

    def test_top_customers(self):
        script_path = 'order_processing.py'
        csv_path = 'orders.csv'

        os.system(f'python {script_path}')

        # Check if top_customers list is not empty
        self.assertTrue(top_customers, "Top customers list is empty.")

        # Check if the top customer is calculated correctly
        self.assertEqual(top_customers[0][0], 'Customer_1')
        self.assertAlmostEqual(top_customers[0][1], 330.00, places=2)

        # Add more assertions based on your specific data and calculations

if __name__ == '__main__':
    unittest.main()
