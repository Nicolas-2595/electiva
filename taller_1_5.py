#punto 5
from math import sin
from math import cos

tetha=float(input('ingrese el angulo de rotacion deseado: '))

cs=cos(tetha/57.3)
sn=sin(tetha/57.3)
cs_ng=cs*(-1)
sn_ng=sn*(-1)

print(sn)
print(cs)

print('rotacion en z: \n')
rot_z=[[cs,sn_ng,0],
       [sn,cs,0],
       [0,0,1]]

for i in rot_z:
    print(i,'\n')

print('rotacion en x: \n')
rot_x=[[1,0,0],
       [0,cs,sn_ng],
       [0,sn,cs]]

for i in rot_x:
    print(i,'\n')

print('rotacion en y: \n')
rot_y=[[cs,0,sn],
       [0,1,0],
       [sn_ng,0,cs]]

for i in rot_y:
    print(i,'\n')