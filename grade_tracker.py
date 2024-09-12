grades = {}

while True:
    option = input("""Menu:
    1. Add a student and their grades
    2. View all students and their grades
    3. Exit
    Chose an option: """)

    match option:
        case "1":
            student = input("Enter the student's name: ")
            grade = input(f"Enter {student}'s grade: ")
            grades[student] = grade
            print(f"{student}'s grade has been addd")
        case "2":
            for name, grade in grades.items():
                print(f"{name}: {grade}")
        case "3":
            break


