def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def get_student_marks():
    student_marks = {}
    print("Enter student names and their marks for 5 subjects.")

    while True:
        student_name = input("Enter student name (or 'exit' to finish): ")
        if student_name.lower() == 'exit':
            break
        marks = []
        for subject in ['Maths', 'English', 'Physics', 'Chemistry', 'Computer']:
            mark = int(input(f"Enter mark for {subject}: "))
            marks.append(mark)
        student_marks[student_name] = marks

    return student_marks

def print_mark_statement(student_marks):
    print(f"{'Student Name':<15}{'Maths':<10}{'English':<10}{'Physics':<10}{'Chemistry':<10}{'Computer':<10}{'Average':<10}{'Grade':<10}")
    print("=" * 70)

    for student, marks in student_marks.items():
        avg = sum(marks) / len(marks)
        grade = calculate_grade(avg)
        print(f"{student:<15}", end="")
        for mark in marks:
            print(f"{mark:<10}", end="")
        print(f"{avg:<10.2f}{grade:<10}")


student_data = get_student_marks()
print_mark_statement(student_data)
