"""
Name: Miles Eriksen
interest.py

Problem: find monthly interest charge

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

def interest():
    annual_interest_rate = eval(input("enter the annual interest rate on your card:"))
    days_in_cycle = eval(input("enter the number of days in your billing cycle:"))
    previous_balance = eval(input("enter your previous balance:"))
    payment_amount = eval(input("enter payment amount:"))
    day_paid = eval(input("enter day of billing cycle you are paying on:"))
    net_balance = previous_balance * days_in_cycle
    payment_times_days = payment_amount * day_paid
    difference = net_balance - payment_times_days
    avg_daily_balance = difference / days_in_cycle
    monthly_interest = annual_interest_rate / 12
    monthly_interest_charge = monthly_interest * avg_daily_balance
    print(monthly_interest_charge)


interest()