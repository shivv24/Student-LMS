class Student:
    def __init__(self, name, rollno, email, password):
        self.name = name
        self.rollno = rollno
        self.email = email
        self.password = password

class DB:
    def __init__(self):
        self.students = {}
        
    def register(self, name, rollno, email, password):
        if rollno in self.students:
            print("User already exists. Go to Login.")
            return
        self.students[rollno] = [name, email, password]
        print("Registration successful.")
        
    def login(self, email, password):
        for rollno, student in self.students.items():
            if student[1] == email and student[2] == password:
                print("You are logged in.")
                return
        print("Enter correct credentials or register before login.")

    def display(self):
        for rollno, student in self.students.items():
            print(f"Roll No: {rollno}, Name: {student[0]}, Email: {student[1]}")

    def logout(self):
        print("Successfully logged out.")

        

db = DB()

def switchcase(op):
    while True:
        if op == 1:
            name = input("Enter name: ")
            rollno = input("Enter roll number: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            db.register(name, rollno, email, password)
            menu()
        elif op == 2:
            email = input("Enter email: ")
            password = input("Enter password: ")
            db.login(email, password)
            menu()
        elif op == 3:
            db.display()
            menu()
        elif op == 4:
            db.logout()
            exit()
        elif op == 5:
            exit()

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Display")
    print("4. Logout")
    print("5. Exit")
    option = int(input("Enter your choice: "))
    switchcase(option)

menu()
