import numpy as np
import matplotlib.pyplot as plt

FUERZA_EXCITATRIZ_MAXIMA = 1765
PERIODO = 0.6532945
PUNTOS_POR_CICLO = 500
X_ADMISIBLE = 0.61
MASA = 10
K = 925
CANT_CICLOS = 5

def puntoMedio(funcion, c):
  #Inicializamos dos datos que se utilizaran
  h = PERIODO/PUNTOS_POR_CICLO
  x1 = 0
  x2 = 0
  x1_max = 0
  x2_max = 0
  t = 0
  ciclo = 1
  contador_puntos_por_ciclo = 0
  arreglo_x1 = []
  arreglo_x2 = []
  arreglo_t = []
  #Iteramos utilizando 500 puntos por ciclo, en este caso son 5 ciclos
  for i in range(CANT_CICLOS*PUNTOS_POR_CICLO):
    arreglo_x1.append(x1)
    arreglo_x2.append(x2)
    arreglo_t.append(t)
    q_1_x1 = x2
    q_1_x2 = funcion(x1, x2, t, ciclo, c)
    q_2_x1 = (x2 + q_1_x2*h/2)
    q_2_x2 = funcion(x1 + q_1_x1*h/2, x2 + q_1_x2*h/2, t + h/2, ciclo,
    c)
    x1 += (q_1_x1 + q_2_x1)*h/2
    x2 += (q_1_x2 + q_2_x2)*h/2
    t = i*h
    
  #Actualizamos para buscar la amplitud maxima
  if (x1 > x1_max):
    x1_max = x1
  if (x2 > x2_max):
    x2_max = x2
  #Actualizamos por que ciclo van para usarlo en la funcion y modificar el tiempo en funcion del periodo
  contador_puntos_por_ciclo += 1
  if (contador_puntos_por_ciclo == PUNTOS_POR_CICLO):
    ciclo += 1
    contador_puntos_por_ciclo = 0
  return arreglo_x1, arreglo_x2, arreglo_t, x1_max, x2_max

def funcion(x1, x2, t, ciclo, c):
  #Verificamos si el tiempo esta dentro de Periodo/10
  if (t >= PERIODO):
    tiempo = t - (PERIODO* (ciclo-1))
  else:
    tiempo = t
  if (tiempo <= PERIODO/10):
    a = FUERZA_EXCITATRIZ_MAXIMA/MASA
  else:
    a = 0
  b = K*x1/MASA
  c = c*x2/MASA
  return a-b-c

def g(c):
  arreglo_x1, arreglo_x2, arreglo_t, x1_max, x2_max= puntoMedio(funcion, c)
  return x1_max - X_ADMISIBLE


def metodoSecante():
  c1 = 100
  c2 = 120
  c3 = 0
  
  valores_g = []
  valores_g.append(g(c1))
  valores_g.append(g(c2))
  
  valores_c = []
  valores_c.append(c1)
  valores_c.append(c2)
  
  valores_f = []
  valores_f.append(g(c1) + X_ADMISIBLE)
  valores_f.append(g(c2) + X_ADMISIBLE)
  
  for i in range(5):
    c3 = c2 - (g(c2)*(c2-c1))/(g(c2)-g(c1))
    valores_g.append(g(c3))
    valores_c.append(c3)
    valores_f.append(g(c3) + X_ADMISIBLE)
    c1 = c2
    c2 = c3
  return valores_c, valores_f, valores_g

##PARA ENCONTRAR LOS VALORES OBTENIDOS DE LA TABLA DE C, F(C) Y G(C) CORRER:
c, f, f_g = metodoSecante()
print(c)
print(f)
print(f_g)
##PARA ENCONTRAR LOS GRAFICOS OBTENIDOS EN LA PRIMERA PARTE:
# x1, x2, t, x1_max, x2_max = puntoMedio(funcion, 100)
# plt.figure(dpi = 125)
# plt.plot(t, x1)
# plt.ylabel("x1(t)")
# plt.xlabel("t")
# plt.show()
# x1, x2, t, x1_max, x2_max = puntoMedio(funcion, 100)
# plt.figure(dpi = 125)
# plt.plot(t, x2)
# plt.ylabel("x2(t)")
# plt.xlabel("t")
# plt.show()
