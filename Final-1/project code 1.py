import math

# defining a function to get the speed 
def speed(mo_speed,radius):
    return mo_speed*radius*((2*math.pi)/60)

# defining a function to get the distance walked/ran
def distance(lin_speed,time):
    return time*lin_speed

# defining a function to get the calories burnt
def calories(weight,height,lin_speed,time):
    return ((0.035*weight)+((lin_speed**2/height)*(0.029*weight)))*time/60

# defining a function to get number of steps taken
def steps(height,distance):
    return distance/(height*0.414)

# Getting inputs from user
w0 = float(input('Enter the rate with the motor is rotating(RPM): '))
r = input('Enter the radius of the motor shaft: ')
w = input('Enter the weight: ')
h = input('Enter the height: ')
t = input('Enter the time duration the person was walking/running: ')

# Spliting inputs for check about the units

r1 = r.split()
w1 = w.split()
h1 = h.split()
t1 = t.split()

# Checking the units of radius

if r1[1] == "m":
    r2 = float(r1[0])
elif(r1[1]== "cm"):
    r2 = float(r1[0])/100
elif(r1[1] == "in"):
    r2 = float(r1[0])*0.0254
else:
    print("Wrong input")

# Checking the units of weight

if w1[1] == "kg":
    w2 = float(w1[0])
elif(w1[1] == "lb"):
    w2 = float(w1[0])*0.453592
else:
    print("Wrong input")

# Checking the units of height

if h1[1] == "m":
    h2 = float(h1[0])
elif(h1[1]== "cm"):
    h2 = float(h1[0])/100
elif(h1[1] == "in"):
    h2 = float(h1[0])*0.0254
else:
    print("Wrong input")

# Checking the units of time

if t1[1] == "s":
    t2 = float(t1[0])
elif(t1[1]== "h"):
    t2 = float(t1[0])*3600
elif(t1[1] == "min"):
    t2 = float(t1[0])*60
else:
    print("Wrong input")


V = speed(w0,r2)
D = distance(V,t2)
C = calories(w2,h2,V,t2)
ST = steps(h2,D)

print('The speed is : ',int(V),'m/s')
print('The distance walked/ran is : ',int(D),'m')
print('calories burnt : ',int(C),'cal')
print('Number of steps taken: ',int(ST))

                                                                                                                                                                                                                                                                                                                                                                                 
  
    
    
