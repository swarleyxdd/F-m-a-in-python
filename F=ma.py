f = input("Force: ")
m = input("Mass: ")
a = input("Acceleration: ")
if  f.isdigit():
    f=int(f)
    if  m.isdigit():
        m=int(m)
        if  a.isdigit():
            a=int(a)
        else:
            f=int(f)
            m=int(m)
            a=f/m
            print("Acceleration: ",a)
    else:
        f=int(f)
        a=int(a)
        m=f/a
        print("Mass: ",m)
else:
    m=int(m)
    a=int(a)
    f= m*a
    print("Force: ",f)