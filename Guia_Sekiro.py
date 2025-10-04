"""
Algoritmo para conseguir todos los logros de sekiro

#variables que voy a usar(probablemente añada mas en el futuro)#

logros_completados: (Que logros ya se consiguieron)
logros_faltantes: (Que logros faltan por conseguir)
finales_completados: (Que finales ya se complearon, en total son 4)
Objetivo_actual: (Que final se quiere conseguir)


#Ahora si el algoritmo#

1. Preguntar al usuario si es su primera partida
-Si si
    2. Completar el juego 
    3. Matar a todos lo jefes principales
    4. Conseguir algun final
    5. Agregar en la variable que logros ya fueron logros_completados
    6. Agregar en la variable que final fue conseguido

-Si no
# Aquí podría usar un ciclo while, ya que la variable no debe tener un valor mayor que 4 ni menor que 0.
# En caso de usar strings, no debe haber un nombre distinto de los 4 finales
    2. preguntar al usuario que finales ya completo     
        Agregar en la variable que final fue conseguido   
    3. Ver que finales faltan por hacer
        - Final Shura
        - Final Purificación
        - Final Retorno
        - Final Inmortal Severed 
    4. Preguntar al usuario que final quiere hacer ahora
        Guardar su respuesta en la variable

5. Generar la lista de logros faltantes comparando con los logros que ya se consiguieron
6. Clasificar los logros en categorias
    -Derrota de jefes principales y opcionales
   - Obtención de herramientas prostéticas
   - Mejoras de herramientas prostéticas
   - Habilidades desbloqueadas (árbol de habilidades)
   - Recolección de objetos clave (semillas de calabaza, cuentas de oración, etc.)
   - Logros relacionados con los diferentes finales

7. De acuerdo a los logros faltantes se sugiriria la ruta mas eficiente
#Personalmente, yo ya complete el juego al 100%, por lo que se cuales son las maneras mas eficientes de conseguir los logros >:D#
    -Que permita obtener el final que eligieron
    -Evitar repetir logros que ya se consiguieron
    -Recomendar la ruta que permita conseguir la mayor cantidad de logros 

8. Terminar la partida
9. Actualizar la variable de logros completados 
10. Repetir los pasos hasta que la variable de logros faltantes este completa 
11. Felicitar al usuario por todo el sufrimiento por el que tuvo que pasar

#Fin del algoritmo#
#Hasta ahora se ve muy sencillo, pero estoy seguro de que voy a sufrir codificando esto#
"""

import os

# Lista de los logros totales
logros_totales = [
    "Man Without Equal", "Ashina Traveler", "Master of the Prosthetic", "Height of Technique", "All Prosthetic Tools",
    "All Ninjutsu Techniques", "Peak Physical Strength", "Ultimate Healing Gourd", "Sword Saint, Isshin Ashina",  "Master of the Arts", 
    "Lazuline Upgrade", "Revered Blade", "Shinobi Prosthetic", "Memorial Mob",  "Resurrection", 
    "Gyoubu Masataka Oniwa", "The Phantom Lady Butterfly", "Genichiro Ashina", "Guardian Ape",  "Guardian Ape Immortality Severed", 
    "Folding Screen Monkeys", "Great Shinobi  - Owl", "Father Surpassed", "Corrupted Monk",  "Gracious Gift of Tears", 
    "Isshin Ashina", "Demon of Hatred", "Great Serpent", "Great Colored Carp"
]

# Chiqui lista de los finales
finales = ["Shura", "Purification", "Return", "Immortal Severed"]

# Pregunta que finales ya se consiguieron y se añaden como logros a un lista nueva llama logros_conseguidos
def pedir_finales(logros_conseguidos):
    print("Primero, qué finales ya conseguiste?")
    for final in finales:
        respuesta = input("¿Has conseguido el final " + final + "? (s/n): ").lower()
        os.system("cls")
        while respuesta not in ["s", "n"]:
            os.system("cls")
            respuesta = input("Responde 's' o 'n'. ¿Has conseguido el final " + final + " ? (s/n): ").lower()
            os.system("cls")
        if respuesta == "s":
            logros_conseguidos.append(final)

# Condicionales para que si ya consiguio un final, se añadan automaticamente los logros que se obtendrian por default 
    if any(final in logros_conseguidos for final in finales):
        logros_conseguidos.extend([logros_totales[8],logros_totales[11], logros_totales[12], logros_totales[15],logros_totales[17], logros_totales[18], 
        logros_totales[20]])

    if finales[1] in logros_conseguidos or finales[2] in logros_conseguidos or finales[3] in logros_conseguidos:
        logros_conseguidos.extend([logros_totales[21], logros_totales[23],logros_totales[24]])

    if "Shura" in logros_conseguidos:
        logros_conseguidos.extend([logros_totales[25]])
        
    if "Purification" in logros_conseguidos:
        logros_conseguidos.extend([logros_totales[22]])

    if  "Return" in logros_conseguidos:
        logros_conseguidos.extend([logros_totales[27]]) 

    os.system("cls")
    return logros_conseguidos

# Pregunta que logros ya conseguiste y los añade a logros_conseguidos
def pedir_logros(logros_conseguidos):
    print("Ahora vamos a registrar los logros.")
         
    for logro in [logros for logros in logros_totales if logros not in logros_conseguidos]:
        respuesta = input("¿Has conseguido " + logro + "? (s/n): ").lower()
        os.system("cls")
        while respuesta not in ["s", "n"]:
                os.system("cls")
                respuesta = input("Responde 's' o 'n'. ¿Has conseguido el final " + logro + " ? (s/n): ").lower()
                os.system("cls")
        if respuesta == "s":
            logros_conseguidos.append(logro)
             
    os.system('cls')
    return logros_conseguidos

# Muestra cuantos logros ya completaste, cuales te faltan y el porcentaje del progreso
def mostrar_progreso(logros_conseguidos):
    logros_faltantes =  [logros for logros in logros_totales + finales if logros not in logros_conseguidos]
    
    print("\nHas conseguido ", len(logros_conseguidos)," de ",len(logros_totales) + len(finales)," logros.")
    
    if len(logros_totales) + len(finales) - len(logros_conseguidos) != 0:
        print("\nTe faltan los siguientes logros:")
        for logros in logros_faltantes:
            print("-", logros)
    else:
        print("\n¡Felicidades! Completaste el juego al 100%")

    porcentaje = (len(logros_conseguidos) / (len(logros_totales) + len(finales))) * 100
    print("\nPorcentaje de logros completados: %.2f" % porcentaje)

# llama a las funciones

logros_conseguidos = []
logros_conseguidos = pedir_finales(logros_conseguidos)
logros_conseguidos = pedir_logros(logros_conseguidos)
mostrar_progreso(logros_conseguidos)


# Hacer este avance tomo demasiadas horas, odio las listas, probablemente matrices me terminen de matar

