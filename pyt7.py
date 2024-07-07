def validate_marks(marks):
    if 0 <= marks <= 100:
        print("Marks are within the valid range.")
    else:
        print("Marks should be between 0 and 100.")

marks = float(input("Enter the marks: "))
validate_marks(marks)

