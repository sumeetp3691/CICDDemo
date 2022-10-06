import datetime
name=input("Enter your name:")
dob=input("Enter your birth date in DD-MM-YYYY format:")
birthyear=dob[6:10]
today=datetime.date.today()
year=today.year
age=int(year)-int(birthyear)
print(f"Hi {name} your age is : {age}")
remainingyears=100-int(age)
futureyear=int(year)+int(remainingyears)
print(f"You will be 100 years old in the year: {futureyear}")
#futureage=int(age)+(100-int(age))
#print(futureage)
