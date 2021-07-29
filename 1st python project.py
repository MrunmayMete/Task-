#Project 1: Basic school administration tool

import csv

def write_into_csv(info_list):
    with open("student_info.csv" , "w+" , "newline=" ) as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow("Name " , "Age" , "Contact Number" , "E-mail Id")
        writer.writerow(info_list)

if __name__ == "__main__":
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter some student information in the following format - Name Age Contact_Number Email_Id: ".format(student_num))
        print("Entered Informartion: ", student_info)
        #split
        student_info_list = student_info.split(" ")
        print("\nThe entered information is -\nName:{}\nAge: {}\nContact Number: {}\nEmail Id:{}" .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check = input("Is the entered information correct?(yes/no)")

        if choice_check == "yes":         
            write_into_csv(student_info_list)
            condition_check = input("Enter (yes/no if you want to put information of another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
                print("Okay , Bye")
        else:
            choice_check == "no"
            print("\nPLease re-enter the values!")