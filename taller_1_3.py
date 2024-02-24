#punto 3
from math import sqrt
from math import atan
from math import acos

coo_cart_x=float(input('Ingrese la coordenada x: '))
coo_cart_y=float(input('Ingrese la coordenada y: '))
coo_cart_z=float(input('Ingrese la coordenada z: '))

x_e_2=coo_cart_x**2
y_e_2=coo_cart_y**2
z_e_2=coo_cart_z**2
r_c_e_2=x_e_2+y_e_2
r_e_e_2=x_e_2+y_e_2+z_e_2

radio_c=sqrt(r_c_e_2 )
tetha_c=(atan((coo_cart_y/coo_cart_x)))*57.3

print('Cilindricas')
print('radio: ',radio_c)
print('angulo theta: ',tetha_c)


radio_e=sqrt(r_e_e_2)
tetha_e=(atan((coo_cart_y/coo_cart_x)))*57.3
phi=(acos(coo_cart_z/radio_e))*57.3

print('Esfericas: ')
print('radio: ',radio_e)
print('angulo tehta: ',tetha_e )
print('angulo phi: ',phi)