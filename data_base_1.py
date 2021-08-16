import sqlite3

with sqlite3.connect('new_learning.db') as connect:
    cursor = connect.cursor()

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS new_learning(
     day INTEGER,
     first_name TEXT,
     last_name TEXT,
     age INTEGER,
     learn TEXT,
     learn_data_base TEXT);
     """)
    connect.commit()

cursor.execute("""
INSERT INTO new_learning(day, first_name, last_name, age, learn, learn_data_base)
VALUES(17, Ruslan, Khavrenko, 24, Python, SQ_Lite3);
""")
connect.commit()
