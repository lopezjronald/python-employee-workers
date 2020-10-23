class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, name):
        self.__employee_name = name

    def get_employee_name(self):
        return self.__employee_name

    def set_employee_number(self, number):
        self.__employee_number = number

    def get_employee_number(self):
        return self.__employee_number


class Production_Worker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def get_shift_number(self):
        return self.__shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def __str__(self):
        return (f"Name: {self.get_employee_name()}\n"
                f"Employee Number: {self.get_employee_number()}\n"
                f"Employee Shift: {self.get_shift_number()}\n"
                f"Employee Hourly Pate Rate: $ {self.get_hourly_pay_rate():,.2f}")


class Shift_Supervisor(Production_Worker):
    def __init__(self, employee_name, employee_number, shift_number, salary, annual_bonus):
        Production_Worker.__init__(self, employee_name, employee_number, shift_number, hourly_pay_rate=None)
        self.__salary = salary
        self.__annual_bonus = annual_bonus

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_bonus(self):
        return self.__annual_bonus

    def __str__(self):
        return (f"Name: {self.get_employee_name()}\n"
                f"Employee Number: {self.get_employee_number()}\n"
                f"Employee Shift: {self.get_shift_number()}\n"
                f"Employee Salary: $ {self.get_salary():,.2f}\n"
                f"Employee Bonus: $ {self.get_annual_bonus():,.2f}")
