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

logros_totales = 34
finales_totales = 4

#Funciones para pedir la cantidad de logros y finales que ya se consiguieron
#Bastante inutiles desde mi punto de vista pero pus funciones
def pedir_logros():
    logros_conseguidos = int(input("¿Cuántos logros has conseguido? (0 a 34): "))
    os.system('cls')
    while logros_conseguidos < 0 or logros_conseguidos > 34:
        print("Eso no es posible")
        logros_conseguidos = int(input("¿Cuántos logros has conseguido? (0 a 34): "))
        os.system('cls')
    return logros_conseguidos

def pedir_finales():
    finales_conseguidos = int(input("¿Cuántos finales has conseguido? (0 a 4): "))
    os.system('cls')
    while finales_conseguidos < 0 or finales_conseguidos > 4:
        print("Eso no es posible")
        finales_conseguidos = int(input("¿Cuántos finales has conseguido? (0 a 4): "))
        os.system('cls')
    return finales_conseguidos

#Guarda los logros y finales conseguidos de acuerdo a las funciones
logros_conseguidos = pedir_logros()
finales_conseguidos = pedir_finales()

#Funcion para decirle al usuario que tanto ha progresado
def progreso(logros,finales):
    logros_faltantes = logros_totales - logros
    finales_faltantes = finales_totales - finales

    if logros_conseguidos == logros_totales and finales_conseguidos == finales_totales:
        print("Felicidades lograste completar Sekiro al 100%, ahora ve y completa Dark souls 3 idk")
          
    elif logros_conseguidos != logros_totales and finales_conseguidos == finales_totales:
        print("Ya completaste todos los finales, pero todavia te faltan conseguir",logros_faltantes,"logros")
          
    elif logros_conseguidos != logros_totales and finales_conseguidos != finales_totales:
        print("Te faltan", logros_faltantes,"logros y",finales_faltantes,"finales")   

    else:
        print("No se que hiciste, pero esto no es posible ")

#Define los valores que se usaran en la funcion (progreso)        
progreso(logros_conseguidos, finales_conseguidos )

#En caso de que el usuario ya haya completado el juego, para no mostrar que le falta
if logros_conseguidos != 34:
    print("Haz conseguido", logros_conseguidos,"logros y", finales_conseguidos,"finales")


#Funcion para el porcentaje
def porcentaje(logros):
    porcentaje_juego = (logros / logros_totales) * 100
    print("Haz completado el %.2f" % (porcentaje_juego),"% del juego"  )
    

#El porcentaje de finales realmente no es necesario, ya que cada final tiene un logro#
if logros_conseguidos != logros_totales:

#Define el valor que se usara en la funcion (porcentaje)
    porcentaje(logros_conseguidos)

# Realmente mi codigo ya tiene estrucutras de decisión, por lo que no se que hacer.





