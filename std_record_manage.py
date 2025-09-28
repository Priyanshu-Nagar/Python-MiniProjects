import csv
import re
num_of_students=0
sum_of_marks=0
student_marks=[]
try:
    with open("student_record.csv","r") as f:
        reader=csv.DictReader(f)
        for student in reader:
            try:
                student['age']=int(student['age'])
                student['marks']=int(student['marks'])
            except ValueError:
                print(f"{student['name']}'s data is incorrect")
                exit()
            if re.search(r"^[a-zA-Z]+$",student['name']):
                student['name']={
                    "name":student['name'],
                    "age":student['age'],
                    "marks":student['marks']
                }
                num_of_students += 1
                sum_of_marks +=int(student['name']['marks']) 
                
                

                student_marks.append(int(student['name']['marks']))

                if int(student['name']['marks'])>=80:
                    print(f"{student['name']['name']} passed the exam")
                else:
                    print(f"{student['name']['name']} failed the exam")
            else:
                print(f" ye Marks={student['marks']} aur Age={student['age']} waale ka name galat hai")
                break
except FileNotFoundError:
    print("file nhi mili")
    exit()
except Exception as e:
    print(e)
    exit()
avg_marks=sum_of_marks/num_of_students
# print(max(student_marks))
with open("student_record.csv","r") as f:
    reader=csv.DictReader(f)
    for student in reader:
        if int(student['marks'])==max(student_marks):
            print(f"{student['name']} is the topper of the class with {student['marks']} marks")
print(f"average marks of class is {avg_marks}")
