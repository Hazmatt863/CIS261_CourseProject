# pay computation
 

from typing import NewType
def input:
      input=e-name="name",e-payrate="payrate",e-hours=hours


def employee_n0=1,n0=2,n0=3,n0=3,n0=4,n0=5:
	employww_n0=input("e-name"), ("[1,2,3,4,5]"))
while employee_n0=("e-name") <11:
    overtime =0
    e_name=input(f"\nEnter Employee {employee_n0}'s Name: ")
    pay_rate=float(input("Enter Pay Rate: $"))
    hours = float(input("Enter Hours: "))

    regular_pay = hours*pay_rate

    if hours > 40:
        overtime = (hours-40)*(1.5*pay_rate)
        gross_pay = regular_pay + overtime
    else:
        gross_pay = regular_pay

    # Tax Deductions

    fed_tax = gross_pay * 0.1 
    state_tax = gross_pay*0.06
    fica = gross_pay *0.03

    #Net Pay

    net_pay = gross_pay - ( fed_tax + state_tax + fica )

    # Payroll  Details
    
    print(f"\nRegular Pay: ${regular_pay} Overtime Pay: ${overtime}, Gross Pay: ${gross_pay}, Federal Tax: ${fed_tax}, State Tax: ${state_tax}, FICA: ${fica}, Net Pay: ${net_pay} ")


    # next employee turn


    employee_n0+=1