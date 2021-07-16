'''
Dada una concesionaria de autos, 5 clientes van a pedir un auto,
debe preguntarsele:

*Nombre y apellido del comprador.
*Marca
*Puertas
*Color

Marcas posibles y sus precios:

-Ford $100000
-Chevrolet: $120000
-Fiat: $80000

-Por la cantidad de puertas se añade un precio:

-2: $50000
-4: $65000
-5: $78000

Dependiendo del color, se deben sumar:

-Blanco: $10000
-Azul: $20000
-Negro: $30000

Deben imprimirse los datos de cada compra y el precio total.
'''


#primer intento
count_price = 0
person_input_marca = ''
person_input_puertas = ''
person_input_color = ''

for person in range(5):
    person_nombre = input('Ingrese su nombre y apellido: ')


    #marca
    person_marca = input('Ingrese la marca: ')

    if person_marca == 'Ford':
        count_price += 100000
        person_input_marca += 'Ford $100000'
    elif person_marca == 'Chevrolet':
        count_price += 120000
        person_input_marca += 'Chevrolet $120000'
    elif person_marca == 'Fiat':
        count_price += 80000
        person_input_marca += 'Fiat $80000'
    else:
        while person_marca != 'Ford' or person_marca != 'Chevrolet' or person_marca != 'Fiat':
            person_marca = input('Por favor ingrese las marcas disponibles: Ford, Chevrolet, Fiat: ')
            if person_marca == 'Ford':
                count_price += 100000
                person_input_marca += 'Ford $100000'
                break
            elif person_marca == 'Chevrolet':
                count_price += 120000
                person_input_marca += 'Chevrolet $120000'
                break
            elif person_marca == 'Fiat':
                count_price += 80000
                person_input_marca += 'Fiat $80000'
                break

    #cant. puertas
    person_puertas = input('Ingrese la cant. de puertas: ')

    if person_puertas == '2':
        count_price += 50000
        person_input_puertas += '2 puertas +$50000'
    elif person_puertas == '4':
        count_price += 65000
        person_input_puertas += '4 puertas +$65000'
    elif person_puertas == '5':
        count_price += 78000
        person_input_puertas += '5 puertas +$78000'
    else:
        while person_puertas != '2' or person_puertas != '4' or person_puertas != '5':
            person_puertas = input('Por favor ingrese la cant. de puertas permitidas: 2, 4, 5 ')
            if person_puertas == '2':
                count_price += 50000
                person_input_puertas += '2 puertas +$50000'
                break
            elif person_puertas == '4':
                count_price += 65000
                person_input_puertas += '4 puertas +$65000'
                break
            elif person_puertas == '5':
                count_price += 78000
                person_input_puertas += '5 puertas +$78000'
                break

    #color
    person_color = input('Ingrese el color: ')

    if person_color == 'Blanco':
        count_price += 10000
        person_input_color += 'color Blanco +$10000'
    elif person_color == 'Azul':
        count_price += 20000
        person_input_color += 'color Azul +$20000'
    elif person_color == 'Negro':
        count_price += 30000
        person_input_color += 'color Negro +$30000'
    else:
        while person_color != 'Blanco' or person_color != 'Azul' or person_color != 'Negro':
            person_color = input('Por favor ingrese los colores permitidos: Blanco, Azul, Negro ')
            if person_color == 'Blanco':
                count_price += 10000
                person_input_color += 'color Blanco +$10000'
                break
            elif person_color == 'Azul':
                count_price += 20000
                person_input_color += 'color Azul +$20000'
                break
            elif person_color == 'Negro':
                count_price += 30000
                person_input_color += 'color Negro +$30000'
                break

    #console
    print(f'\n{person_nombre},')
    print('¡Tu compra fue realizada con exito!\n')
    print('Detalles de la compra:')
    print(f'Auto {person_input_marca} con {person_input_puertas} del {person_input_color}.')
    print(f'\nPrecio Total: ${count_price}\n\n')

























