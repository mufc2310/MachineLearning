#wap to percentage form user & print frist class if percentage is above 60, print second class if percentage is between 40 and 60, print KT is percentage is less than 40.


per=input("Enter the percentage :")

per=float(per)

if(per>=60):
    print("First class")

elif(per<60 and per>=40):
    print("Second class")

else:
    print("KT")
