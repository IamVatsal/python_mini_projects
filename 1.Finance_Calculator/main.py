"""
    A simple finance calculator that calculates 
    the monthly income after tax deduction and expenses.
    It takes user inputs for monthly income, tax rate, currency, and monthly expenses.
    It then calculates and prints the monthly and yearly income, tax deductions, net income, and income after expenses.
"""
from regex import P


def cal_finance(monthly_income: float, tax_rate : float, currency : str, monthly_expenses: float) -> None:
    """
        Calculate the monthly and yearly income after tax deduction and expenses.
    """
    monthly_tax_deduction: float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax_deduction
    monthly_income_after_expenses = monthly_net_income - monthly_expenses
    yearly_tax_deduction: float = monthly_tax_deduction * 12
    yearly_net_income: float = monthly_net_income * 12
    yearly_income = monthly_income * 12
    yearly_income_after_expenses = monthly_income_after_expenses * 12

    print("\n............................................................\n")
    print(f"Monthly Income: {currency} {monthly_income:,.2f}")
    print(f"Monthly Tax Deduction: {currency} {monthly_tax_deduction:,.2f}")
    print(f"Monthly Net Income: {currency} {monthly_net_income:,.2f}")
    print(f"Monthly Income After Expenses: {currency} {monthly_income_after_expenses:,.2f}\n")
    print(f"Yearly Income: {currency} {yearly_income:.2f}")
    print(f"Yearly Tax Deduction: {currency} {yearly_tax_deduction:,.2f}")
    print(f"Yearly Net Income: {currency} {yearly_net_income:,.2f}")
    print(f"Yearly Income After Expenses: {currency} {yearly_income_after_expenses:,.2f}")
    print("\n............................................................\n")

def income_input():
    """
        Get the user input for monthly income, tax rate, and currency.
    """
    while True:
        try:
            currency = input("Enter your currency: ")
            monthly_income = float(input("Enter your monthly income: "))
            tax_rate = float(input("Enter the tax rate: "))
            return monthly_income, tax_rate, currency
        except ValueError:
            print("Please enter a valid number for income, tax rate and expenses")

def expenses_input(tax):
    """
        Get the user input for monthly expenses.
    """
    while True:
        try:
            rent = float(input("\nEnter your monthly rent: "))
            utilities = float(input("Enter your monthly utilities: "))
            groceries = float(input("Enter your monthly groceries: "))
            entertainment = float(input("Enter your monthly entertainment: "))
            gym = float(input("Enter your monthly gym membership: "))
            sum = rent + utilities + groceries + entertainment + gym
            expenses = sum + sum * tax
            return expenses
        except ValueError:
            print("Please enter a valid number for income, tax rate and expenses")

def main():
    print("Welcome to the Finance Calculator")
    print("\n............................................................\n")
    try:
        monthly_income, tax_rate, currency = income_input()
        monthly_expenses = expenses_input(tax_rate)
    except UnboundLocalError:
        print("")
    try:
        cal_finance(monthly_income, tax_rate, currency, monthly_expenses)
    except UnboundLocalError:
        print("")

if __name__ == "__main__":
    main()

