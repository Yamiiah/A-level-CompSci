#3 categories for repair difficulty
#easy - tyre change, oil change, spark plugs replaced, bulb replacements, liquid top ups £10-20 10-30 min
#med - parts replacement (brakes, bumpers, fenders), dent removal, remapping £20-200 30-120 min
#hard - engine replacement, major body damage, clutch, timing belt, alternator £100-1000 120-480 min
#labour of £15/hr
#for med to hard repairs, flat fee of £50
labour = 15
time = 0
diff = input("choose the difficulty of your repair [easy,med,hard]")
diff = diff.upper()
if diff == 'EASY':
    type_e =[]

elif diff == 'MED' or 'MEDIUM':
    type_m = []

else:
    type_h = []
    

