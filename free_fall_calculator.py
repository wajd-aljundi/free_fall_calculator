import math


def User_input():

    UserIn = input("Hi! this the free fall claculator.\nif u want to calculate the fall height type h\nif u want to calculate the speed type v\nif you want to calculate the duration of the fall type t\n")

    if UserIn == "h":
        fall_height()
    if UserIn == "v":
        speed()
    if UserIn == "t":
        duration()
    else:
        print("check ur input pls")
        User_input()


def fall_height():
    time_input = input("input the fall duration ")
    if float(time_input) > 0:
        h = 0.5 * 9.81 * (float(time_input)**2)
        print("X = {:.2f}".format(h))
        another_action = input("wanna do anything else? pls type yes or no ")
        if another_action == "yes":
            User_input()
        else:
            print("thank you for using this app")
    else:
        print("time must be > 0")
        fall_height()


def speed():
    question = input(
        "do u have the time given or not? answer with \"yes\" or \"no\" ").lower()
    if question == "yes":
        time_input = input("input the time ")
        if float(time_input) > 0:
            v = 9.81 * float(time_input)
            print("v = {:.2f}".format(v))
            another_action = input(
                "wanna do anything else? pls type yes or no ")
            if another_action == "yes":
                User_input()
            else:
                print("thank you for using this app")
        else:
            print("time must be > 0")
    elif question == "no":
        height_input = input("pls input the height ")
        if float(height_input) > 0:
            v = math.sqrt(2 * 9.81 * float(height_input))
            print("X = {:.2f}".format(v))
            another_action = input(
                "wanna do anything else? pls type yes or no ")
            if another_action == "yes":
                User_input()
            else:
                print("thank you for using this app")
        else:
            print("height must be > 0")
    else:
        print("pls type yes or no")
        speed()


def duration():
    height_input = input("pls input the height ")
    if float(height_input) > 0:
        t = math.sqrt((2 * float(height_input)/9.81))
        print("t = {:.2f}".format(t))

        another_action = input(
            "wanna do anything else? pls type yes or no ").lower()
        if another_action == "yes":
            User_input()
        else:
            print("thank you for using this app")
    else:
        print("height must be > 0")
        duration()


User_input()
