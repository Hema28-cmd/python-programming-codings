# -*- coding: utf-8 -*-
"""1(c).ipynb

#program 1
present_count=0
absent_count=0
total_students=50
print("Enter 'P' for present, 'A' fro absent, or 'END' to stop")
while(present_count+absent_count)<total_students:
      current_student=present_count+absent_count+1
      attendance=input(f"Student{current_student}:").strip().upper()
      if attendance=='END':
        print("Attendance tracking stoppe early")
        break
      elif attendance=='P':
        present_count+=1
      elif attendance=='A':
        absent_count+=1
      else:
        print("Invalid input!")
total_entered=present_count+absent_count
if total_entered>0:
      attendance_percentage=(present_count/total_entered)*100
else:
      attendance_percentage=0.0
print(f"Total present:{present_count}")
print(f"Total absent:{absent_count}")
print(f"Attendance percentage:{attendance_percentage:.2f}%")

#sample output
Enter 'P' for present, 'A' fro absent, or 'END' to stop
Student1:A
Student2:P
Student3:A
Student4:P
Student5:A
Student6:P
Student7:END
Attendance tracking stoppe early
Total present:3
Total absent:3
Attendance percentage:50.00%


#program2
score=0
total_questions=10
print("Enter 'C' for correct,'W' for wrong, or 'Quit' to exit")
for i in range (1,total_questions+1):
  answer=input(f"Question{i}Result:").strip().upper()
  if answer=='OCUIT':
    print("Quiz terminated by user.")
    break
  elif answer=='C':
    score+=5
  elif answer =='W':
    score==1
  else:
    print("Invalid input!Treated as unanswered")
if score>=40:
  grade='A'
elif score>=25:
  grade='B'
elif score>=10:
  grade='C'
else:
  grade='F'
print(f"Final score:{score} marks")
print(f"Grade:{grade}")

#sample output
Enter 'C' for correct,'W' for wrong, or 'Quit' to exit
Question1Result:C
Question2Result:
Invalid input!Treated as unanswered
Question3Result:C
Question4Result:W
Question5Result:C
Question6Result:QUIT
Invalid input!Treated as unanswered
