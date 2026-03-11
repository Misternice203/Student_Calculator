while True:
    print("Student Grade Calculator")
    print("=" * 25)

    total_score = 0
    grade = ""
    subject_scores = {}
    subject_names = []

    subject_count = int(input("Enter the number of subjects: "))
    average_score = total_score / subject_count


    if subject_count <= 0:
        print("Invalid number of subjects. Please enter a positive number.")
        subject_count = int(input("Enter the number of subjects: "))
    else:
        print("Great! now lets enter the name of the subjects!")

    print(f"You have {subject_count} subjects.")
    for i in range(subject_count):
        subject_names.append(input(f"Enter the name of subject {i+1}: "))
    
    
    print("Now let's enter the scores for each subject.")
        
    for i in range(subject_count):
        score = float(input(f"Enter score for subject {i+1}: "))
        while score < 0 or score > 100:
            print("Invalid score. Please enter a value between 0 and 100.")
            score = float(input(f"Enter score for subject {i+1}: "))
        total_score += score

    average_score = total_score / subject_count

    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("--- Student Report ---")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade:{grade}")
    print("Thank you for using the Student Grade Calculator!")
    restart = input("Would you like to Restart the program? (y/n): ")
    if restart.lower() == "y":
        print("Restarting program!!")
    else:
        print("Exiting program. Goodbye!")
        break
