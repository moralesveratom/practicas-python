'''
Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
Se pide imprimir el nombre, el apellido y el promedio.
Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".
'''

person_nombre = input('Ingrese su nombre y apellido: ')
person_nota_mat = int(input('Ingrese su nota de matematicas: '))
person_nota_lit = int(input('Ingrese su nota de literatura: '))
person_nota_fis = int(input('Ingrese su nota de fisica: '))
promedio = (person_nota_fis + person_nota_mat + person_nota_lit) / 3

if promedio >= 9:
    print('Aprobado, alumno destacado')
elif promedio > 6:
    print('Aprobado')
elif promedio < 5.99999 and promedio > 4:
    print('A recuperatorio')
else:
    print('Insuficiente')