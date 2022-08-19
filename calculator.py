from math import sqrt
from os import system
from sys import exit
class Calculator:
    def __init__(self, VALUE1, VALUE2):
        self.value1 = float(VALUE1)
        self.value2 = float(VALUE2)

    def sum(self):
        return self.value2 + self.value1

    def minus(self):
        return self.value1 - self.value2

    def multiplication(self):
        return self.value1 * self.value2

    def division(self):
        return self.value1 / self.value2

    def qüvvət(self):
        return self.value1 ** self.value2

    def square_root(self):
        return sqrt(self.value1)


def menu():
    while True:
        system("cls")

        print("""
        { 1 } Sum
        { 2 } Minus
        { 3 } Multiplication
        { 4 } Division
        { 5 } Qüvvət
        { 6 } Square root
        { Q } Quit
        """)


        def clean():
            input(" Press to back menu..")
            system("cls")

        choose = input("Choose a process: ")

        if choose == "6":
            value1 = float(input("Value 1: "))
            if value1 and value2:
                cal = Calculator(value1, value2)
                print("The square root of {} is {}".format(value1,  cal.square_root()))
                clean()

            else:print("Please, enter a input")

        else:

            value1 = input("Value 1: ")
            value2 = input("Value 2: ")

            if value1 and value2:
                cal = Calculator(value1, value2)

                if choose == "1":
                    print("The sum of {} and {} is {}".format(value1, value2, cal.sum()))
                    clean()

                elif choose == "2":
                    print("{} minus {} is {}".format(value1, value2, cal.minus()))
                    clean()

                elif choose == "3":
                    print("{} times {} is {}".format(value1, value2, cal.multiplication()))
                    clean()

                elif choose == "4":
                    print("{} division {} is {}".format(value1, value2, cal.division()))
                    clean()

                elif choose == "5":
                    print("{} üstü {} is {} :D".format(value1, value2, cal.qüvvət()))
                    clean()

                elif choose == "q" or choose == "Q":
                    print(" Exiting..")
                    exit()

                else:
                    print(" Wrong input! Try again.")
                    clean()

            else:print("Please, enter a input")

menu()


