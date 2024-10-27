#car value calculator

#initialise my variables
CarValue = 0
Mileage = 0
YearsYouHadCar = 0

#find values for these variables
CarValue = int(input("what is the initial value of your car?: "))
Mileage = int(input("what is the mileage of your car?: "))
YearsYouHadCar = int(input("how long have you had the car in years?: "))

#mileage depreciation (i will be using webuyanycar method for calculating such costs)
if Mileage <= 20000:
    CarValue = CarValue * 0.8
elif Mileage > 20000 and Mileage >= 40000:
    CarValue = CarValue * 0.64

