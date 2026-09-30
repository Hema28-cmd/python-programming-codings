# -*- coding: utf-8 -*-
"""1(b).ipynb

#program 1
marks=float(input("Enter marks:"))
income=float(input("Enter family income:"))
if marks >= 90 and income <=50000:
  print("Full scholarship")
elif marks >=80 and income <=75000:
  print("Half scholarship")
else:
  print("Not eligible")

# sample output
Enter marks:90
Enter family income:45000
Full scholarship


#program 2
age=int(input("Enter age:"))
salary=int(input("Enter salary:"))
credit=int(input("Enter credit score:"))
if age >=21:
  if salary >=30000:
    if credit >=700:
      print("Loan approved")
    else:
      print("Rejected:Credit score is very low")
  else:
    print("Rejected:Salary is too low")
else:
  print("Rejected: Age must be atleast 21")

#sample output
Enter age:21
Enter salary:30000
Enter credit score:300
Rejected:Credit score is very low


#program 3
experience=int(input("Enter years of experience:"))
rating=input("Enter performance rating:")
if experience >=10 and rating =="Excellent":
  bonus=20
elif experience >=5 and rating =="Good":
  bonus=10
elif rating =="Average":
  bonus=5
else:
  bonus=0
print(f"Bonus:{bonus}%")

#sample output
Enter years of experience:0
Enter performance rating:Average
Bonus:5%


#program 4
purchase_amount=float(input("Enter the total purchase ampunt($):"))
is_premium=input("Are you a premium member?:").strip().lower() =="yes"
discount=0.0
if purchase_amount>=5000:
  if is_premium:
    discount=0.25
  else:
    if purchase_amount>=2000:
      if is_premium:
        discount=0.15
      else:
        discount=0.10
    else:
      if is_premium:
        discount=0.05
else:
  discount=0.0
discount_amount=purchase_amount*discount
final_amount=purchase_amount-discount_amount

#sample output
Enter the total purchase ampunt($):6000
Are you a premium member?:yes


#program 5
age=25
is_weekend=True
if age<12:
  ticket_price=100
elif age<=59:
  ticket_price=200
else:
  ticket_price=150
if is_weekend:
  ticket_price+=50
print("---Movie ticket Summary---")
print(f"Age of customer:{age}")
print(f"Is weekend show?{is_weekend}")
print(f"Totla ticket price:${ticket_price}")

#sample output
---Movie ticket Summary---
Age of customer:25
Is weekend show?True
Totla ticket price:$250
