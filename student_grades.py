students = {"aditya" : "A" ,"priya" : "A" ,"neha" : "B" ,"aman" : "D"}
while True:
    print("\n1. Add student")
    print("2. Update grade")
    print("3. Show all grades")
    print("4. Exit")
    choice = int(input("Enter your choice :"))
    if choice == 4 :
        print ("Thank you for coming")
        break
    elif choice == 1 :
        name = input("Enter name of the student :")
        grade = input("Enter grade of the student :")
        students[name] = grade
        print("Student added")

    elif choice == 2 :
        name = input("Enter the name of student :")
        if name in students :
            grade = input("Enter grade of the student :")
            students[name] = grade
            print("Grade Updated")
        else :
            print("student not found")

    elif choice == 3 :
        for name,grade in students.items() :
            print("All grades of students are :\n",name ,"->",grade)
    else :
        print(" Invalid Choice please select from 1 to 4")
