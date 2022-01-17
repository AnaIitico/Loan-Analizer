
# coding: utf-8
import os
import csv
from pathlib import Path

# @TODO 1 Automate the Calculations.
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Calculate the total number of loans in the list.
# Print the number of loans from the list
loan_costs_length = len(loan_costs)
print(f"The length of the loans list is: {loan_costs_length}")

# What is the total of all loans?
# @TODO: Calculate the total of all loans in the list.
# Print the total value of the loans
total_sum_of_all_loans = sum(loan_costs)
print(f"The sum of all loans is: ${total_sum_of_all_loans:.2f}")

# What is the average loan amount from the list?
# @TODO: Calculate the average loan price.
# Print the average loan amount
average_loan_amount = total_sum_of_all_loans / loan_costs_length
print(f"The average loan amount is: ${average_loan_amount:.2f}")
print("")

# @TODO 2 Analyze Loan Data
# @TODO: Calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")
print(f"Number of remaining months on the loan: {remaining_months}")
print(f"Future value of the loan: ${future_value}")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   Use the **monthly** version of the present value formula.
#   Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

minimum_required_return = .2
fair_value = future_value / (1 + (minimum_required_return / 12)) ** remaining_months
print(f"The fair value of the loan is: ${fair_value:.2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.

if fair_value > loan.get("loan_price"):
    print(f"The loan is worth at least the cost to buy it")
else:
    print(f"The loan loan is too expensive and not worth the price")
print("")


# @TODO 3 Financial Calculations
# @TODO: Perform Financial Calculations
# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    _present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    return _present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
present_value = calculate_present_value(new_loan.get("future_value"), .2, new_loan.get("remaining_months"))
print(f"The present value of the loan is: ${present_value:.2f}")
print("")


# @TODO 4 Conditional Filter
# @TODO: Conditionally filter lists of loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
key_to_find = "loan_price"
for key in loans:
    for loan_price, value in key.items():
        if key_to_find == loan_price and value < 500:
            inexpensive_loans.append(key)

# @TODO: Print the `inexpensive_loans` list
print("The inexpensive_loans list\n",  inexpensive_loans)
print('')


# @TODO 5 Save the results to csv
# @TODO: Save the results
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("challenge_files/loan_analyzer/inexpensive_loans.csv")
if not os.path.isfile(output_path):
    print(f'File {output_path} does not exist!')
    print('It will be created for you!')
print('')
# print(os.path.abspath(output_path))

# @TODO: Write the header row and each row of `loan.values()`
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
    if os.path.isfile(output_path):
        print(f'File {csvfile.name} was successfully written')
    else:
        print(f'File {output_path} was not written')