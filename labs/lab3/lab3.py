"""
Name: <Miles Eriksen>
lab3.py

Problem:
Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

def average():
    avg = eval(input("How many grades are you averaging: "))
    total = 0
    for i in range(avg):
        hw = eval(input("Enter your grade on HW" + str(i) + ':'))
        total = total + hw
    average = total / avg
    print("average", average)

average()



def tip_jar():
    def tip_jar():
    donations = eval(input("How many people are donating"))
    start = 0
    for i in range(donations):
        dollars = eval(input("Enter the amount you are donating "))
        start = start + dollars


    print("total amount donated: ", start)

tip_jar()


def newton():
    x = eval(input("what is x:"))
    number = eval(input("how many times do you want to approximate:"))
    for guess in range(number):
        number = (number + (x/number))/2
    print(number)
newton()



def sequence():
    terms = eval(input("how many terms are in the number sequence"))
    for i in range(5):
        total = (i % 2)*2
    print(terms)

sequence()

def pi():
    n = eval(input("how many terms are in the series"))
    for i in range():

pi()

