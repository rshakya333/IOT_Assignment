
#temperature => name of table
#temperature => 1 column => float
#city => 2nd column varchar(20)
# time => timestamp => default CURRENT_TIMESTAMP 

#temperature_database.py

import temperature_database as db
db.insert_temperatures(32.2, "Bhopal")
db.insert_temperatures(22.2, "gwalior")
db.insert_temperatures(22.2, "indore")


print("New temperature added.......")
temperatures = db.get_temperatures()
print(temperatures)
print()
for t in temperatures:
    print(t)







