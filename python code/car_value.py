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
    print(f"your car value after mileage depreciation is {CarValue}") #decreases 20% per 20,000 miles
elif Mileage > 20000 and Mileage <= 40000:
    CarValue = CarValue * 0.64
    print(f"your car value after mileage depreciation is {CarValue}")
elif Mileage > 40000 and Mileage <= 60000:
    CarValue = CarValue * 0.512
    print(f"your car value after mileage depreciation is {CarValue}")
elif Mileage > 60000 and Mileage <= 80000:
    CarValue = CarValue * 0.4096
    print(f"your car value after mileage depreciation is {CarValue}")
elif Mileage > 80000 and Mileage <= 100000:
    CarValue = CarValue * 0.32768
    print(f"your car value after mileage depreciation is {CarValue}")
else:
    CarValue = CarValue * 0.262144
    print(f"your car value after mileage depreciation is {CarValue}")

#depreciation by age, this will follow the same code for mileage but with different values
    #values gained from motorway.co.uk
if YearsYouHadCar == 1:
    CarValue = CarValue * 0.8 #decreases 20% for the first 2 years
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 2:
    CarValue = CarValue * 0.64
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 3:
    CarValue = CarValue * 0.544 #after year 2, decreases by 15%
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 4:
    CarValue = CarValue * 0.4624
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 5:
    CarValue = CarValue * 0.39304
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 6:
    CarValue = CarValue * 0.334084
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 7:
    CarValue = CarValue * 0.2839714
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 8:
    CarValue = CarValue * 0.24137569
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 9:
    CarValue = CarValue * 0.2051693365
    print(f"your car value after age depreciation is {CarValue}")
elif YearsYouHadCar == 10:
    CarValue = CarValue * 0.174393936
    print(f"your car value after age depreciation is {CarValue}")
else:
    CarValue = CarValue * 0.15 #this value is made up
    print(f"your car value after age depreciation is {CarValue}")

