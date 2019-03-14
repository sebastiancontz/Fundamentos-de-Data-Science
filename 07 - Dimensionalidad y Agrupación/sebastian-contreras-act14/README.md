![](logo.png)

# Actividad 14 - Dimensionalidad y Agrupación

* Para poder realizar esta actividad debes haber revisado la lectura correspondiente a la semana.
* Crea una carpeta de trabajo y guarda todos los archivos correspondientes (notebook y csv).
* Una vez terminada la actividad, comprime la carpeta y sube el `.zip` a la sección correspondiente

# Unidad: Dimensionalidad y Agrupación - Sesión 2


## Ejercicio 1: Preparación del ambiente de trabajo

* Para este ejercicio trabajaremos de manera __conjunta__ identificando la paleta de colores de carátulas de álbumes.
    * Las imágenes se encuentran en una carpeta con el nombre `album_covers`
    * Cada imagen tiene la siguiente nomenclatura: `artista-nombre-del-album.jpg`.
* El objetivo es generar un método que nos permita identificar la dominancia de una cantidad finita de colores.
* Para importar imágenes y visualizarlas, vamos a importar las siguientes librerías:
    * Partamos por incluír las librerías clásicas: `pandas`, `numpy` y `matplotlib.pyplot`.
    * `sklearn.cluster.KMeans`: para extraer los principales componentes de una matriz numérica.
    * `skimage.io`: Para poder ingresar y leer imágenes.

## Ejercicio 2: Importación de imagenes

* Partamos por ingresar una imágen a nuestro ambiente de trabajo. Para ello ocuparemos `io.imread`. ¿Qué devuelve?
* Para visualizar la imágen en el notebook, ocupe `io.imshow`.

## Ejercicio 3: Preprocesamiento de imágenes y KMeans

* Con la representación numérica de la imágen, vamos a extraer la altura, el ancho y la cantidad de canales mediante `shape`.
* Posteriormente redimensionaremos la imágen con `reshape`.
* Partamos por inicializar nuestro algoritmo `KMeans` con un `k=8`, ¿Qué significará esto?
* Vuelva a implementar el mismo algoritmo con `MiniBatchKMeans`. ¿Qué diferencia existe con `KMeans`?

## Ejercicio 4: Extracción de valores

* Ahora extraeremos las etiquetas predichas con `labels_`. Hasta el momento las etiquetas hacen referencia a cada centroide. Para imputar sentido en éstos, debemos extraer los valores de los centroides.
* Para extraer los centroides (valores característicos), utilicemos el atributo `cluster_centers_`.
* Con las etiquetas, generaremos un conteo de ocurrencia con `np.unique`. Para extraer el conteo, debemos implementar la opción `return_counts=True`.

## Ejercicio 5: Conversión rgb a hex

* Con los centroides, vamos a convertirlos a formato hexadecimal. Vamos a generar una función y la pasaremos con `map` por cada centroide.

## Ejercicio 6: Definición de base

* Ahora generaremos un `DataFrame` con las siguientes variables:
    - El color `hex`.
    - La ocurrencia del color en cada pixel `count`.
    - El porcentaje de ocurrencia de cada color respecto a `cluster_centers_`.
* Posteriormente ordenaremos los colores de forma descendente por el porcentaje de ocurrencia.

## Ejercicio 7: Visualización

* Genere un gráfico de barras donde presente el porcentaje de cada color. Las barras deben estar coloreadas con el color inferido.


## Bonus point: envuelva todo en una función
