# This program calculates and displays Travel Expenses
# 09/05/23
# CTI-110 P1HW2 - Travel Expenses
# Malik Graves
#
print("This program calculates and display Travel Expenses")
print('Enter your Budget:')
print('Enter your travel destination:')
print('Enter your gas budget:')
print('Enter your spendings on accommodation:')
print('Enter your budget on food:')
######### Pesudocode ########
#
# Request Information

budget = float(input('Enter your Budget:'))
destination = input('Enter your travel destination:')
gasBudget = float(input('Enter your gas budget:'))
spendingAccommodation = float(input('Enter your spendings on accommodation:'))
foodBudget = float(input('Enter your budget on food:'))
print('Enter your Budget' + 'Enter your spendings on accommodation:')
expenses = (gasBudget + spendingAccommodation + foodBudget)
displayResults = (budget - expenses) 
                     
