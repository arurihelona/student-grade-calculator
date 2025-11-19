print("*****Student Grade Calculator *****\n")
marks = []
subjects = ["Maths", "Physics", "Chemistry"]

x = int(input("Number of student grades to calculate: "))
students = []

def calculate_grade(average):
    if average >= 95:
        return "S"
    elif average >= 85:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 65:
        return "C"
    elif average >= 55:
        return "D"
    elif average >= 36:
        return "E"
    else:
        return "Fail"
for i in range(x):
    name = input(f"Enter student {i+1} name: ")
    marks = []
    # Taking marks from user
    for j in subjects:
        while (1):
            try:
                score = float(input(f"Enter marks for {j} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    # Calculations
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    students.append((name,total,average,grade))

# Output
for name,total,average,grade in students:
    print("*** RESULT ***")
    print(f"Name of Student : {name}")
    print(f"Total Marks   : {total}")
    print(f"Average Marks : {average:.2f}")
    print(f"Grade         : {grade}")
    print("-----------------------------\n")
