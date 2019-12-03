from day1.Northwind_OOP import Northwind, Region
# create a new Northwind object using the init method and save result in my_northwind_object variable
# () This is called a constructor

my_region_object = Region("Region")

operation = input("Please enter your character for your CRUD operations: ")

if operation == 'C' or operation == "c":
    my_region_object.mycreate_operation()
elif operation == "R" or operation == "r":
    my_result_set = my_region_object.read_operation()
    my_region_object.print_result_set(my_result_set)
elif operation == "U" or operation == "u":
    my_region_object.update_operation()
elif operation == "D" or operation == "d":
    my_region_object.delete_operation()