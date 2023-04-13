salary = int(input())
years_of_service = int(input())
 
more_than = years_of_service > 5
 
if more_than:
     bonus = (salary * 5)/ 100
     print(bonus)
else:
    print("No Bonus")

    
