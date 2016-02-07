from fibonacci import *


intro = input("Introduce un numero: ")

newfibo = fibo(intro)

nu = 13

if 55 in newfibo.array():
    print newfibo.lmun()
    print "lo encontre el 55"
elif nu in newfibo.array():
    print newfibo.lnum()
    print "lo encontre el %s" % nu
else:
    print "no se encuentran en dicha serie"
