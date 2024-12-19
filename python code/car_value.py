#car value calculator

#initialise my variables
CarValue = 0
Mileage = 0
YearsYouHadCar = 0

#find CarValue
CarValue = int(input("what is the initial value of your car?: "))

#mileage depreciation (i will be using webuyanycar method for calculating such costs)
Mileage = int(input("what is the mileage of your car?: "))
if Mileage <= 20000:
    CarValue = CarValue * 0.8
    CarValue = round(CarValue, 2) #using round() to keep CarValue at 2 decimal places
    print(f"your car value after mileage depreciation is £{CarValue}") #decreases 20% per 20,000 miles
elif Mileage > 20000 and Mileage <= 40000:
    CarValue = CarValue * 0.64
    CarValue = round(CarValue, 2)
    print(f"your car value after mileage depreciation is £{CarValue}")
elif Mileage > 40000 and Mileage <= 60000:
    CarValue = CarValue * 0.512
    CarValue = round(CarValue, 2)
    print(f"your car value after mileage depreciation is £{CarValue}")
elif Mileage > 60000 and Mileage <= 80000:
    CarValue = CarValue * 0.4096
    CarValue = round(CarValue, 2)
    print(f"your car value after mileage depreciation is £{CarValue}")
elif Mileage > 80000 and Mileage <= 100000:
    CarValue = CarValue * 0.32768
    CarValue = round(CarValue, 2)
    print(f"your car value after mileage depreciation is £{CarValue}")
else:
    CarValue = CarValue * 0.262144
    CarValue = round(CarValue, 2)
    print(f"your car value after mileage depreciation is £{CarValue}")

#depreciation by age, this will follow the same code for mileage but with different values
    #values gained from motorway.co.uk
YearsYouHadCar = int(input("how long have you had the car in years?: "))
if YearsYouHadCar == 1 or 2:
    CarValue = CarValue*(0.8**YearsYouHadCar)
    print(f"your car is valued at £{CarValue}")
else:
    CarV = CarValue*(0.8**YearsYouHadCar)
    CarV = CarV*(0.85**YearsYouHadCar)
    print(f"your car is valued at £{CarV}")
    

