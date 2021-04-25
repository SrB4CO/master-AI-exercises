Imagina que quieres saber cuál es la probabilidad de que tu equipo gane un partido en función de que el entrenador alinee a ciertos jugadores. Vamos a muestrear sólo un jugador por cada puesto de la defensa, mediocampo y delantera del Real Madrid de las tres Champions seguidas: Sergio Ramos, Luka Modric y Cristiano Ronaldo. El dataset estaría compuesto por variables binarias indicando si juega cada jugador, y la variable a predecir sería si el Real Madrid ganó ese partido. Por ejemplo [0, 1, 1] -> [1] significaría que el Madrid ganó el partido con Modric y Cristiano pero sin Ramos.

 

Esto podría ser extensible a todos los jugadores de la plantilla del Madrid, aunque para simplificar, usaremos sólo esos jugadores. Vamos a ver cómo la red neuronal más simple posible nos permite no sólo predecir el resultado de un partido en función de qué jugadores estén alineados, sino también la importancia que tiene la presencia de cada jugador.

 

Traduciendo el enunciado al mundo de las redes neuonales, en esta práctica implementaremos el perceptrón simple para clasificación binaria. Será necesario implementar este algoritmo utilizando dos de las funciones de activación que hemos visto en el módulo: la función escalón, y la función sigmoide.

 

Proporcionamos un esqueleto de la clase PerceptronSimple con las siguientes funciones:

__init__: Constructor de la clase.
escalon: Función escalón
sigmoide: Función sigmoide
derivadaSigmoide: Derivada de la función sigmoide
forward: Paso hacia adelante de información
fit: Entrenamiento usando Descenso de Gradiente Estocástico
predict: Predicción de nuevos ejemplos. Similar a forward, pero considerando que se le pueden pasar varios ejemplos a predecir simultáneamente
Consideraciones:

En el caso de utilizar la función escalón, la actualización de los pesos no se realiza por el método del descenso del gradiente sino que se realiza como vimos en el apartado de Perceptrón simple del módulo.
En el caso de la función sigmoide, damos la actualización de los pesos ya completada. En este caso habrá que rellenar el código para la función sigmoide y la de su derivada.
Parte extra

En la plantilla que os hemos entregado sólo aparece el esqueleto de todo lo que debéis hacer sin ningún añadido. Os sugerimos implementar mejoras como la monitorización de resultados, probar con un dataset que encontréis por internet o incluir nuevas funciones de activación a vuestra red.