![](logo.png)
# Actividad 02 - Control de flujos

* Para poder realizar esta actividad debes haber revisado la lectura correspondiente a la semana.
* Crea una carpeta de trabajo y guarda todos los archivos correspondientes (notebook y csv).
* Una vez terminada la actividad, comprime la carpeta y sube el `.zip` a la sección correspondiente.

## Ejercicio 1: Generar un par de arrays ficticios con `numpy`

* Utilice la función `np.linspace` para generar un array entre 1 y 50, y un array entre 50 y 150.

## Ejercicio 2: Ejecute un loop que devuelva si el número en el primer array es par o impar

* Para averiguar si el cada número es par o impar puede implementar el operador de módulo (`%`) para encontrar si el número es divisible por 2.

## Ejercicio 3: Genere un loop con el segundo array que cuente las siguientes condiciones

* Si el número es divisible por 2 o 3
* Si el número es divisible por 2 y 3
* Si el número es divisible por 3 pero no por 2
* si el número no es divisible por 2 ni 3



## Ejercicio 4
* Utilizando la misma base `flights.csv`

### Hacer un loop y clasificar los meses con una cantidad de pasajeros menor a la media

* Para ello, generen un nuevo objeto que represente la media de `passengers`.
* Generen una columna en la base de datos que se llame `underperforming` y asígnele 0.
* Ejecuten un loop que recorra cada observación de `passengers`, donde si la observación es menor a la media de `passengers` se le asigne a `underperforming` un 1.
* Para asignar unos en la columna `underperforming` ya creada, utilice la función `at`. Lea la documentación asociada para ver qué parámetros ingresa.

## Ejercicio 5: Hacer un loop que clasifique los meses donde la cantidad de pasajeros se escapa de la tendencia.

* Para ello, genere dos objetos que guarden la media general y la desviación estandar general de `passengers`.
* Genere una nueva columna en la tabla de datos que se llame `outlier` y asígnele 0.
* Ejecuten un loop que recorra cada observación de `passengers`, donde si la observación se escapa de la tendencia sea 1, de lo contrario 0.
* Para clasificar los casos que se escapen la tendencia, la observación debe satisfacer una de las siguientes condiciones:
    - La observación debe ser menor a la  media menos la desviación estándar, o
    - La observación debe ser mayor a la media más la desviación estándar.

#### ¿Cuántas observaciones se pueden clasificar como casos extremos?

