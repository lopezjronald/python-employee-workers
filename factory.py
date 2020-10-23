def main():
    while True:
        new_emp = add_employee_process()
        display_information(new_emp)
        if add_new_employee() == True:
            continue
        break


def add_employee_process():
    import employees

    new_employee = None
    add_employee = True
    while add_employee:
        while True:
            try:
                worker = int(input(f"Type of Worker:\n1. {'supervisor'.title()}\n2. {'Production worker'.title()}\n"))
            except ValueError:
                print("Invalid Entry")
                continue
            if worker > 2 or worker < 1:
                print("Not a valid number")
                continue
            break
        employee_name = input("New Employee Name: ")
        employee_number = input("New Employee Number: ")
        while True:
            try:
                shift_num = int(input("Shift\n1. Day\n2. Night\n"))
            except ValueError:
                print("Invalid Entry")
                continue
            break

        if worker == 1:
            while True:
                try:
                    supervisor_salary = float(input("Salary: "))
                except ValueError:
                    print("Invalid Entry")
                    continue
                break
            while True:
                try:
                    supervisor_bonus = float(input("Annual Bonus: "))
                except ValueError:
                    print("Invalid Entry")
                    continue
                break
            new_employee = employees.Shift_Supervisor(employee_name, employee_number, shift_num, supervisor_salary,
                                                      supervisor_bonus)
        else:
            while True:
                try:
                    hourly_rate = float(input("Hourly Pay Rate: "))
                except ValueError:
                    print("Invalid Entry")
                    continue
                break
            new_employee = employees.Production_Worker(employee_name, employee_number, shift_num, hourly_rate)
        break
    return new_employee


def display_information(new_employee):
    print(new_employee)


def add_new_employee():
    while True:
        add_new_emp = input("Would you like to add a new employee ('y' for yes or 'n' for no)\n")
        add_new_emp = add_new_emp.lower()
        if add_new_emp == 'n':
            return False
        elif add_new_emp == 'y':
            return True
        else:
            print("Invalid Entry")


main()
