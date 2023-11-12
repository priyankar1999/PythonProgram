# PythonProgram
# Online Store Order Processing

This project processes customer orders from an online store based on the provided CSV file. It calculates total revenue for each month, product, and customer, and identifies the top 10 customers by revenue.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional, for containerization)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/priyankar1999/PythonProgram.git
cd PythonProgram

Usage
Running the Main Script:
```bash
python orders.py

will process the orders from the orders.csv file and display the monthly revenue, product-wise revenue, customer-wise revenue, and top 10 customers by revenue.

Running Tests:
```bash
python -m unittest test_orders.py

Docker Support:
If you have Docker installed, you can also run the application in a container. Build the Docker image:

```bash
docker build -t PythonProgram.
Run the container:

```bash

docker run PythonProgram.
