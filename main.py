"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
WEEKS_PER_YEAR = 23
TANK_OF_GAS = 0

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(ANNUAL_COST):
    result = ANNUAL_COST / SEMESTERS_PER_YEAR
    return result


def cost_per_month(ANNUAL_COST):
    result = ANNUAL_COST / MONTHS_PER_YEAR
    return result


def cost_per_day(ANNUAL_COST):
    result = ANNUAL_COST / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return result


def cost_per_credit(ANNUAL_COST, credits):
    result = (ANNUAL_COST / SEMESTERS_PER_YEAR) / credits
    return result


def cost_per_class(ANNUAL_COST, credits):
    result = (ANNUAL_COST / SEMESTERS_PER_YEAR) / credits / CS1430_MEETINGS_PER_SEMESTER * CS1430_CREDITS
    return result


def weekly_gas_cost(TANK_OF_GAS):
    result = TANK_OF_GAS * WEEKS_PER_YEAR
    return result   
# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    print("Hello! Let's get you some numbers!")
    ANNUAL_COST = float(input("Enter the total cost for one year: "))
    credits = float(input("Enter the number of credits this semester: "))

    while True:
        # Show your menu here.
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class meeting")
        print("6. Gas cost per year")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(ANNUAL_COST):,.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(ANNUAL_COST):,.2f}")
        elif choice == "3":
            print(f"Cost per class day: ${cost_per_day(ANNUAL_COST):,.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(ANNUAL_COST, credits):,.2f}")
        elif choice == "5":
            print(f"Cost per CS 1430 class meeting: ${cost_per_class(ANNUAL_COST, credits):,.2f}")
        elif choice == "6":
            TANK_OF_GAS = float(input("Enter the cost of a tank of gas: $"))
            print(f"Cost of gas per year: ${weekly_gas_cost(TANK_OF_GAS):,.2f}")
        elif choice == "Q":
            print("Thank You for using the calculator, Goodbye!")
            break

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
