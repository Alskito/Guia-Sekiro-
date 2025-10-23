# Tracker-Sekiro
### Contexto
Sekiro: Shadows Die Twice es un videojuego desarrollado por FromSoftware y lanzado en 2019. En este juego, controlas a "Wolf", un shinobi que se embarca en la misión de rescatar a su señor. El juego es considerado "difícil" y requiere de bastante esfuerzo para conseguir todos los logros, siendo estos un total de 34 (uno de los cuales es conseguir todos los logros).

Este programa es un tracker de los logros del juego. Al correr el programa, se despliega un menú en el que se le da la opción al usuario de ver su progreso o de actualizarlo. En caso de que decida actualizar su progreso, se le preguntará al usuario qué logros y finales ya consiguió. Si decide ver su progreso, se le dirá al usuario cuántos logros ya consiguió, cuáles le faltan y el porcentaje de completación.

### Instrucciones
Descarga el archivo y correlo en la terminal con:

`python Tracker_Sekiro.py`

El código se probó en Windows y, en teoría, debería ser funcional tanto en Linux como en Mac. Sin embargo, no sé cuál es el comando para correr el código en esos sistemas y tampoco fue probado en ellos, por lo que preferiría que solo se use con Windows.

NO USAR THONNY, ya que no permite limpiar la consola.

Para usar el menú, simplemente usa los números asignados a cada opción y sigue las instrucciones del programa.

### Logaritmo
El codigo final termino muy diferente al del algoritmo del avance 1.

### Actual:

```
Inicio algoritmo

1. Desplegar menu con 3 opciones
     1. Actualizar logros
     2. Mostrar progreso
     3. Salir
  
- Opcion 1
  1. Se le pregunta al usuario que finales ya consiguio
     - Si si
       Se agrega el final a la lista logros_conseguidos y se agregan los logros dependientes de ese final.
       
     - Si no
       No se añade nada a la lista logros_conseguidos
       
  2. Se le pregunta al usuario cuales logros ya consiguio
     - Si si
       Se agrega el logro a la lista logros_conseguidos y se agregan los logros dependientes de ese logro.
       
     - Si no
       No se añade nada a la lista logros_conseguidos
       
- Opcion 2
  1. Se crea una nueva lista llamada logros_faltantes, que incluye todos los logros y finales que no se encuentran en la lista logros_conseguidos
  2. Se le muestra al usuario el numero de logros que ya consiguio con respecto a el total de logros
  3. Se le muestra al usuario que logros le faltan
  4. Se calcula el porcentaje de completacion y se lo muestra al usuario
  5. Si el usuario ya consiguio todos los logros, se le felicita.
     
- Opcion 3
Termina el programa

Fin del algoritmo
```

### Original: 

```
Inicio algoritmo

1. Preguntar al usuario si es su primera partida
-Si si
    2. Completar el juego
    3. Matar a todos lo jefes principales
    4. Conseguir algun final
    5. Agregar en la variable que logros ya fueron logros_completados
    6. Agregar en la variable que final fue conseguido

-Si no
    2. preguntar al usuario que finales ya completo
        Agregar en la variable que final fue conseguido
    3. Ver que finales faltan por hacer
        - Final Shura
        - Final Purificación
        - Final Retorno
        - Final Inmortal Severed
    4. Preguntar al usuario que final quiere hacer ahora


5. Generar la lista de logros faltantes comparando con los logros que ya se consiguieron
6. Clasificar los logros en categorias
    -Derrota de jefes principales y opcionales
   - Obtención de herramientas prostéticas
   - Mejoras de herramientas prostéticas
   - Habilidades desbloqueadas (árbol de habilidades)
   - Recolección de objetos clave (semillas de calabaza, cuentas de oración, etc.)
   - Logros relacionados con los diferentes finales

7. De acuerdo a los logros faltantes se sugiriria la ruta mas eficiente
    -Que permita obtener el final que eligieron
    -Evitar repetir logros que ya se consiguieron
    -Recomendar la ruta que permita conseguir la mayor cantidad de logros

8. Terminar la partida
9. Actualizar la variable de logros completados
10. Repetir los pasos hasta que la variable de logros faltantes este completa
11. Felicitar al usuario por todo el sufrimiento por el que tuvo que pasar

Fin del algoritmo
```

### Imports
Para este proyecto se importó `os`, el cual se utiliza para interactuar con el sistema operativo. 
solo lo utilice para limpiar la consola y que todo se vea más limpio: 

Primero se utiliza `os.name` para verificar qué sistema operativo se está usando; en caso de que el código se corra en Windows, se utiliza el comando `os.system('cls')` para limpiar la consola; en caso de que se use en cualquier otro sistema operativo, se usa el comando `os.system('clear')`.
