print("'welcome to the tip calculator'")
bill=float(input("what was the total bill?"))
tip = int(input("what percentage tip would you like to give ? 10 12 15"))
people =int(input("how many people to split the bill?"))
bill_tip= tip/100
total_tip=bill*bill_tip
total_bill= bill+total_tip
bill_per_people=total_bill/people
final_amount=round(bill_per_people,2)
print(f"Each person should pay:{final_amount}")