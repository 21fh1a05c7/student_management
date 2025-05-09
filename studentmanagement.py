from random import choice
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="charan@5c7",
    database="pdbc_db"
)
cursor = conn.cursor()


def add_student():
    id=input("enter id:")
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    cursor.execute("INSERT INTO students (id,name, age, grade) VALUES (%s,%s, %s, %s)", (id,name, age, grade))
    conn.commit()
    print("Student added.")

def view_students():
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        print(student)


def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("New name: ")
    age = input("New age: ")
    grade = input("New grade: ")
    cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s", (name, age, grade, student_id))
    conn.commit()
    print("Student updated.")


def delete_student():
    student_id = input("Enter ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted.")


def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")

        choice_input = input("Enter choice: ")

        if choice_input == "1":
            add_student()
        elif choice_input == "2":
            view_students()
        elif choice_input == "3":
            update_student()
        elif choice_input == "4":
            delete_student()
        elif choice_input == "5":
            break
        else:
            print("Invalid choice, please try again.")


menu()

