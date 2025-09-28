import statistics
import random
import sys

print("""welcome to Student Marks Analyzer 
      ===========\n
      """)
if len(sys.argv)<5:
    sys.exit("please enter 5 student names")
marks=[]
for i in range(1,6):
   while True:
        try:
            mark=int(input(f"marks of {sys.argv[i]}?"))
        except ValueError:
            print("please enter a integer value")
        
        else:
           
                if mark<=100 and mark>=0:
                    marks.append(mark)
                    break 
                else:
                    print("please enter num between 0 and 100")
                    
print("Marks of students are:", marks)

print("average marks of students are:",statistics.mean(marks))
print("median marks of student are:",statistics.median(marks))
print("mode marks of student are:",statistics.mode(marks))
print("random marks :",random.choice(marks))

