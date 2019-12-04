import pyodbc
import json

server = "localhost, 1433"
database_name = "Northwind"
user_name = "SA"
password = "Passw0rd2018"

connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database_name + ';UID=' + user_name +
        ';PWD=' + password)
my_northwind_cursor = connection.cursor()

query = "SELECT * FROM Customers"
result = my_northwind_cursor.execute(query)

items = []

for row in result:
    for key in my_northwind_cursor.description:
        items.append({key[0]: value for value in row})

#print(json.dumps({'items': items}))

#file = open("sql_json.json", "w")
#file.write(json.dumps({'items': items}, indent=2))

with open("sql_json.json", "w") as json_file:
    json.dump(items, json_file)

#print(json.dump(items, json_file, indent=2))