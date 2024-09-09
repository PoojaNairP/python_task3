
from school_module import Student, AdvancedSchool

school=AdvancedSchool()
students=[]


print("1 : Add Student\n"
      "2 : Add grades\n"
      "3 : Remove Student\n"
      "4 : Display Student Details\n"
      "5 : Search Student Details\n"
      "6 : Find Students Having Avg Grade above a Threshold\n"
      "7 : Quit\n")

while True:
    choice=input("Enter the choice:")
    if choice=="1":
        try:
            student_id=int(input("Enter the id: "))
            if student_id<=0:
                raise ValueError("Positive Integer Value expected")
            if student_id in school.students:
                raise ValueError("Student id already exists.")
            name=input("Enter the name: ")
            student=Student(student_id,name)
            school.add_student(student)
            students.append(student)
            #print(school.students)
        except ValueError as e:
            print(e)

    elif choice=="2":
        try:
            if not students:
                raise ValueError("No student added yet")
            grade=input("Enter the grades: ").split(" ")
            grade=(int(grades) for grades in grade)
            students[-1].add_grade(grade)
        except ValueError as e:
            print(e)

    elif choice=="3":
        try:
            if not students:
                raise ValueError("No student added yet")
            student_id=int(input("Enter the id : "))
            if student_id<0:
                raise ValueError("Positive integer value expected")
            school.remove_student(student_id)
        except ValueError as e:
            print(e)


    elif choice=="4":
        school.__iter__()
        for student in school:
            print(student.display_details())

    elif choice=="5":
        try:
            student_id=int(input("Enter student id : "))
            if student_id<0:
                raise ValueError
            student=school.search_student(student_id)
            if student:
                print(student.display_details())
        except ValueError:
            print("Positive Integer Expected")
        # except AttributeError:
        #     print("Student with the given id is not present")

    elif choice=="6":
        while True:
            try:
                threshold=float(input("Enter the threshold : "))
                if not isinstance(threshold, (int, float)) or not (0 <= threshold <= 100):
                    raise ValueError("Threshold must be a number between 0 and 100")
                school.find_students_above_threshold(threshold)
                break
            except ValueError:
                print("Positive Number between 0 and 100 expected\nTry Again")

    elif choice=="7":
        print("Quiting....")
        break

    else:
        print("invalid choice")








# student1=Student(1,"A")
# student2=Student(2,"B")
# student3=Student(3,"C")
# student4=Student(4,"D")
#
# school.add_student(student1)
# school.add_student(student2)
# school.add_student(student3)
# school.add_student(student4)
#
# school.remove_student(2)
# # x=school.__iter__()
# # for i in range(0,3):
# #     print(next(x))
#
# for student in school:
#     print(type(student))
#     details = student.display_details()
#     print(f"Student Details: {details}")


