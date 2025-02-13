age = int(input("Enter your age:"))

if age <= 3:
    print ("The ticket price is 0$")

elif age <= 10 :
    print ("The ticket price is 5$")

elif age <= 40:
    print ("The ticket price is 10$")

else:
    print("The ticket price is 15$")