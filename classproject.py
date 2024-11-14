#(\n)Matthew Jones#0
#CIS261_CourseProject_phase_1(\n)#
 
from datetime import datetime
FILENAME = "employee_data.txt"

def get_dates():
    while True:
        from_date = input("Enter from date (mm/dd/yyyy): ")
        to_date = input("Enter to date (mm/dd/yyyy): ")
        try:
            # Validate date format
            datetime.strptime(from_date, '%m/%d/%Y')
            datetime.strptime(to_date, '%m/%d/%Y')
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please try again.")
            
def get_employee_info():
    from_date, to_date = get_dates()
    employee_name = input("Enter employee name: ")
    total_hours = float(input("Enter total hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    income_tax_rate = float(input("Enter income tax rate (as a percentage): ")) / 100  # Convert to decimal
    return {
        "from_date": from_date,
        "to_date": to_date,
        "employee_name": employee_name,
        "total_hours": total_hours,
        "hourly_rate": hourly_rate,
        "income_tax_rate": income_tax_rate
    }

def calculate_financials(employee):
    gross_pay = employee["total_hours"] * employee["hourly_rate"]
    income_tax = gross_pay * employee["income_tax_rate"]
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(employee, gross_pay, income_tax, net_pay):
    print(f"From Date: {employee['from_date']}")
    print(f"To Date: {employee['to_date']}")
    print(f"Employee Name: {employee['employee_name']}")
    print(f"Hours Worked: {employee['total_hours']}")
    print(f"Hourly Rate: ${employee['hourly_rate']:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {employee['income_tax_rate'] * 100:.2f}%")
    print(f"Income Taxes: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

def write_employee_info(employee):
    with open(FILENAME, "a") as file:
        file.write(f"{employee['from_date']}|{employee['to_date']}|{employee['employee_name']}|"
                   f"{employee['total_hours']}|{employee['hourly_rate']}|"
                   f"{employee['income_tax_rate']}\n")

def generate_report():
    from_date_input = input("Enter From Date for report (mm/dd/yyyy) or type 'All': ")
    if from_date_input.lower() == 'all':
        from_date_input = None
    else:
        try:
            datetime.strptime(from_date_input, '%m/%d/%Y')
        except ValueError:
            print("Invalid date format. Please enter again.")
            return

    totals = {
        "total_employees": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_net_pay": 0
    }
    
    with open(FILENAME, "r") as file:
        for line in file:
            from_date, to_date, employee_name, total_hours, hourly_rate, income_tax_rate = line.strip().split('|')
            if from_date_input and from_date != from_date_input:
                continue

            total_hours = float(total_hours)
            hourly_rate = float(hourly_rate)
            income_tax_rate = float(income_tax_rate)
            
            employee = {
                "from_date": from_date,
                "to_date": to_date,
                "employee_name": employee_name,
                "total_hours": total_hours,
                "hourly_rate": hourly_rate,
                "income_tax_rate": income_tax_rate
            }
            gross_pay, income_tax, net_pay = calculate_financials(employee)
            display_employee_info(employee, gross_pay, income_tax, net_pay)

            totals["total_employees"] += 1
            totals["total_hours"] += total_hours
            totals["total_tax"] += income_tax
            totals["total_net_pay"] += net_pay
            
    print("Total Employees:", totals["total_employees"])
    print("Total Hours:", totals["total_hours"])
    print("Total Tax:", totals["total_tax"])
    print("Total Net Pay:", totals["total_net_pay"])

def main():
    employees = []
    
    while True:
        employee_info = get_employee_info()
        employees.append(employee_info)
        write_employee_info(employee_info)
        
        if input("Do you want to add another employee? (yes/no): ").lower() != 'yes':
            break
    
    generate_report()
    
if __name__ == "__main__":
    main()
