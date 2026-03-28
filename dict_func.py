def employee_print(employee_info):
    data = employee_info.copy()
    name = data.pop("Name", "N/A")
    salary = data.pop("Salary", "N/A")
    role = data.pop("Role", "N/A")
   
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")
    if data:
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")

    