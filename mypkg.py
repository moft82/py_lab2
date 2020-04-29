#!/usr/bin/python

def conversion():
    n="0b"+input("Input Bynary number : ")
    dn=int(n, 2)
    result=format(dn, 'o')
    print("OCT> {}".format(result))
    print("DEC> {}".format(dn))
    result=format(dn, 'x')
    print("HEX> {}".format(result))

def menu2():
    def repl(a):
        a=a.replace(" ","")
        a=a.replace("[","")
        a=a.replace("]","")
        return a

    a=input("1st list : ")
    a=repl(a)
    print("{}".format(a))
    list1=a.split(',')

    b=input("2st list : ")
    b=repl(b)
    print("{}".format(b))
    list2=b.split(",")

    print("union : {}".format(sorted(list(set(list1)|set(list2)))))
    print("intersection : {}".format(sorted(list(set(list1).intersection(list2)))))

if __name__ == '__main__':
    print("test code")
    #conversion()
    menu2()
