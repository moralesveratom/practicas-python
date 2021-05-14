'''Dado el problema anterior del concesionario de autos debemos modificarlo,
1teniendo en cuenta:

1-Ya no sabemos cuantos clientes tendremos,
2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
3-Lo mismo con la cantidad de puertas y los colores.
4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar ttodo
5-Si la cantidad de clientes fue:
--5.1: 0 a 5 personas no hay descuento
--5.2: 6 a 10 personas: hay un descuento del 10%
--5.3: 11 a 50 personas: hay un descuento del 15%
--5.4: Más de 50 personas: El descuento es del 18%
6-Solo se va a mostrar que se vendió al final del programa'''

#global variables
count_price = 0
count_clients = 1
count_general_buys = 0
person_input_marca = ''
person_input_puertas = ''
person_input_color = ''



inicio_compra = int(input('Quiere iniciar la compra? 1:SI 0:NO '))
if inicio_compra:
    count_clients += 1


while count_clients != 0:
    #start
    person_nombre = input('Ingrese su nombre y apellido: ')

    #brand
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

    #doors
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

    #colors
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

    discount_calculator = 0
    #discount
    if count_clients >= 6 and count_clients <= 10:
        discount_calculator += (count_price * 10) / 100
    elif count_clients >= 11 and count_clients <= 50:
        discount_calculator += (count_price * 15) / 100
    elif count_clients > 50:
        discount_calculator += (count_price * 18) / 100

    person_count_total = count_price - discount_calculator
    count_general_buys += person_count_total

    #console
    print(f'\n{person_nombre},')
    print('¡Tu compra fue realizada con exito!\n')
    print('Detalles de la compra:')
    print(f'Auto {person_input_marca} con {person_input_puertas} del {person_input_color}.')
    print(f'\nPrecio Total: ${person_count_total}\n\n')
    count_price = 0
    person_input_marca = ''
    person_input_puertas = ''
    person_input_color = ''


    #Clients
    mas_clientes = int(input('Sigue otro cliente despues de usted? 1:SI 0:NO '))
    if mas_clientes:
        count_clients += 1
    else:
        print(f'Hubo {count_clients - 1} clientes e hicimos ${count_general_buys} pesos hoy.')
        count_clients = 0
