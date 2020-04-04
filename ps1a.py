# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:12:13 2020
Part A: House hunting exercise
@author: 44773
"""

annual_salary = int(input ('Enter your annual salary:'))
portion_saved = float(input('Enter the percentage of your salary to save, as a decimal:'))
total_cost = int(input ('Enter the cost of your dream home:'))

portion_down_payment = 0.25*total_cost
monthly_salary = annual_salary/12      
monthly_savings = portion_saved * monthly_salary

current_savings = 0
r =0.04 # Return rate for investments;
no_months = 0

while current_savings < portion_down_payment:
    current_savings += monthly_savings + ((current_savings*r)/12)
    no_months += 1
print('Number of months:', no_months)



