#(\n)Matthew Jones#
#CIS261_CourseProject_phase_1(\n)#
 
def get_employee_name():
    """Input and return the employee's name."""
    return input("Enter employee's name (or 'End' to finish): ")

def get_total_hours():
    """Input and return the total hours worked."""
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    """Input and return the hourly rate."""
    return float(input("Enter hourly rate: "))

def get_income_tax_rate():
    """Input and return the income tax rate as a percentage."""
    return float(input("Enter income tax rate (as a percentage): "))

def calculate_pay(total_hours, hourly_rate, tax_rate):
    """Calculate gross pay, income tax, and net pay."""
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(name, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
    """Display employee information."""
    print(f"\nEmployee Name: {name}")
    print(f"Total Hours: {total_hours}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate}%")
    print(f"Income Tax: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

def display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    """Display totals for all employees."""
    print("\n--- Summary ---")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours: {total_hours}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net_pay:.2f}\n")

def main():
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0  # Fixed the assignment here
    total_tax = 0
    total_net_pay = 0

    while True:
        name = get_employee_name()  # Removed the colon here
        if name.lower() == 'end':
            break

        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()

        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        display_employee_info(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

        total_employees += 1
        total_hours += hours
        total_gross_pay += gross_pay
        total_tax += income_tax
        total_net_pay += net_pay
 
    display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)

if __name__ == "__main__":
    main()
