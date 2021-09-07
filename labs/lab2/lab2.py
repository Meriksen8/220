"""
Name: Miles Eriksen
lab2.py
"""

import math

def sum_of_threes():
    upper_bound = eval(input("select number - "))
    x = 0
    for num in range(3,upper_bound+1, 3):
        x = x + num
        print(x)

sum_of_threes()


def muliplication_table():
    for mult_table in range (1,11):
        print(mult_table, mult_table*2, mult_table*3, mult_table*4, mult_table*5)
muliplication_table()

def triangle_area():
    a = eval(input("select number - "))
    b = eval(input("select number - "))
    c = eval(input("select number - "))
    s = (a + b + c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)

triangle_area()


def sumquares():
    first_range = eval(input("select number - "))
    last_range = eval(input("select number - "))
    x = 0
    for num in range (first_range,last_range+1, 1):
        x = x + num** 2
        print(x)

sumquares()

def power():
    base = eval(input("select number - "))
    exponent = eval(input("select number - "))
    answer = 1
    for num in range(exponent):
        answer = answer * base
    print(base,"^", exponent, "=", answer)


power()





