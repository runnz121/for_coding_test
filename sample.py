car = input()

i = 0
while i <len(car):
    if "i" in car:
        car = car.replace("i",'c')
        print(car)
        i = 0
    else:
        i +=1

print(car)