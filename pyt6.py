def validate_voter_age(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote yet.")

age = int(input("Enter your age: "))
validate_voter_age(age)

