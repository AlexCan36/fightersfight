

print("Welcome to ... ")
print("""
 ___    __       ___  ___  __   __  
|__  | / _` |__|  |  |__  |__) /__` 
|    | \__> |  |  |  |___ |  \ .__/ 
                                    
 ___    __       ___                
|__  | / _` |__|  |                 
|    | \__> |  |  |       

""")

nombre = input("Whats your name? ")
print()
print("Hi ", nombre, ", Welcome to Fighters Fight !")
print()

# Profile
agno = int(input("Whats your birht year? "))
edad = 2017-agno-1
print()


estatura = float(input("Whats your height?"))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )


num_amigos = int(input("How many fighters do you know? "))


print()
print("Nice,", nombre, ". Lets setup ypur profile")
print("--------------------------------------------------")
print("Name:  ", nombre)
print("Age:    ", edad, "years")
print("Height:", estatura_m, "meters", estatura_cm, "inches")
print("Friends:  ", num_amigos)
print("--------------------------------------------------")
print("Thanks for making a profile, enjoy and discussed upcoming matches")
print()

#Use bool to continue 
continuar = True

#While continue or quit
while continuar:
    print("What you wanna do?")
    print("1. Write a message")
    print("2. Change your username")
    print("3. Quit")

    opcion = input("Input the number of your selected option: ")

    if opcion == '1':
        mensaje = input("Write a message: ")
        print("Message is:", mensaje)
    elif opcion == '2':
        nuevo_nombre = input("Choose your new username: ")
        print("New username is:", nuevo_nombre)
        nombre = nuevo_nombre
    elif opcion == '3':
        print("Bye , See you next time.")
        continuar = False
    else:
        print("Option not valid , Select one of our options")

# exit message
print("Thanks for using us , see you soon")
