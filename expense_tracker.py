print("=" * 60)
print("         EXPENSE TRACKER SYSTEM")
print("             Developed by Zahid")
print("=" * 60)

name = input("Enter Your Name: ")

print(f"\nWelcome, {name}!")
print(" calculate your expenses.\n")

total = 0

num_expenses = int(input("How many expenses do you want to enter? "))

for i in range(1, num_expenses + 1):
    expense = float(input(f"Enter Expense {i}: Rs. "))
    total += expense

print("\n" + "=" * 60)
print(f"Expense Report for: {name}")
print(f"Total Spent: Rs. {total:.2f}")
print("Project Developed by Zahid")
print("=" * 60)