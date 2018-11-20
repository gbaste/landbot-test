# Prueba backend

En mi solución primero de todo he declarado una variable donde he guardado solo los delimitadores que me recibo desde el test.

```
delim = list(separators[2::3])
```

He inicializado un loop donde por cada carácter dentro de la variable de delimitadores compruebo en las fechas que me llegan desde el test, separarlas dependiendo de los delimitadores que encuentre.

```
for char in delim:
    end = date.find(char)
```

En el primer IF detecto si no ha encontrado el carácter, eso significa que a llegado al fin del loop.

```
if end < 0:
    end = len(date)
```

En el segundo IF compruebo que a encontrado el carácter y guardo den el array dates la fecha y elimino de date los caracteres extraidos.

```
if date[start:end] != '':
        dates.append(date[start:end])
    date = date[end + 1:]
dates.append(date)
```

En el ultimo IF controlo el problema de que no lleguen los segundos en el parámetro date, y elimino el ultimo espacio que debería estar ocupado por los segundos.

```
if dates[-1] == '':
    del dates[-1]
```

Finalmente devuelvo los resultados guardándolos en la variable result.

```
result = (dates, delim)
    return(result)
```

Para ejecutar los tests en el directorio que contenga "utils" he usado el siguiente comando

```
python3 -m unittest discover -t ..
```
