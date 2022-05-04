#
# radious of circle inscribed in a tringle
# place here your solution code
#
# from math import *
from math import sqrt
a = int(input("What's the value for side 'a'? "))
b = int(input("What's the value for side 'b'? "))
c = int(input("What's the value for side 'c'? "))

if a > 0 and b > 0 and c > 0:
    semiperimeter = (a + b + c) / 2
    print('Semiperimeter value is: ' + str(semiperimeter))
    try:
        area = sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))
        radius = area / semiperimeter
        print('The radius value is: ' + str(radius))
    except ValueError:
        print('Please enter a valid values')
else:
    print("Invalid side values")