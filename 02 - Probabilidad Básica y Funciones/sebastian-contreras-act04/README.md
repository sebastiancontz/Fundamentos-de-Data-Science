![](logo.png)

# Actividad 04 - Funciones y probabilidad básica

* Para poder realizar esta actividad debes haber revisado la lectura correspondiente a la semana.
* Crea una carpeta de trabajo y guarda todos los archivos correspondientes (notebook y csv).
* Una vez terminada la actividad, comprime la carpeta y sube el `.zip` a la sección correspondiente.

* Importe las librerías `pandas` y `numpy` siguiendo las convenciones.
* Importe la base de datos `worldcup2014.csv` utilizada en la sesión anterior y guárdela en un objeto `df` para su posterior uso.

## Ejercicio 1: Generación de funciones

* Genere dos funciones para calcular la media y varianza de un vector. Debe cumplir con los siguientes requistos:
    - Ambas funciones deben ingresar el vector a analizar como un argumento `x`.
    - Las funciones deben contener `docstrings` con la documentación asociada a la variable.
    - Deben __retornar__ el resultado (_tip_: utilice `return`).
    - La función de la varianza debe llamar a la función de la media.
* Utilice las funciones para reportar la información sobre `goles_favor`, `goles_contra`, `puntos` en la base de datos.

## Ejercicio 2: A continuación se presenta el siguiente código para obtener la media y varianza de una variable para distintos continentes


```python
continent = []
store_mean = []
store_std = []

for d in [africa_df, europe_df, asia_df, northamerica_df, southamerica_df]:
    continent.append(d.iloc[0,1])
    store_mean.append(media(d['goles_favor']))
    store_std.append(varianza(d['goles_favor']))
    
tmp = pd.DataFrame({'continente': continent,
                   'media_goles': store_mean,
                   'std_goles': store_std})

tmp
```

* En base al código presentado, refactorízelo en una función con los argumentos `dataframe`, `group_by` y `var` para ingresar una base de datos, una variable para segmentar y una variable a analizar, respectivamente.
* Se debe ingresar la base de datos completa, para que la segmentación se realize __dentro__ de la función.
* La función debe retornar un `DataFrame`.
* Implemente la función para extraer la información sobre la cantidad de goles a favor, en contra y la cantidad de puntos.
* Reporte en qué continente se encuentra la mayor cantidad de goles a favor, en contra y cantidad de puntos.

## Ejercicio 3: Simulaciones

* Genere una función `generate_pet` que devuelva de forma aleatoria un string `'perro'` o `'gato'`. Ejecútela un par de veces.
    - _tip:_ Puede utilizar la función `np.random.choice` para retornar elementos al azar.

* Aplique la función `generate_pet` 20 veces mediante un loop y guarde los resultados en una lista.
    - _tip:_ Puede generar una lista vacía con `[ ]` y asignarla a un objeto. Puede añadir elementos a la lista con `.append`.
    - _tip:_ Puede generar loops `for _ in <rango>`, donde la declaración de `_` permite ejecutar las expresiones n veces.
* ¿Cuál es la probabilidad de elegir un perro al azar? ¿Y un gato?

* Agrege `np.random.seed(2)` al inicio del chunk. ¿Qué hace éste método en la simulación?

## Ejercicio 4: Función simuladora

* Genere un método llamado `simulate_pets_prob` que tome como argumento un número finito de simulaciones a generar.
* El método debe simular dos situaciones, `young_pet` y `old_pet`, y contar la ocurrencia de los siguientes escenarios:
    1. De los dos animales simulados, contar las ocasiones donde por lo menos uno de los animales sea un perro.
    - De los dos animales simulados, contar las ocasiones donde por lo menos uno sea un perro viejo.
    - De los dos animales simulados, contar las ocasiones donde los dos sean perros
* El método debe tener una semilla pseudoaleatoria de 1.
* De los tres escenarios, ¿Cuál es el menos probable? ¿Cuál es el más probable?
