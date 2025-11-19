import os
import json
print("DLl Student Information System")
print("=============================================")

stud_record = {}
while True:
    print("Select From The Following Options")
    print("A - Adding Student Record")
    print("B - Print All Student Information")
    print("C - Search Student")
    print("D - Delete Student Record")
    print("E - Edit Student Info")
    print("F - Export Data")
    print("G - Exit System")

    choice = input("Input your choice: ").lower().strip()

    if choice == 'a':
        student_id = input("Input ID Number ---> ")
        first_name = input("Enter First Name ---> ")
        last_name = input("Enter Last Name ---> ")
        course = input("Enter Course ---> ")
        section = input ("Enter Section ---> ")
        email = input("Enter Your EMail ---> ")
        print("DATA SAVED")

        stud_record[student_id] = [first_name, last_name, course, section, email]
        os.system('cls')
        continue

    elif choice == 'b':
        
        print("PRINTING STUDENT INFORMATION...")
        print("======================================")

        for id, info in stud_record.items():
            print(f"STUDENT ID {student_id} - RECORD - {info}")
        
        continue

    if choice == 'c':
        os.system('cls')

        print("SEARCHING STUDENT RECORD...")

        search_id = input ("INPUT STUDENT ID ---> ").lower()
        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRecord Found")
                
                for id in stud_record[search_id]:
                    print(f"--- {id} ---")

            else:
                print("NO RECORD FOUND")

            break
        continue

    if choice == 'd':
        os.system('cls')

        print("DELETE STUDENT RECORD...")

        search_id = input ("INPUT STUDENT ID ---> ").lower()
        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRecord Found")
                
                for id in stud_record[search_id]:
                    print(f"--- {id} ---")

                stud_record.pop(search_id)

                print("DATA DELETED")

            else:
                print("NO RECORD FOUND")

            break
        continue

    if choice == 'e':
        print("UPDATING STUDENT RECORD...")
        search_id = input ("INPUT STUDENT ID ---> ").lower()
        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRecord Found")
                
                for id in stud_record[search_id]:
                    print(f"--- {id} ---")

                first_name = input("Enter First Name ---> ")
                last_name = input("Enter Last Name ---> ")
                course = input("Enter Course ---> ")
                section = input ("Enter Section ---> ")
                email = input("Enter Your EMail ---> ")
                print("DATA SAVED")

                stud_record[search_id][0] = first_name
                stud_record[search_id][1] = last_name
                stud_record[search_id][2] = course
                stud_record[search_id][3] = section
                stud_record[search_id][4] = email
                print("RECORD UPDATED")


            else:
                print("NO RECORD FOUND")

            break
        continue

    if choice == 'f':
        print("EXPORT DATA")

        with open ('student_record.json', 'w') as new_file:
            json.dump(stud_record, new_file, indent = 4)
        
        continue

        print("DATA SAVED SUCCESSFULLY....")

    if choice == 'g':
        break
        