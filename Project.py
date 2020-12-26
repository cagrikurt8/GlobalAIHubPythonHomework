class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def take_courses(self, *args):
        self.course_list = list()
        for i in args:
            if i != "":
                self.course_list.append(i)
        if len(self.course_list) < 3:
            return("You failed in class.")

        else:
            return self.course_list

    def grade_calculator(self, midterm, final, project):
        self.grade_dictionary = {"midterm": midterm, "final": final, "project": project}
        self.grade = midterm * 0.3 + final * 0.5 + project * 0.2
        return self.grade

student = Student("Çağrı", "Kurt")

attempts = 3
while True:
    in_name = input("Your name: ")
    in_surname = input("Your surname: ")

    if in_name != student.name or in_surname != student.surname:
        attempts -= 1
        print(f"You have {attempts} attempt(s) left.")
        if attempts == 0:
            print("Please try again later.")
            break
    else:
        print("\nWelcome.")
        break
if attempts != 0:
    print("\nIf you don't want to take any course just press enter to skip. Don't forget you must take at least 3 courses!\n")
    for i in range(5):
        if i == 0:
            lesson1 = input("Enter your first course: ")
        elif i == 1:
            lesson2 = input("Enter your second course: ")
        elif i == 2:
            lesson3 = input("Enter your third course: ")
        elif i == 3:
            lesson4 = input("Enter your fourth course: ")
        elif i == 4:
            lesson5 = input("Enter your fifth course: ")

    student.take_courses(lesson1, lesson2, lesson3, lesson4, lesson5)
    print("\n")
    if len(student.course_list) < 3:
        print(student.take_courses(lesson1, lesson2, lesson3, lesson4, lesson5))
    else:
        lessons_list = student.course_list
        print("You have to choose one of the courses that you've taken for exam.\n")
        for i in range(len(lessons_list)):
            print(f"{i+1}. {lessons_list[i]}")
        in_course = int(input("Enter the course you choose(Just enter the ordinal): "))
        chosen_course = lessons_list[in_course - 1]
        print(f"\nYou have chosen {chosen_course} for exam. Good luck!\n")
        midterm = int(input("Enter your midterm grade: "))
        final = int(input("Enter your final grade: "))
        project = int(input("Enter your project grade: "))
        student.grade_calculator(midterm, final, project)
        grade = student.grade
        print(f"\nYour total grade: {grade}")
        if grade >= 90:
            print("Your letter grade: AA")
        elif grade >= 70:
            print("Your letter grade: BB")
        elif grade >= 50:
            print("Your letter grade: CC")
        elif grade >= 30:
            print("Your letter grade: DD")
        elif grade < 30:
            print("Your letter grade: FF")
            print("You failed in class.")
        print(student.grade_dictionary)
