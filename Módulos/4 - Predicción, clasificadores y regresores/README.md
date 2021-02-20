# Actividad colaborativa
## Enunciado

## Realización
Buenas a todos.

Os dejo un artículo donde la nutrición es objeto de estudio dentro de un sistema un poquito más complejo en el que por desgracia tengo algo de experiencia, diabetes. Espero que a Andrés no le pille, tendrá que empezar a cuidarse.

En el interior del paper he subrayado las partes que he considerado más interesantes, no por importancia ni nada relativo, sino porque simplemente bajo mi criterio me resultan curiosas, y me gustaría comentarlas en la mesa redonda del viernes.

Sobre el tema, yo distingo 3 grandes bloques dentro de este "macrosistema". Dentro de ellos voy a citar (también desde mi punto de vista) puntos clave o a hacia donde debería tender la resolución del problema para los diabéticos:

1. Análisis de la nutrición basada en sistemas inteligentes: 

Clasificación de los platos de comida a través de imágenes, infiriendo cantidades de los 3 macronutrientes (grasas, proteínas y carbohidratos)
Recomendación genérica en función de numerosas variables que forman parte del sistema (preferencias, objetivos, patologías como celiaquía, etc...)
2. Monitorización multivariable: 

Actividad física
Niveles de glucosa en este caso, pudiéndose tener en cuenta otras patologías.
Cantidad de macronutrientes ingeridos, bien como resultado de una buena clasificación de nuestro sistema a partir de una foto, o introduciendo manualmente en el caso de no ser una opción válida.
 3. Ayuda (solo recomendación) en la toma de decisión.

Considero que la tendencia de este tipo de sistemas es a poder hacer este análisis multivariable de manera autónoma, y que el usuario pueda confirmar o seguir estas directrices siempre aprobadas por un médico, o por el mismo usuario en su defecto. Principalmente orientado (aunque creo que habría más opciones) a:

Qué, cuanto y cuando comer.
Cuanto y cuando inyectar la insulina.
 

RESUMEN DEL DOCUMENTO:

- En primer lugar, se hace una introducción y una revisión de la literatura relacionada con los sistemas de control de diabetes y nutrición, reseñando puntos fuertes y débiles o ausentes en cada uno.

- Posteriormente describen su sistema en arquitectura y funcionalidad, conformado también de manera muy resumida por:

El desarrollo de un modelo de aprendizaje automático para el sistema de recomendación de alimentos para diabéticos utilizando el algoritmo K-Nearest Neighbour (KNN).
La programación y notificación a los pacientes diabéticos. Junto con el seguimiento de la actividad de los pacientes diabéticos.
Una interfaz visual interactiva
- En cuanto a la implementación y testeo, utilizan:

Combinan capas de Inception e Imagenet (si no lo he entendido mal).
Un servicio Flask escrito en Python.
Google Firebase para la aplicación Android y web.
 

 

CONCLUSIONES:

En los dos primeros apartados creo que la parte más compleja es poder contar con un dataset con número suficiente de datos de calidad, sobre todo en cuanto a la actividad física, que considero que a día de hoy es el más complejo a nivel de usuario. El hecho de contar con algún reloj o pulsera inteligente podría facilitar esta tarea.
La monitorización de glucosa gracias a los nuevos sistemas es algo creo que bastante accesible, la complejidad creo que podría recaer más en la disponibilidad del dato y en la vinculación con el resto de variables.
Todos los datos anteriores, creo que deberían servir de realimentación al modelo continuamente por los datos propios de cada usuario, sobre todo para "recalcular" la predisposición del cuerpo en el momento actual (ej: la sensibilidad a la insulina)
 
 
# Tarea
## Enunciado

## Realización
