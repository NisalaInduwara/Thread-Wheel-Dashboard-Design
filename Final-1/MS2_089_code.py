# To run program with custom parameters - you can give the parameters in any order
# python E18_G_XXX.py --motor 4 --radius "0.09 m" --height "170 cm" --weight "100 lb"

# To run program with default parameters
# python E18_G_XXX.py


# GP 106 : Group Project
# Group 089 : E/18/265, E/18/266, E/18/267
# Code of the second milestone


# importing function
import time 
import argparse
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
    return (distance/(height*0.414))*2



# Don't change the the code below this point
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=3)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
        
    args=args.parse_args()

# Don't change the the code above this point

# Getting the initial time 
ini_time = time.time()

# Spliting inputs for check about the units

r = args.radius.split()
w = args.weight.split()
h = args.height.split()


# Checking the units of radius

if r[1] == "m":
    r1 = float(r[0])
elif(r[1]== "cm"):
    r1 = float(r[0])/100
elif(r[1] == "in"):
    r1 = float(r[0])*0.0254
else:
    print("Wrong input")


# Checking the units of weight

if w[1] == "kg":
    w1 = float(w[0])
elif(w[1] == "lb"):
    w1 = float(w[0])*0.453592
else:
    print("Wrong input")



# Checking the units of height

if h[1] == "m":
    h1 = float(h[0])
elif(h[1]== "cm"):
    h1 = float(h[0])/100
elif(h[1] == "in"):
    h1 = float(h[0])*0.0254
else:
    print("Wrong input")




# Calling functions to get the values

while True:
    current_time = time.time()
    t = current_time - ini_time
    wo = args.motor_rate
    V = speed(wo,r1)
    D = distance(V,t)
    C = calories(w1,h1,V,t)
    ST = steps(h1,D)
    

    # Printing output values 
    print(int(V),'m/s')
    print(int(D),'m')
    print(int(C),'cal')
    print(int(ST))
    




    
