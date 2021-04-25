
# Tarea
BetSentiment.com es una empresa que ofrece un análisis de la opinión de los aficionados sobre el fútbol inglés e internacional. Analizan miles de tweets todos los días para extraer el estado de ánimo general asociado con los equipos y jugadores, utilizando algoritmos de inteligencia artificial NLP.

Para esta tarea hemos escogido uno de sus datasets gratuitos. Concretamente miles de tweets, en inglés, publicados entre Mayo y Septiembre de 2018. Estos tweets hablan sobre el Mundial de Fútbol de ese mismo año celebrado en Rusia, con el sentimiento asociado a cada mensaje.


 1.- (Mínimo)

Implementar algoritmo de clasificación, que permita detectar el sentimiento de un mensaje.


Detallar las diferentes fases del proceso:

- EDA (exploratory data analysis). Análisis de los datos en bruto con el fin de conseguir información que sea útil para las siguientes fases de desarrollo. Posteriormente se puede realizar una limpieza datos que únicamente aportan ruido: eliminación de nuelos, etc..

(Extrae al menos dos características estadísticas del texto)

- Preprocesado. En esta etapa utilizar las técnicas vistas en el manual que se crean convenientes: Lemmatization, stopwords, normalización, etc…

(Utiliza al menos una técnica)
 
- Extracción de features (tokenización). Tal como habéis visto en el manual, se trata de dividir el texto en ngramas y asignarle una representación numérica para que nuestro modelo pueda lidiar con los datos.  Hay multitud de librerías que nos facilitan esta tarea.

- Modelado. Antes de nada, importantísimo separar conjunto de datos de entrenamiento y de validación. Elegir e implementar el modelo que creas adecuado para la solución de este problema. Se busca maximizar el poder predictivo y calidad del modelo.

(Consejo): Lo mejor es que juegues “cacharreando” con uno u otro… Trastea los hiperparámetros, compara métricas, revisa comportamiento y resultados. Si sigues este proceso el apartado (2) lo tienes prácticamente hecho! : )

- Evaluación y conclusiones. En base a los resultados y las métricas obtenidas. Evaluar el rendimiento predictivo de nuestro modelo. Graficar métricas puede ser muy útil y revelador. ¿Qué accuracy es la esperada? ¿Qué métrica es más representativa para indicar la calidad de mi modelo?


2.- (Extra)

 Implementar varias soluciones y comprobar resultados con el fin de afinar métricas. Detallar ventajas e inconvenientes de unas soluciones frente a otras.

**Objetivo:**

El objetivo de la tarea es afianzar conocimientos y perfeccionar uso de técnicas y procedimientos propios de este tipo de problemas. Concretamente la clasificación de textos. Y aprender a maximizar el poder de predicción (calidad) de nuestro modelo.
