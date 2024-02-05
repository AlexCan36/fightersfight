

print("Bienvenido a ... ")
print("""
 ___    __       ___  ___  __   __
|__  | / _` |__|  |  |__  |__) /__`
|    | \__> |  |  |  |___ |  \ .__/

 ___    __       ___  
|__  | / _` |__|  |   
|    | \__> |  |  |     
      
""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

# CÃ¡lculo de edad
agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
edad = 2017-agno-1
print()

# CÃ¡lculo de estatura
estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "aÃ±os")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informaciÃ³n. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:
    print("¿Qué acción deseas realizar?")
    print("1. Escribir un mensaje")
    print("2. Modificar nombre en el perfil")
    print("3. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == '1':
        mensaje = input("Escribe tu mensaje: ")
        print("Mensaje ingresado:", mensaje)
    elif opcion == '2':
        nuevo_nombre = input("Ingresa tu nuevo nombre: ")
        print("Nombre actualizado a:", nuevo_nombre)
        nombre = nuevo_nombre
    elif opcion == '3':
        print("Adiós. Programa terminado.")
        continuar = False
    else:
        print("Opción no válida. Ingresa un número válido.")

# Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
