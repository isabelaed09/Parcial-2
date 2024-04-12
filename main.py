# Punto 1. Se crea un programa para administrar la información médica de pacientes, que permite realizar diversas operaciones, como ingresar nuevos pacientes, obtener informes de afiliación a EPS, obtener información del pacientes respecto al LH según su edad, y también la función de borrar pacientes del programa y salir del programa. Se utilizan variables como 

from funciones import*

#mostrar un menú principal y ejecutar las funciones correspondientes según la opción seleccionada por el usuario.
while True:
    menu = validar_numero("MENÚ PRINCIPAL \n1. Ingresar paciente\n2. Informe de afiliación EPS\n3. Borrar paciente\n4. Salir\n")
    if menu == 1:
        ingresar_paciente()
    elif menu == 2:
        informe_afiliacion_eps()
    elif menu == 3:
        borrar_paciente()
    elif menu == 4:
        break