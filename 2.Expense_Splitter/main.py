def cal_split(expenses: float, num_people: int, currency: str, li: list) -> None:
    """
        Calculate the expenses per person.
    """
    

    print(f"\nTotal Expenses: {currency} {expenses:,.2f}")
    print(f"Number of People: {num_people}")
    for i in range(len(li)):
        share_per_person = expenses * li[i]/100
        print(f"Expenses For person {i+1}: {currency} {share_per_person:,.2f}")

def split_input_by_persentage(num_people: int):
    """
        Get the user input for expenses per people.
    """
    print("\n")
    while true:
        li = []
        try:
            i: int = 0
            while sum(li) < 100:
                persentage = float(input(f"Enter the persentage(%) of expense for person {i+1}: "))
                li.append(persentage)
                i += 1
            return li
        except ValueError:
            print("Please enter a valid number persentage of expense per people")

def split_input():
    """
        Get the user input for expenses and number of people.
    """
    while True:
        try:
            expenses = float(input("Enter the total expenses: "))
            num_people = int(input("Enter the number of people: "))
            return expenses, num_people
        except ValueError:
            print("Please enter a valid number for expenses and number of people")

def main():
    """
    Main function to run the expense splitter.
    
    It gets user inputs for total expenses, number of people, and each person's share percentage,
    then calculates and prints the expenses per person.
    """
    print("Welcome to the Expense Splitter")
    print("\n............................................................\n")
    try:
        expenses, num_people = split_input() 
        split_list = split_input_by_persentage(num_people)
        currency = "Rs" # input("Enter your currency: ")
        cal_split(expenses, num_people, currency, split_list)
    except ValueError:
        print("Please enter a valid number for expenses and number of people")




if __name__ == "__main__":
    main()