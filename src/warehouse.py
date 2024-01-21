from time import time as tt, ctime as ct


# Make this class a singleton
def singleton(a_class):
    instance = None # this is global to the inner function, to have access to it use Nonlocal statement
    def inner(*args, **kwargs):
        nonlocal instance # give me permission to change the value of instance
        if instance is None: # if i do not have this class registered in my dict
            instance = a_class(*args, **kwargs) # update only happens 
        return instance
    return inner

@singleton
class Warehouse:

    def __init__(self):
        self.num_employees = 0
        self.creation_time = ct(tt())
        self.employee_list = []

    def add_employee(self):
        self.num_employees += 1

    def __str__(self):
        return f"Warehouse created on {self.creation_time}. Employees: {self.num_employees}"
