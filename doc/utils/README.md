# Prueba backend


Realiza una clase en Python con un método estático que reciba dos argumentos date\_string y date\_format

date\_string es una cadena que contiene un datetime pj: "2018-12-01 07:03"
puede contener variables como @year o $dia en vez de números entre los separadores

date\_format es el formato de esta fecha pj: "%Y-%m-%d %I:%M:%s"

El método devolverá dos arrays, el primero con los elementos de la fecha por separado
["2018", "12", "01", "07", "03"]
y el segundo los separadores eliminados
["-", "-", " ", ":"]

> Ejecuta los tests en el directorio que contenga "utils" con el comando
>
    python3 -m unittest
