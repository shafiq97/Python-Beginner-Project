import sqlite3
import uuid

if __name__ == "__main__":

    print("MENU")
    print("1. Insert new contact")
    print("2. View all contact")
    print("3. Search contact")
    choice = int(input("Enter choice: "))

    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()

    # check if table person exists
    # conn.execute("DROP TABLE PERSON")
    try:
        conn.execute('''CREATE TABLE PERSON
                         (ID TEXT PRIMARY KEY,
                         NAME TEXT NOT NULL,
                         NUMBER TEXT NOT NULL);''')
        print("Table created successfully")

    except Exception as e:
        print(e)

    if choice == 1:
        nextId = str(uuid.uuid4())
        print(type(nextId))
        name = input("Name: ")
        number = input("Number: ")
        cursor.execute("insert into PERSON (ID, NAME, NUMBER) values (?, ?, ?)",
                       (nextId, name, number))
        conn.commit()
        print("Records created successfully")

    elif choice == 2:
        data = conn.execute("SELECT id, name, number FROM PERSON")
        for row in data:
            print("ID = " + row[0])
            print("NAME = " + row[1])
            print("NUMBER = " + str(row[2]) + '\n\n')

    elif choice == 3:
        print("1. Search by name")
        print("2. Search by number")
        choice = int(input("Enter choice: "))
        if choice == 1:
            name = input("Name: ")
            data = conn.execute("SELECT id, name, number FROM PERSON WHERE name =?", (name,))
            for row in data:
                print("ID = " + row[0])
                print("NAME = " + row[1])
                print("NUMBER = " + str(row[2]) + '\n\n')
        elif choice == 2:
            number = input("Number: ")
            data = conn.execute("SELECT id, name, number FROM PERSON WHERE number =?", (number,))
            for row in data:
                print("ID = " + row[0])
                print("NAME = " + row[1])
                print("NUMBER = " + str(row[2]) + '\n\n')

    conn.close()
