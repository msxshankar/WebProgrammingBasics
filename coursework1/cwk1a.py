# Calculating annual income based on tax

def main():  # Starts main function
    income_tax = input("Enter income tax: ")
    try:
        income_tax = float(income_tax)
        if income_tax > 0:
            if income_tax == 0:
                annual_income = round(12500, 2)
            elif income_tax <= 7500:
                annual_income = round(((income_tax / 0.2) + 12500), 2)
            elif income_tax <= 40000 and income_tax > 7500:
                annual_income = (income_tax - 7500.00) / 0.4
                annual_income += 50000.00
                annual_income = round(annual_income, 2)
            else:
                annual_income = (income_tax - 7500.00 - 40000.00) / 0.45
                annual_income += 150000.00
                annual_income = round(annual_income, 2)
            print(f'£{annual_income}')
        else:
            print("Invalid amount")

    except ValueError:
        print("Invalid amount")
