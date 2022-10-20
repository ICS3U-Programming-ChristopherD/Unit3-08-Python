#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Oct. 20, 2022
# This program checks if a year is a leap year.


def main():
    user_year = input("Enter a year: ")
    print("")

    try:
        user_year = int(user_year)
    except ValueError:
        print("You must enter an integer.\n")
        return main()

    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                print(f"{user_year} is a leap year.\n")
            else:
                print(f"{user_year} is not a leap year.\n")
        else:
            print(f"{user_year} is a leap year.\n")
    else:
        print(f"{user_year} is not a leap year.\n")


if __name__ == "__main__":
    main()
