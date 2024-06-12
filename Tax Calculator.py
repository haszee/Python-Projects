'''
Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.
'''

cost = float(input('Enter the cost of the product: '))
tax =  float(input('Enter the tax rate: '))/100

final_cost = cost + cost*tax
print(final_cost)