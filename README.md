# OBJETIVO

El objetivo del trabajo práctico es determinar el coeficiente de amortiguamiento para evitar las
vibraciones excesivas en una estructura que está siendo sometida a una carga cíclica.

## Problema de valores iniciales:

1) Se debe resolver la ecuación diferencial dada por la segunda ley de Newton obteniendo la
posición, la velocidad y la aceleración.
2) Se debe seleccionar un paso de cálculo de por lo menos 500 puntos por ciclo.
3) La resolución del problema de valores iniciales se resolverá con el método Runge-Kutta de orden 2. 

## Obtención del coeficiente de amortiguación deseado

4) Se define una función “f(x)” en la que “x” es el valor de “C” y “f(x)” la amplitud deseada. El valor
de la función se obtiene con una corrida del algoritmo  de Runge Kutta de orden 2, y le método de la secante. 
5) El valor del coeficiente “C” se debe obtener con 3 cifras significativas correctas
