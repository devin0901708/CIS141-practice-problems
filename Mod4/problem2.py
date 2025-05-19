'''
The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold.
If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
'''
light = input("Value of light. ")

try:
    int_light = int(light)
except ValueError:
    print("please use digits only.")

if int_light <= 8:
    print("Headlights On")
else:
    print("Headlights Off")
