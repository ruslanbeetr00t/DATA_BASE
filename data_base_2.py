import sqlite3

def name_data_base(first_name, last_name, age, car, learning, learn_data_base):
    try:
        with sqlite3.connect('data_base.db') as connect:
            cursor = connect.cursor()
            sqlite3_insert_with_params = """
            INSERT INTO sqlite_info
            (first_name TEXT, 
            last_name TEXT,
            age TEXT,
            car TEXT, 
            learning TEXT, 
            learn_data_base TEXT)
            VALUES(?,?,?,?,?,?);
            """
            data_tuple = (first_name, last_name, age, car, learning, learn_data_base)
            cursor.execute(sqlite3_insert_with_params, data_tuple)
            connect.commit()
            print('Add variable in data base data_base')
            cursor.close()

    except sqlite3 as error:
        print('Error for work SQlite3', error)



name_data_base('Ruslan', 'Khavrenko', '24', 'Alpine D5 Wagon', 'Python', 'SQ Lite3')