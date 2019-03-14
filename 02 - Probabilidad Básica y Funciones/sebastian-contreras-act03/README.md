![](logo.png)

# Actividad 03 - Subsetting y probabilidad básica

* Para poder realizar esta actividad debes haber revisado la lectura correspondiente a la semana.
* Crea una carpeta de trabajo y guarda todos los archivos correspondientes (notebook y csv).
* Una vez terminada la actividad, comprime la carpeta y sube el `.zip` a la sección correspondiente.


## Ejercicio 1: Lectura de archivos

* Importe `pandas` y `numpy` siguiendo las convenciones.
* Lea la base de datos `worldcup2014.csv` y asígnela a un objeto `df`.
* Solicite las primeras 5 observaciones con `head`

## Ejercicio 2: Estime las frecuencias de `continent`
* Utilice `value_counts`. Responda lo siguiente:
    - ¿Cuál es el continente con una mayor presencia en la muestra?
    - ¿Cuál es la probabilidad de elegir un equipo asiático al azar?
    - ¿Cuál es la probabilidad de elegir un equipo africano al azar?

## Ejercicio 3: Probabilidades por continente

* Por cada continente, genere un nuevo objeto que almacene sólo las observaciones del continente.
    - _tip_: Para ello puede utilizar la siguiente sintáxis: `df[df['variable'] == condicion]`.

## Ejercicio 4: Calcule la probabilidad de clasificación a la siguiente ronda

* Pase todos los objetos creados en un loop que imprima la probabilidad de pasar a la siguiente ronda por continente.
    - _tip_: Genere un array que contenga los objetos a pasar en el loop.
* ¿Cuál fue la probabilidad de que un país asiático pase a la siguiente ronda?
* ¿Cuáles fueron los dos continentes que tuvieron la mayor probabilidad de clasificar?
* ¿Cuál fue la probabilidad de no clasificar un país europeo?

## Ejercicio 5: Refactorización

* A continuación se presenta un loop que cuenta las probabilidades de juegos ganados. Se pide que `value_counts` cuente los juegos no ganados y ganados, ignorando de la cantidad de juegos.

```python
for i in [africa_df, europe_df, asia_df, northamerica_df, southamerica_df]:
    print(i['juegos_ganados'].value_counts('%'))
```


* Para contar los juegos ganados puede utilizar `np.where`, que devuelve un array con valores imputados cuando se satisface una condición. En este caso debemos clasificar como 0 cuando los juegos ganados sean igual a 0, y 1 cuando sean igual o mayor a 1.
* El array que devuelve `np.where` es difícil de trabajar, por lo que pueden transformarlo con `pd.Series` para utilizar `value_counts`.
* En base a la refactorización del código, responda lo siguiente:
    - ¿Qué continente tuvo una mayor probabilidad de ganar juegos?
    - ¿Qué continente presentó un nivel similar entre juegos ganados y perdidos?
* Utilize el código para el caso de juegos perdidos y analize el continente con una mayor probabilidad de perder.

### En base a la información generada, responda lo siguiente
* ¿Qué continente tiene una mayor probabilidad de clasificar?
* ¿Qué continente tiene una menor probabilidad de clasificar?
* ¿Cuál es la probabilidad de no clasificar de un país africano?

