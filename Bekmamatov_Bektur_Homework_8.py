import sqlite3 
 
file = sqlite3.connect("private_business.sqlite3") 
sql = file.cursor() 
 
sql.execute( 
    """ 
    CREATE TABLE IF NOT EXISTS business( 
    place TEXT, 
    time TEXT, 
    datetime TEXT 
    ) 
    """ 
) 
file.commit() 
 
 
def info(): 
    user_place = input("Place :") 
    user_time = input("Time :") 
    user_when = input("When :") 
    sql.execute("INSERT INTO business VALUES (?, ?, ?)", (user_place, user_time, user_when)) 
 
    file.commit() 
    print("Записано") 
    for value in sql.execute("SELECT * FROM business"): 
        print(value) 
 
 
info()