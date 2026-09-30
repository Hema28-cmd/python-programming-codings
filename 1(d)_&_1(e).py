# -*- coding: utf-8 -*-
"""1(d) & 1(e).ipynb


#program 1
cart=["Laptop","Mouse","Keyboard"]
print(f"Step2:Initial cart:{cart}")
cart.append("Headphones")
print(f"Step3:After append:{cart}")

#sample output
Step2:Initial cart:['Laptop', 'Mouse', 'Keyboard']
Step3:After append:['Laptop', 'Mouse', 'Keyboard', 'Headphones']


#program 2
emp_ids=(101,102,103,104,105)
print(f"Step2:Complete Employee ID tuple:{emp_ids}")
print(f"Step3:First employee ID:{emp_ids[0]}")
print(f"Step4:Last employee ID(negative index):{emp_ids[-1]}")

#sample output
Step2:Complete Employee ID tuple:(101, 102, 103, 104, 105)
Step3:First employee ID:101
Step4:Last employee ID(negative index):105


#program 3
students={"Arun","Priya","Rahul","Arun"}
print("Registered students:",students)
students.add("Kavin")
print("After adding Kavin:",students)
students.remove("Rahul")
print("After removing Rahul:",students)

#sample output
Registered students: {'Priya', 'Rahul', 'Arun'}
After adding Kavin: {'Kavin', 'Priya', 'Rahul', 'Arun'}
After removing Rahul: {'Kavin', 'Priya', 'Arun'}


#program 4
student={
    "No":101,
    "Name":"Kavya",
    "Class":12,
    "Age":17,
    "Marks":99,
}
print("Complete Record:",student)
print("Name:",student["Name"])
student["City"]="Erode"
print("After adding City:",student)

#sample output
Complete Record: {'No': 101, 'Name': 'Kavya', 'Class': 12, 'Age': 17, 'Marks': 99}
Name: Kavya
After adding City: {'No': 101, 'Name': 'Kavya', 'Class': 12, 'Age': 17, 'Marks': 99, 'City': 'Erode'}


#program 5
first_name="Kavya"
last_name="Sri"
username=first_name[:3]+last_name[-3:]
print(f"Username:{username}")

#sample output
Username:KavSri


#program 6
password="Python123"
is_strong=(len(password)>=8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password))
print("Strong password"if is_strong else"Weak password")

#sample output
Strong password


#program 7
email="student@gmail.com"
is_valid="@"in email and email.endswith(".com")and " " not in email
print("Valid Email"if is_valid else "Invalid Email")

#sample output
Valid Email


#program 8
product_code="tv123lg"
formatted=f"{product_code[:2].upper()}-{product_code[2:5]}-{product_code[5:].upper()}"
print(f"Formatted:{formatted}")

#sample output
Formatted:TV-123-LG


#program 9
text="Python is easy. I love Python because Python is powerful."
cleaned_text=text.lower().replace("."," ").replace(","," ")
count=cleaned_text.split().count("python")
print(f"Python appers {count} times")

#sample output
Python appers 3 times


#program 10
msg="Machine Learnig"
decoded=" ".join(word[::-1] for word in msg.split())
print(f"Decoded:{decoded}")

#sample output
Decoded:enihcaM ginraeL


#program 11
filename="assignment.pdf"
if filename.lower().endswith('.pdf'):
  print("PDF document")
elif filename.lower().endswith(('.jpg','.jpeg','.png')):
  print("Image file")
else:
  print("Unknown file type")

#sample output
PDF document


#program 12
message="I hate bad language"
banned_words=["bad","hate"]
for word in banned_words:
  message=message.replace(word,"***")
  print(message)

#sample output
I hate *** language
I *** *** language


#program 13
passenger ="Priyanka"
mobile = '9876543210'
destination="New Delhi"
name_part=passenger[:2]
mobile_part=mobile[-4:]
words=destination.split()
destination_part=words[0][0]+words[1][0]
ticket_id=name_part+mobile_part+destination_part.upper()
print("Ticket ID:",ticket_id)

#sample output
Ticket ID: Pr3210ND


#program 14
feedback="The service was excellent and quick."
feedback=feedback.lower()
positive_words=["excellent","good","awesome"]
negative_words=["poor","bad","worst"]
if any(word in feedback for word in positive_words):
  print("Positive feedback")
elif any(word in feedback for word in negative_words):
  print("Negative feedback")
else:
  print("Netural feedback")

  #sample output
  Positive feedback
