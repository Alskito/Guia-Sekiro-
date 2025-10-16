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
# Aquí podría usar un ciclo while
ya que la variable no debe tener un valor mayor que 4 ni menor que 0.
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
Personalmente, yo ya complete el juego al 100%
por lo que se cuales son las maneras mas eficientes de conseguir los logros >:D#
    -Que permita obtener el final que eligieron
    -Evitar repetir logros que ya se consiguieron
    -Recomendar la ruta que permita conseguir la mayor cantidad de logros

8. Terminar la partida
9. Actualizar la variable de logros completados
10. Repetir los pasos hasta que la variable de logros faltantes este completa
11. Felicitar al usuario por todo el sufrimiento por el que tuvo que pasar

#Fin del algoritmo#
"""

"""
(づ ᴗ _ᴗ)づ Proyecto python
Tracker de los logros obtenidos en sekiro
El programa le pregunta al usuario que logros a conseguido
dependiendo de sus respuestas le dice que logros le faltan
y que tanto del juego a completado
"""


import os
"""
================== Listas  =======================================
"""
LOGROS_SIN_FINALES = [
    "Man Without Equal",
    "Sword Saint, Isshin Ashina",
    "Height of Technique",
    "Master of the Prosthetic",
    "Ashina Traveler", "All Prosthetic Tools", "All Ninjutsu Techniques",
    "Peak Physical Strength", "Ultimate Healing Gourd", "Master of the Arts",
    "Lazuline Upgrade", "Revered Blade", "Shinobi Prosthetic", "Memorial Mob",
    "Resurrection", "Gyoubu Masataka Oniwa", "The Phantom Lady Butterfly",
    "Genichiro Ashina", "Guardian Ape", "Guardian Ape Immortality Severed",
    "Folding Screen Monkeys", "Great Shinobi - Owl", "Father Surpassed",
    "Corrupted Monk", "Gracious Gift of Tears", "Isshin Ashina",
    "Demon of Hatred", "Great Serpent", "Great Colored Carp"
]

FINALES = ["Shura", "Purification", "Return", "Immortal Severed"]

LOGROS_TOTALES = [LOGROS_SIN_FINALES, FINALES]

"""
================== Funciones  =======================================
"""
def pedir_finales(logros_conseguidos):
    """
    Recibe: la lista logros_conseguidos
    Pregunta por los finales que el usuario ha conseguido.
    Añade los finales conseguidos a la lista logros_conseguidos 
    Dependiendo del final que haya conseguido, se añaden 
    los logros correspondientes a la lista logros_conseguidos
    Por último, devuelve la lista logros_conseguidos.
    """
    
    os.system("cls")
    print("--- Finales Conseguidos ---")
    print("Primero, ¿qué finales ya conseguiste?")

    logros_comunes_no_shura = [
        "Sword Saint, Isshin Ashina", "Great Shinobi - Owl",
        "Corrupted Monk", "Gracious Gift of Tears"
    ]
    logros_comunes_obligatorios = [
        "Revered Blade", "Shinobi Prosthetic", "Gyoubu Masataka Oniwa",
        "Genichiro Ashina", "Guardian Ape", "Folding Screen Monkeys"
    ]
    logros_unicos_final = {
        "Shura": ["Isshin Ashina"],
        "Purification": ["Father Surpassed"],
        "Return": ["Great Serpent"]
    }

    for final in FINALES:
        if final not in logros_conseguidos:
            respuesta = input(
                f"¿Has conseguido el final '{final}'? (s/n): ").lower()
            os.system("cls")
            while respuesta not in ["s", "n"]:
                respuesta = input(
                    f"Responde 's' o 'n'. ¿Has conseguido el final '{final}'? (s/n): ").lower()
                os.system("cls")
            if respuesta == "s":
                logros_conseguidos.append(final)

                for logro in logros_comunes_obligatorios:
                    if logro not in logros_conseguidos:
                        logros_conseguidos.append(logro)

                if final == "Shura":
                    if logros_unicos_final["Shura"][0] not in logros_conseguidos:
                        logros_conseguidos.append(
                            logros_unicos_final["Shura"][0])
                else:
                    for logro in logros_comunes_no_shura:
                        if logro not in logros_conseguidos:
                            logros_conseguidos.append(logro)
                    if final in logros_unicos_final:
                        if logros_unicos_final[final][0] not in logros_conseguidos:
                            logros_conseguidos.append(
                                logros_unicos_final[final][0])

    os.system("cls")
    return logros_conseguidos


def pedir_logros(logros_conseguidos):
    """
    Recibe: la lista logros_conseguidos
    Pregunta por los logros que el usuario ha conseguido. 
    Añade un diccionario llamado logros_dependientes; 
    éste contiene los logros que requieren de otros para ser obtenidos. 
    Añade a la lista logros_conseguidos los logros que consiguió el usuario. 
    En caso de que se haya conseguido un logro dependiente, 
    se añaden los logros correspondientes. 
    Por último, devuelve la lista logros_conseguidos.
    """
    logros_dependientes = {
        "Man Without Equal": [
            "Gyoubu Masataka Oniwa",
            "The Phantom Lady Butterfly",
            "Genichiro Ashina",
            "Guardian Ape",
            "Guardian Ape Immortality Severed",
            "Folding Screen Monkeys",
            "Great Shinobi - Owl",
            "Father Surpassed",
            "Corrupted Monk",
            "Sword Saint, Isshin Ashina",
            "Isshin Ashina",
            "Demon of Hatred",
            "Great Colored Carp"],
        "Sword Saint, Isshin Ashina": [
            "Gyoubu Masataka Oniwa",
            "Genichiro Ashina",
            "Guardian Ape",
            "Folding Screen Monkeys",
            "Great Shinobi - Owl",
            "Corrupted Monk"],
        "Height of Technique": ["Master of the Arts"],
        "Master of the Prosthetic": [
            "All Prosthetic Tools",
            "Lazuline Upgrade"]}

    os.system("cls")
    print("--- Actualizar Logros ---")
    print("Vamos a registrar tus logros.")

    for logro in LOGROS_SIN_FINALES:
        if logro in logros_conseguidos:
            continue

        respuesta = input(f"¿Has conseguido '{logro}'? (s/n): ").lower()
        os.system("cls")
        while respuesta not in ["s", "n"]:
            respuesta = input(
                f"Responde 's' o 'n'. ¿Has conseguido '{logro}'? (s/n): ").lower()
            os.system("cls")

        if respuesta == "s":
            logros_conseguidos.append(logro)
            if logro in logros_dependientes:
                for sub_logro in logros_dependientes[logro]:
                    if sub_logro not in logros_conseguidos:
                        logros_conseguidos.append(sub_logro)

    os.system("cls")
    return logros_conseguidos


def mostrar_progreso(logros_conseguidos):
    """
    Recibe: la lista logros_conseguidos
    Crea una nueva lista llamada logros_faltantes
    que contiene los logros que no se encuentran en logros_conseguidos.
    Tambien crea otra funcion llamada todos_los_logros que contiene
    todos los logros.....
    por ultimo calcula el porcentaje de logros completados
    """
    os.system("cls")
    print("--- Resumen de Progreso ---")

    todos_los_logros = LOGROS_TOTALES[0] + LOGROS_TOTALES[1]
    logros_faltantes = [
        logro for logro in todos_los_logros if logro not in logros_conseguidos
    ]

    print(
        f"\nHas conseguido {len(logros_conseguidos)} de {len(todos_los_logros)} logros.")

    if not logros_faltantes:
        print("\n¡Felicidades! ¡Completaste el juego al 100%! ＼( ^▽^ )／")
        print("Ahora sal y toca pasto (￢_￢)")
    else:
        print("\nTe faltan los siguientes logros:")
        for logro in sorted(logros_faltantes):
            print(f"- {logro}")

    porcentaje = (len(logros_conseguidos) / len(todos_los_logros)) * 100
    print(f"\nPorcentaje de logros completados: {porcentaje:.2f}%")


"""
================== Bucle principal  =======================================
"""
if __name__ == "__main__":
    logros_conseguidos = []

    while True:
        os.system("cls")
        print("--- Tracker de Logros de Sekiro ---")
        print("(Si cierras el programa se reinicia el registro)")
        print("\nElige una opción:")
        print("1. Actualizar logros conseguidos")
        print("2. Ver mi progreso")
        print("3. Salir")

        opcion = input("\n> ")

        if opcion == '1':
            logros_conseguidos = pedir_finales(
                logros_conseguidos)
            logros_conseguidos = pedir_logros(logros_conseguidos)
            print("Logros actualizados (ദ്ദി˙ᗜ˙) ")
            input("\nPresiona Enter para volver al menú ˙ᴗ˙")
        elif opcion == '2':
            mostrar_progreso(logros_conseguidos)
            input("\nPresiona Enter para volver al menú ˙ᴗ˙")
        elif opcion == '3':
            os.system("cls")
            print("\nDONT YOU DARE GO HOLLOW")
            print("Juego equivocado (¯ . ¯٥)....")
            print("Buena suerte ")
            break
        else:
            print("Opción no válida (°ロ°) !")
            input("\nPresiona Enter para continuar ˙ᴗ˙")




