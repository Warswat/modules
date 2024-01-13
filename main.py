from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(dt.datetime.date(dt.datetime.now()))

