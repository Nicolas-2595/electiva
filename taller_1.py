#punto 1
import numpy as  np
import numpy.linalg as lg
vector_1=[]
vector_2=[]
vector_suma=[]
vector_resta=[]
vector_punto=[]
vector_division=[]

a=int(input('Ingrese el tamaño del vector: '))

#vector 1
for i in range(0,a):
    b=float(input('ingrese el valor '+str(i+1)+' para el primer vector :'))
    vector_1.append(b)

#vector 2
for i in range(0,a):
    b=float(input('ingrese el valor '+str(i+1)+' para el segundo vector :'))
    vector_2.append(b)

print('vector 1: ',vector_1)
print('vector 2: ',vector_2)

#suma de vectores'
for i in range(0,a):
    vector_suma.append(vector_1[i]+vector_2[i])

#resta de vectores
for i in range(0,a):
    vector_resta.append(vector_1[i]-vector_2[i])

#producto punto
for i in range(0,a):
    vector_punto.append(vector_1[i]*vector_2[i])

#division de vectores
for i in range(0,a):
    vector_division.append(vector_1[i]/vector_2[i])

print('vector suma: ',vector_suma)
print('vector resta: ',vector_resta)
print('producto punto: ',sum(vector_punto))
print('producto cruz: ', np.cross(vector_1,vector_2))


#punto 2

lista_1=[]
lista_2=[]
matrix_1=[]
matrix_2=[]
matrix_suma=[]
matrix_resta=[]
mtrx_mult=[]
mtrx_div=[]

c=int(input('ingrese la cantidad de filas: '))
d=int(input('ingrese la cantidad de columnas: '))

for i in range(c):
    lista_1=[float(input('dame el dato de la matriz 1: ')) for j in range(d)]
    matrix_1.append(lista_1)
    
for i in range(c):
    lista_2=[float(input('dame el dato de la matriz 2: ')) for j in range(d)]
    matrix_2.append(lista_2)

#matriz 1
print('Matriz 1: ')
for i in matrix_1:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#matriz 2
print('Matriz 2: ')
for i in matrix_2:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#suma
for i in range (c):
    mtrx_mas=[]
    for j in range(d):
        mtrx_mas.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_suma.append(mtrx_mas)

print('suma de mariz: ',)
for i in matrix_suma:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#resta
for i in range (c):
    mtrx_menos=[]
    for j in range(d):
        mtrx_menos.append(matrix_1[i][j] - matrix_2[i][j])
    matrix_resta.append(mtrx_menos)

print('resta de mariz: ',)
for i in matrix_resta:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#producto punto

for i in range(len(matrix_1)):
    mtrx_mult.append([])
    for j in range(len(matrix_2[0])):
        mtrx_mult[i].append(0)

for i in range(c):
    for j in range(d):
        for k in range(d):
            mtrx_mult[i][j]+=matrix_1[i][k] *matrix_2[k][j]

print('producto matriz: ') 
for i in mtrx_mult:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#division de matrices
print('inversion de matriz 2: ')
matrix_2_inv=lg.inv(matrix_2)
mtrx_inv=matrix_2_inv.tolist()
print(mtrx_inv)

for i in range(len(matrix_1)):
    mtrx_div.append([])
    for j in range(len(mtrx_inv[0])):
        mtrx_div[i].append(0)

for i in range(len(matrix_1)):
    for j in range(len(mtrx_inv[0])):
        for k in range(len(matrix_1[0])):
            mtrx_div[i][j]+=matrix_1[i][k] *mtrx_inv[k][j]

print('division matriz: ') 
for i in mtrx_div:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')