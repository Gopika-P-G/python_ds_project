hrs = input("Enter Hours:")

rate=input('enter rat:')

exh=input('enter extra hours:')

try:
    h = float(hrs)
    r = float(rate)
    eh=float(exh)
except:
    print('error please enter the number')

if h<40:
    pay = h*r
    print(pay)
elif h>40:
    pay = 40*r+eh*r*1.5
    print(pay)