import math
s,a,deg = input().split()
r = 6440
a = int(a)
if deg == 'min':
    a = a / 60
if a > 180:
    a = 360 - a

dia = (r + int(s))*2  #直徑
rad = r + int(s)
arc = dia*math.pi*(a/360)

print('{:6f}'.format(arc),end = ' ')


c = rad**2 + rad**2 - 2*rad*rad *math.cos(math.radians(a))
#print(c)
c = c**0.5
print('{:6f}'.format(c))

