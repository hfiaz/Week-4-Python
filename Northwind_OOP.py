import pyodbc

class Northwind:
    def __init__(self):
        self.server = "localhost, 1433"
        self.database_name = "Northwind"
        self.user_name = "SA"
        self.password = "Passw0rd2018"

        self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database_name + ';UID=' + self.user_name +
            ';PWD=' + self.password)
        self.my_northwind_cursor = self.connection.cursor()


    def print_result_set(self, result_set):
        for item in result_set:
            print(item)

class Region(Northwind):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name

    def create_operation(self):
        region_id = int(input("Enter the Region ID"))
        region_desc = input("Enter the Region Description")
        sql = "INSERT INTO Region(regionid,regiondescription) Values('{}','{}')".format(region_id, region_desc)
        insert_result_set = self.my_northwind_cursor.execute(sql)
        insert_result_set.commit()

    def read_operation(self):
        result_set = self.my_northwind_cursor.execute("SELECT * FROM Region")
        return result_set

    def update_operation(self):
        region_id = int(input("Enter the Region ID"))
        new_values = input("Enter new value")
        sql = "UPDATE Region SET RegionDescription='{}' WHERE RegionID ={}".format(new_values, region_id)
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()

    def delete_operation(self):
        region_id = int(input("Enter the Region ID"))
        sql = "DELETE FROM Region WHERE RegionID ={}".format(region_id)
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()

class Categories(Northwind):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name

    def create_operation(self):
        category_id = int(input("Enter the Category ID"))
        category_name = input("Enter the Category Name")
        category_desc = input("Enter the Category Description")
        category_picture = input("Enter the picture ")
        sql = "INSERT INTO Categories(CategoryID,CategoryName,Description, Picture) Values('{}','{}', '{}', '{}')".format(category_id,
                                                                                                                          category_name,
                                                                                                                          category_desc,
                                                                                                                          category_picture)
        insert_result_set = self.my_northwind_cursor.execute(sql)
        insert_result_set.commit()

    def read_operation(self):
        result_set = self.my_northwind_cursor.execute("SELECT * FROM Categories")
        return result_set

    def update_operation(self):
        category_id = int(input("Enter the Category ID"))
        new_values = input("Enter new value")
        sql = "UPDATE Categories SET Description='{}' WHERE RegionID ={}".format(new_values, category_id)
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()

    def delete_operation(self):
        category_id = int(input("Enter the Category ID"))
        sql = "DELETE FROM Categories WHERE CategoryID ={}".format(category_id)
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()
