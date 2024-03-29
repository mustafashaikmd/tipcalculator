print("Welcome to the tip calculator!!!!")
bill = float(input("Enter the Total bill amount?"))
tip = int(input("Enter the tip percentage?"))
people = int(input("Enter the number of people?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each Person should pay: Rs.{final_amount}")