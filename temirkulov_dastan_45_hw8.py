import sqlite3


conn = sqlite3.connect('school.db')
cursor = conn.cursor()

def show_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}. {city[1]}")

def main():
    while True:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        show_cities()

        s = input("Введите id города: ")
        city_id = s

        if city_id == '0':
            break

        cursor.execute("""
            SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
            FROM students
            JOIN cities ON students.city_id = cities.id
            JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        """, (city_id,))

        students = cursor.fetchall()

        if students:
            for student in students:
                print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")
        else:
            print("В этом городе нет учеников.")


countries  = '''CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
'''

insert_countreies = '''CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);
'''

insert_cities = '''INSERT INTO cities (title, area, country_id) VALUES 
('Bishkek', 127.0, 1),
('Osh', 182.5, 1),
('Berlin', 891.7, 2),
('Munich', 310.7, 2),
('Beijing', 16808.0, 3),
('Shanghai', 6340.5, 3),
('Guangzhou', 7434.4, 3);
'''
students = '''CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
'''

insert_students = '''INSERT INTO students (first_name, last_name, city_id) VALUES 
('John', 'Doe', 1),
('Jane', 'Doe', 1),
('Ali', 'Smith', 2),
('Sara', 'Johnson', 2),
('Max', 'Mustermann', 3),
('Erika', 'Mustermann', 3),
('Wang', 'Wei', 5),
('Li', 'Ming', 5),
('Chen', 'Xiao', 6),
('Zhang', 'Wei', 6),
('Zhao', 'Lei', 7),
('Huang', 'Min', 7),
('Hans', 'Schmidt', 4),
('Klaus', 'Meier', 4),
('Tina', 'Fischer', 4);
'''

if __name__ == "__main__":
    main()

conn.close()