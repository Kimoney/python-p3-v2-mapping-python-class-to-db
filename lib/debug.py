#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Delete the existing table to debug on a clean slate
Department.drop_table()

# Create a new table to debug on a clean slate
Department.create_table()


# INSTANCE METHODS
# # Test Save Methods   
# payroll = Department("Payroll", "Building A, 5th Floor")
# print(f"\033[31m*********{payroll}*********\033[0m")  # <Department None: Payroll, Building A, 5th Floor>

# payroll.save()  # Persist to db, assign object id attribute
# print(f"\033[31m*********{payroll}*********\033[0m")  # <Department 1: Payroll, Building A, 5th Floor>

# hr = Department("Human Resources", "Building C, East Wing")
# print(f"\033[31m******{hr}******\033[0m")  # <Department None: Human Resources, Building C, East Wing>

# hr.save()  # Persist to db, assign object id attribute
# print(f"\033[31m******{hr}******\033[0m")  # <Department 2: Human Resources, Building C, East Wing>

# CLASS METHOD
# payroll = Department.create("Payroll", "Building A, 5th Floor")
# print(f"\033[31m*+*+*+*+*{payroll}*+*+*+*+*\033[0m")  # <Department 1: Payroll, Building A, 5th Floor>

# hr = Department.create("Human Resources", "Building C, East Wing")
# print(f"\033[31m*+*+*+*+*{hr}*+*+*+*+*\033[0m")  # <Department 2: Human Resources, Building C, East Wing>


payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>


ipdb.set_trace()
