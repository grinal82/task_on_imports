from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime

dt = datetime.now()


def main():
    calculate_salary()
    print('today is:', dt)
    get_employees()


if __name__ == "__main__":
    main()
