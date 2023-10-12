Flooring Install Estimator

# Program Header
print()
print('*** Deluxe Floor Estimator***')
print('This program calculates an estimate for floor installation ')
print('based on user inputs. The program prints the total cost, a ')
print('cost breakdown, and the total amount of materials and labor required.')
print('*****************************')


# Loop control variable.
keep_going = 'Y'

# Pre-defined variables.
labor = float(30.00)
upcharge = float(0.10)



# Begins the loop to calculate estimates.
while keep_going == 'Y':
    
    # Requests floor square footage and price per case from User.
    print("\n\n\nPlease type the following data and press ENTER:")
    square_feet = float(input("Square feet of flooring: "))
    case_price = float(input("Price per case of flooring: $"))
    
    
    
    # Calculates the total number of cases required 
    # and rounds to the next whole number.
    # (Whole number added to a boolean statement for the remainder.)
    total_cases = int(square_feet / 24) + (square_feet % 24 > 0)
    
    # Calculates the hours of labor required.
    total_hours = int(total_cases * 2)
    
    # Calculates the cost of the materials.
    material_cost = float(total_cases * case_price)
    
    # Calcualtes the labor cost and determines if there is an upcharge.
    # (Upcharge only if the square footage is greater than 150.)
    labor_cost = float(total_hours * labor)
    if square_feet > 150:
        labor_cost += float(labor_cost * upcharge)
    
    # Calcualtes the total cost.
    total_cost = float(material_cost + labor_cost)
    
    
    
    # Output block:
    print("\n\n\t******** HERE IS YOUR ESTIMATE ********\n")
    
    # Prints the total cases of flooring and hours of labor required.
    print("--- MATERIALS AND LABOR -----------------------\n")
    print("Number of cases of flooring required: ", total_cases, "cases")
    print("Hours of labor required:             ", total_hours, "hours\n")
    
    # Prints the cost breakdown and total cost estimate.
    print("--- COST BREAKDOWN ----------------------------\n")
    print(f"Cost of materials (flooring): ........ ${material_cost:,.2f}")
    print(f"Cost of labor: ....................... ${labor_cost:,.2f}")
    print("_______________________________________________\n")
    print(f"Floor installation TOTAL COST: ....... ${total_cost:,.2f}")
    
    # Checks if User wants to calculate another estimate.
    # ('Y' to loop, 'N' to end loop.)
    print("_______________________________________________\n")
    keep_going = input("'Would you like to run another estimate " +
                       "(Y/N)?' ")
    
# Closing Message
print('-----------------------------------------------------------')
print()
print('***Thank you for using Deluxe Floor Estimator***')
print()
print()