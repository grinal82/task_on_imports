from unicodedata import name
from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime

dt = datetime.now()

if __name__ == "__main__":
    calculate_salary()
    print('today is:', dt)
    get_employees()
