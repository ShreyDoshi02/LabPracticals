def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input values
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_period = float(input("Enter the time period (in years): "))

interest = calculate_simple_interest(principal_amount, interest_rate, time_period)

print("\nSimple Interest:", interest)
