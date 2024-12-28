import mysql.connector

def get_temperatures():

    connection=mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_db",
    )
    cursor = connection.cursor()
    query = f"select * from temperatures;"
    cursor.execute(query)
    temperatures= cursor.fetchall()
    cursor.close()
    connection.close()
    return temperatures


 #----------End of function get_temperature()-----------------------------------


def insert_temperatures(temperature,city):

    connection=mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_db",
    )
    
    cursor  = connection.cursor()      
    query= f"insert into temperatures (temperature,city)values ({temperature}, \"{city}\");"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
























