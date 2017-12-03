# Python script to prove that (a+b)2 = a2+2ab+b2

def rhs(a,b):
    return (a+b)**2

print rhs(2,3)

def lhs(c,d):
    return (c*c+2*c*d+d*d)

print lhs(2,3)

if (lhs==rhs):

   print("hence proved")