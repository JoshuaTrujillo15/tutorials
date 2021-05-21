def main():

    print("Final Grade Calculator 9000 ...\n")
    
    for iterator in range(1, 5):
        print("\nPlease enter the following data for student {}".format(iterator))
        studentId = input("\tStudent Id: ")
        studentName = input("\tStudent Name: ")
        midtermExam, finalExam = eval(input("\tMidterm and Final Exam Grades (separated by commas): "))
        projectGrade = eval(input("\tProject Grade: "))
        average = (midtermExam + finalExam + projectGrade) / 3
        print("\tFinal Grade:", average)

main()