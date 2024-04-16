

# get user input for expense

# Write their expense to file 

# read file and summarize expenses


from expense import Expense


def main():
    print("Hello")

    expense_file_path = "expenseFile.csv"

    expense = get_user_expenses()
    budget = 2000
    print(expense)
    save_expenses_to_file(expense, expense_file_path)
    summarize_expenses(expense_file_path, budget)

    pass


# all input return string
def get_user_expenses():
    class Invalid_IndexError(Exception): pass

    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter your amount: "))
    print("You have entered {expense_name} and {expense_amount}")
    
    expense_categories = [
        "Food",
        "Housing",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("Select a category: ")
        # index of item and value of item
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")

        value_ranged = f"[1 - {len(expense_categories)}]"
        try: 
            selected_index = input(f"Enter a number {value_ranged}: ")
            
            
            if selected_index.isdigit():
                selected_index = int(selected_index) - 1 # Adjusting for 0-based indexing

                if selected_index in range(len(expense_categories)): 
                    selected_category = expense_categories[selected_index]
                    new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
                    return new_expense
                
                print("Invalid number \n Please select again!!! \n")  

            else:
                raise Invalid_IndexError()
            
        except Invalid_IndexError:
            print("Invalid number \n Please select again!!! \n")

        
#  :Expense - is type hint
def save_expenses_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    # a - append - add to file
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    


def summarize_expenses(expense_file_path, budget):
    print("summary")
    # This variable is a list of Expenses - : list[Expense] is type hint
    expenses: list[Expense] = []
    # get all the object in the file_path, append to expenses
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # strip() take the /n characters from the line
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    for key, amount in amount_by_category.items(): 
        print(f"%s: %s" % (key, amount))
        
    totalSum = sum([ex.amount for ex in expenses])
    print(f"Spent ${totalSum} this month")

    remaining_budget = budget - totalSum
    print(f"Budget remaining ${remaining_budget}")

# Only run when this file call, run directly (when this is a part of another file)
if __name__ == "__main__":
    main()