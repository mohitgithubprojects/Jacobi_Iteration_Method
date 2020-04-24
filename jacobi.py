from math import *

a11 = int(input("Enter a11 = "))
a12 = int(input("Enter a12 = "))
a13 = int(input("Enter a13 = "))
b1 = int(input("Enter b1 = "))
a21 = int(input("Enter a21 = "))
a22 = int(input("Enter a22 = "))
a23 = int(input("Enter a23 = "))
b2 = int(input("Enter b2 = "))
a31 = int(input("Enter a31 = "))
a32 = int(input("Enter a32 = "))
a33 = int(input("Enter a33 = "))
b3 = int(input("Enter b3 = "))


if abs(a11)<abs(a12)+abs(a13):
    print("The equations can not satisfy the necessary condition !")
elif abs(a22)<abs(a21)+abs(a23):
    print("The equations can not satisfy the necessary condition !")
elif abs(a33)<abs(a31)+abs(a32):
    print("The equations can not satisfy the necessary condition !")    
else:

    xo = 0
    yo = 0
    zo = 0
    print("\nInitial condition :- ")
    print("\n{}".format(xo))
    print("\n{}".format(yo))
    print("\n{}".format(zo))
    x=1
    y=1
    z=1
    i=1
    while x!=xo and y!=yo and z!=zo:
        x=xo
        y=yo
        z=zo
        m =(b1-(a12*yo)-(a13*zo))
        n =(b2-(a21*xo)-(a23*zo))
        q =(b3-(a31*xo)-(a32*yo))
        print("\n{} Approximation :-".format(i))
        xo = round(m/a11, 2)
        yo = round(n/a22, 2)
        zo = round(q/a33, 2) 
        print("x{} = ".format(i),end="")
        print("{}".format(xo))
        print("y{} = ".format(i),end="")
        print("{}".format(yo))
        print("z{} = ".format(i),end="")
        print("{}".format(zo))
        i=i+1
    print("\n Therefore, ")
    print("\n x = {0:.2f}".format(xo))
    print("\n y = {0:.2f}".format(yo))
    print("\n z = {0:.2f}".format(zo))    
