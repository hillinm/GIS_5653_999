age = input("What is the age of the visitor? ")

if int(age) <= 5:
    print("Admission is free!")
elif int(age) >= 6 and int(age) < 12:
    print("Admission is $6")
else:
    print("Admission is $12")