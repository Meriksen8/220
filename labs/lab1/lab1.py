"""
Name: <Miles Eriksen>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print ("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the shots: "))
    made_shots = eval(input("Enter the shots: "))
    shooting_percentage = made_shots/total_shots
    print ("Shooting_percentage", shooting_percentage)

def coffee():
    cost = eval(input("Enter the pounds: "))
    shipping = eval(input("Enter the pounds: "))
    overhead = eval(input("Enter the price: "))
    coffee = 10.50 * cost + 0.86 * shipping + overhead
    print ("coffee", coffee)


def kilometers_to_miles():
    miles = eval(input("Enter the miles: "))
    kilometers_to_miles = 1.6 * miles
    print ("kilometers_to_miles", kilometers_to_miles)
