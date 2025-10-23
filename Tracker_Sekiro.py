import os
"""
================== Listas  =======================================
"""
LOGROS_SIN_FINALES = [
    "Man Without Equal",
    "Sword Saint, Isshin Ashina",
    "Height of Technique",
    "Master of the Prosthetic",
    "Ashina Traveler",
    "All Prosthetic Tools",
    "All Ninjutsu Techniques",
    "Peak Physical Strength",
    "Ultimate Healing Gourd",
    "Master of the Arts",
    "Lazuline Upgrade",
    "Revered Blade",
    "Shinobi Prosthetic",
    "Memorial Mob",
    "Resurrection",
    "Gyoubu Masataka Oniwa",
    "The Phantom Lady Butterfly",
    "Genichiro Ashina",
    "Guardian Ape",
    "Guardian Ape Immortality Severed",
    "Folding Screen Monkeys",
    "Great Shinobi - Owl",
    "Father Surpassed",
    "Corrupted Monk",
    "Gracious Gift of Tears",
    "Isshin Ashina",
    "Demon of Hatred",
    "Great Serpent",
    "Great Colored Carp"
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

    limpiar()
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
            limpiar()
            while respuesta not in ["s", "n"]:
                respuesta = input(
                    f"Responde 's' o 'n'"
                    f" ¿Has conseguido el final '{final}'? (s/n): ").lower()
                limpiar()
            if respuesta == "s":
                logros_conseguidos.append(final)

                for logro in logros_comunes_obligatorios:
                    if logro not in logros_conseguidos:
                        logros_conseguidos.append(logro)

                if final == "Shura":
                    if (logros_unicos_final["Shura"][0]
                        not in logros_conseguidos):
                        logros_conseguidos.append(
                            logros_unicos_final["Shura"][0])
                else:
                    for logro in logros_comunes_no_shura:
                        if logro not in logros_conseguidos:
                            logros_conseguidos.append(logro)
                    if final in logros_unicos_final:
                        if (logros_unicos_final[final][0]
                            not in logros_conseguidos):
                            logros_conseguidos.append(
                                logros_unicos_final[final][0])

    limpiar()
    return logros_conseguidos


def pedir_logros(logros_conseguidos):
    """
    Recibe: la lista logros_conseguidos
    Pregunta por los logros que el usuario ha conseguido.
    Añade un diccionario llamado logros_dependientes;
    éste contiene los logros que requieren de otros para ser obtenidos.
    Añade a la lista logros_conseguidos los logros
    que consiguió el usuario.
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

    limpiar()
    print("--- Actualizar Logros ---")
    print("Vamos a registrar tus logros.")

    for logro in LOGROS_SIN_FINALES:
        if logro in logros_conseguidos:
            continue

        respuesta = input(
            f"¿Has conseguido el logro '{logro}'? (s/n): ").lower()
        limpiar()
        while respuesta not in ["s", "n"]:
            respuesta = input(
                f"Responde 's' o 'n'."
                f" ¿Has conseguido el logro '{logro}'? (s/n): ").lower()
            limpiar()

        if respuesta == "s":
            logros_conseguidos.append(logro)
            if logro in logros_dependientes:
                for sub_logro in logros_dependientes[logro]:
                    if sub_logro not in logros_conseguidos:
                        logros_conseguidos.append(sub_logro)

    limpiar()
    return logros_conseguidos


def mostrar_progreso(logros_conseguidos):
    """
    Recibe: la lista logros_conseguidos
    Crea una nueva lista llamada logros_faltantes
    que contiene los logros que no se encuentran en logros_conseguidos.
    Tambien crea otra lista llamada todos_los_logros que contiene
    todos los logros.....
    por ultimo calcula el porcentaje de logros completados
    """
    limpiar()
    print("--- Resumen de Progreso ---")

    todos_los_logros = LOGROS_TOTALES[0] + LOGROS_TOTALES[1]
    logros_faltantes = [
        logro for logro in todos_los_logros if logro not in logros_conseguidos
    ]

    print(
        f"\nHas conseguido {len(logros_conseguidos)} "
        f"de {len(todos_los_logros)} logros.")

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
================== Funcion auxiliar  ============================
"""


def limpiar():
    """
    Esta funcion no recibe nada
    Simplemente es para hacer el codigo compatble con linux y mac
    En caso de que el usuario este en windows,
    se usa el comando "os.system('cls')"
    Si el usuario no esta en windows,
    se usa el comando "os.system('clear')"
    La funcion no regresa nada
    """

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


"""
================== Bucle principal  ==================================
"""
if __name__ == "__main__":
    logros_conseguidos = []

    while True:
        limpiar()
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
            limpiar()
            print("\nDONT YOU DARE GO HOLLOW")
            print("Juego equivocado (¯ . ¯٥)....")
            print("Buena suerte ")
            break
        else:
            print("Opción no válida (°ロ°) !")
            input("\nPresiona Enter para continuar ˙ᴗ˙")




