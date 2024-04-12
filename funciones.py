import datetime

contador = 0
#El contador se utiliza para asignar un número consecutivo a cada paciente
pacientes = {}
#Un diccionario donde se almacena la información de cada paciente

def codigo(menueps):
    global contador
    if menueps == 1:
        contador += 1
        eps = "EPS SISBEN" + str(contador)
    elif menueps == 2:
        nombre = input("Ingresar el nombre de la EPS: ")
        contador += 1
        eps = "EPS" + nombre + "-" + str(contador)
    return eps

#Genera el código del paciente según si pertenece al SISBEN o a una EPS. Incrementa el contador global cada vez que se agrega un nuevo paciente

def validar_numero(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")
            intentos -= 1
    print("Reingresando al menú principal.")
    return None
#valida que el input sea un número y permite hasta 3 intentos antes de regresar al menú principal.

def validar_fecha(fecha_str):
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha
    except ValueError:
        print("Por favor, ingrese una fecha válida (YYYY-MM-DD)")
        return None
#Valida que el formato de la fecha sea correcto

def ingresar_paciente():
    nombre = input("Ingresar el nombre del paciente: ")
    genero = validar_numero("Ingrese el género del paciente \n 1. hombre \n  2 mujer \n -  ")
    edad = validar_numero("Ingrese la edad del paciente: ")
    if genero == 1:
        genero= "M"
        if edad > 18:
            diagnostico = "1.8 a 8.6 UI/L"
        elif 0 <= edad <= 18:
            diagnostico = "1 a 1.8 UI/L"
    elif genero == 2:
        genero = "F"
        if 0 <= edad <= 18:
            diagnostico = "0 a 5 UI/L"
        elif edad >= 51:
            diagnostico = "5 a 25 UI/L"
        elif edad >= 52:
            diagnostico = "14.2 a 52.3U/L"
    else:
        print("Género inválido.")
        return

    nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    nacimiento_validado = validar_fecha(nacimiento)
    if not nacimiento_validado:
        return

    id = validar_numero("Ingrese el documento de identidad del paciente: ")
    menueps = validar_numero("Escoja una opción para EPS:\n1. SISBEN\n2. EPS\n")
    eps = codigo(menueps)
    lh = "lh" + str(contador)

    pacientes[id] = [nombre, eps, nacimiento_validado, edad, (lh, diagnostico)]

    print(f"Paciente: {nombre} identificado con I.D {id} ingresado exitosamente, su resultado es {diagnostico}.")

    #Permite al usuario ingresar la información de un nuevo paciente, incluyendo nombre, género, edad, fecha de nacimiento, documento de identidad y afiliación a EPS. Luego, guarda esta información en el diccionario de pacientes, además de darle al usuario el diagnóstico según los rango de Lh y edad 

def informe_afiliacion_eps():
    sub_menu = input("Seleccione una opción:\n1) Buscar paciente\n2) Ver cantidad de pacientes totales\n3) Ver cantidad de pacientes menores de 10\n4) Ver cantidad de pacientes mayores de 60\n")
    if sub_menu == "1":
        id_paciente = validar_numero("Ingrese el documento de identidad del paciente que desea buscar: ")
        paciente = pacientes.get(id_paciente)
        if paciente:
            print(f"Paciente encontrado:\nNombre: {paciente[0]}\nEPS: {paciente[1]}\nFecha de nacimiento: {paciente[2].strftime('%Y-%m-%d')}\nEdad: {paciente[3]}\nDiagnóstico: {paciente[4][1]}")
        else:
            print("El paciente con el número de identificación proporcionado no existe en la base de datos.")
    elif sub_menu == "2":
        print(f"La cantidad total de pacientes es: {len(pacientes)}")
    elif sub_menu == "3":
        menores_10 = len(list(filter(lambda x: pacientes[x][3] < 10, pacientes)))
        print(f"La cantidad de pacientes menores de 10 años es: {menores_10}")
    elif sub_menu == "4":
        mayores_60 = len(list(filter(lambda x: pacientes[x][3] > 60, pacientes)))
        print(f"La cantidad de pacientes mayores de 60 años es: {mayores_60}")

#Esta función presenta un submenú con diferentes opciones relacionadas con la información de los pacientes.A demás dependiendo de la opción elegida por el usuario, permite buscar un paciente por su documento de identidad, mostrar la cantidad total de pacientes, la cantidad de pacientes menores de 10 años o la cantidad de pacientes mayores de 60 años meidante la función filter para luego contarlos

def borrar_paciente():
    id_paciente = validar_numero("Ingrese el documento de identidad del paciente a borrar: ")
    if id_paciente in pacientes:
        pacientes.pop(id_paciente)
        print("Paciente eliminado")
    else:
        print("El paciente no está registrado en la base de datos.")

#La función borrar paciente permite al usuario eliminar un paciente, solicitando al usuario el documento del paciente para verificar si existe en el diccionario pacientes y borrarlo, de lo contrario muestra un mensaje indicando que el paciente no está registrado