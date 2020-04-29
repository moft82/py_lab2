#!/usr/bin/python
import mypkg as pk
n=0
while(n!=3):
    print("1 : conversion")
    print("2 : union/intersection")
    print("3 : quit")
    n=int(input("Select Menu : "))
    if(n==1):
        pk.conversion()
    elif(n==2):
        pk.menu2() 




