from graphics.rect import *
from graphics.circle import *
from graphics.dgraphics.sphere import *
from graphics.dgraphics.cuboid import *

print("rectangle")
l=int(input("enter len:"))
b=int(input("enter bre:"))
print("area of rectangle=",Rectarea(l,b))
print("perimeter of rectangle=",Rectperimeter(l,b))

print("circle")
r=int(input("enter the radius of the circle:"))
print("area of circle:",circlearea(r))
print("perimeter of circle=",circleperimeter(r))

print("cuboid")
l=int(input("enter len:"))
b=int(input("enter bre:"))
h=int(input("enter height:"))
print("area of cuboid=",cuboidArea(l,w,h))
print("perimeter of cuboid:", cubperimeter(l,w,h))

print("sphere")
r=int(input("enter the radius of the sphere:"))
print("area of sphere:",spherearea(r))
print("perimeter of sphere:",sphereperimeter(r))
