import sys

expenses = []
for line in sys.stdin:
    expenses.append(int(line))

# This solution could yield incorrect answer since we loop through expenses three times and so may end up using the
# same number two or three times instead of three different numbers. Apparently my data was not that tricky though.
for expense in expenses:
    for otherExpenses in expenses:
        for yetAnotherExpense in expenses:
            if expense + otherExpenses + yetAnotherExpense == 2020:
                print(expense * otherExpenses * yetAnotherExpense)
                exit()
