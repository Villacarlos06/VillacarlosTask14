def check_grade (grade):
    if grade >=80 or grade <=100:
        return("You did a great job.")
    elif grade >=70 or grade <=79:
        return("Keep it up.")
    elif grade >=60 or grade <=69:
        return("You passed, but there's room for improvement.")  
    elif grade <=59:
        return "Better luck next time."
    
    usergrade = int(input("enter your grade :"))
    (check_grade(userGrade))