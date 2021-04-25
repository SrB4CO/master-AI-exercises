# Colaborativa
## Enunciado
En la actualidad las redes sociales, son una verdadera mina de información. Por lo que automáticamente se convierten en una de las principales fuentes de datos para algoritmos de Procesamiento del Lenguaje Natural.

A diario millones de interacciones suceden en ellas generando: visibilidad, viralización, creación de opinión y poder de persuasión entre otra... Dichas herramientas son extremadamente útiles.

¿Se te ocurre alguna propuesta en la que se pudiera aprovechar este fenómeno?

- Indica en qué ámbito deportivo lo aplicarías.

- Cómo extraerías y procesarías dicha información.

- De qué tecnología te servirías para ello: infraestructura, recursos, algoritmos NPL utilizados…

- ¿Existe algún ejemplo real donde se aplique tu propuesta? 

El objetivo es que entre todos descubramos la importancia de un buen aprovechamiento y uso de la información presente en las redes sociales. 

## Realización 
A continuación, desgloso los distintos puntos de la actividad sobre una pequeña idea al vuelo sobre cómo se podría utilizar Twitter para extraer información que pudiera ser interesante para una plataforma de resultados o de noticias.

 

- Indica en qué ámbito deportivo lo aplicarías.

Dentro del mundo del deporte, creo que sería aplicable a más de uno, pero para concretar enmarco este supuesto desarrollo en el mundo del fútbol. 

La idea consiste en utilizar información publicada por usuarios de diversa índole en Twitter para:

1. Extracción de resultados en categorías con un menor grado de repercusión, como no profesionales o de fútbol base.

2. Análisis de impacto y sentimiento de para poder detectar temas de interés actual para la generación de noticias.

 

- Cómo extraerías y procesarías dicha información.

La extracción la realizaría a través de la librería Tweepy que nos mostró Rodrigo en una de las sesiones.

Para ambos casos se realizarían manualmente listas de suscripción sobre las cuentas que puedan ser sujeto de estudio, tanto para resultados como para información.

Donde el procesamiento lo realizaría utilizando algunos de los recursos vistos durante el módulo como expresiones regulares, listas de palabras representativas o tokenizadores. 

1. Resultados: 

Búsqueda de palabras clave como resultado, final, marcador, etc.
Búsqueda  y validación de caracteres numéricos a partir de varias fuentes, tales como equipos implicados, federaciones, seguidores fiables, etc.
Análisis y detección de nombres de equipo para asociar el marcador. Importante tener en cuenta la posición dentro del texto.
2. Información:

Análisis de la actividad de los tweets.
Análisis de sentimiento para los tweets más virales.
 

- De qué tecnología te servirías para ello: infraestructura, recursos, algoritmos NPL utilizados…

Desde mi actual ignorancia (que pretendo ir corrigiendo en los próximos días) optaría por utilizar BERT como algoritmo NPL en el que basar el trabajo.

Dado que según he entendido durante el módulo, tiene bastantes posibilidades, versiones y versatilidad, sin olvidar que es de Google. Por lo que tiene un considerable respaldo de calidad.

En cuanto a infraestructura y recursos, a priori optaría por utilizar la gama de servicios a día de hoy disponibles en la nube dada la ausencia de detalles en el contexto, y también pensando en una posible escalabilidad futura.

 

-  ¿Existe algún ejemplo real donde se aplique tu propuesta? 

En alguna ocasión he escuchado a Manuel Heredia, CEO y fundador de BeSoccer, hablar sobre estos temas para la conformación de su base de datos. Comenta que utilizan datos de redes sociales, con una gran cantidad de filtros y jerarquías para su validación, para la generación de información en sus bases de datos cuando la situación y el problema lo requieren.

Desconozco totalmente cual será su metodología, pero me parece muy interesante, puesto que dan soporte a categorías en las que es muy difícil acceder a la información y con una velocidad bastante alta.

# Tarea
