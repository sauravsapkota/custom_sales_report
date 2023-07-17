# Custom Sales Report Module

This module extends the functionality of Odoo 10 to provide a custom sales report for customer-wise sales data.

## Installation

- Clone or download this repository to your local machine.
- Copy the `custom_sales_report` folder into the `addons` directory of your Odoo installation.

## Usage

1. Restart the Odoo server to load the custom module.
2. Log in to your Odoo instance with administrative privileges.
3. Go to the **Sales Reporting** menu, accessible only to the sales manager.
4. Click on **Sales Report** to open the wizard form.
5. Enter the desired **From Date**, **To Date**, and select a **Customer**.
6. Click on **Generate Report** to generate the sales report for the selected customer within the provided date range.
7. The sales report will be displayed, including the customer's sales data as per the specified format.

## Dependencies

This module depends on the following:

- Odoo 10
- Python 2.7 or higher

Please make sure you have a compatible version of Odoo and Python installed before running this module.

## License

This project is licensed under the MIT License.
