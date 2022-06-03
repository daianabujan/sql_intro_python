import json
import requests
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

def fetch():
    print('Contenido de la tabla')
    
    conn = sqlite3.connect('sql_intro_python\heart.db')
    c = conn.cursor()    
    
    data = c.execute("SELECT pulso FROM sensor").fetchall()
    print(data)

    return data
    
def show(data):
    #Generación del gráfico

    fig = plt.figure()
    fig.suptitle('Evolución del rítmo cardíaco', fontsize = 16)
    ax = fig.add_subplot()

    ax.plot(data, c='navy', label='ID')
    ax.legend('Pulso', fontsize= 10)
    ax.set_facecolor('whitesmoke')
    ax.grid('solid')
    plt.show()

def estadistica(data):
    #Análisis de datos
    data = np.asanyarray(data)
    print('El valor MEDIO es =', round(data.mean()))
    print('El valor MAXIMO es =', data.max())
    print('El valor MINIMO es =', data.min())
    print('El DESVIO ESTANDAR es =', round(data.std()))

def regiones(data):
    data = np.asanyarray(data)
    mean = round(data.mean())
    std = round(data.std())

    x1 = []
    y1 = []

    x2 = []
    y2 = []

    x3 = []
    y3 = []

    for i in range(len(data)):
        if data[i] <= (mean-std):
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (mean+std):
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])
    
    #Creación de gráfico
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x2, y2, color='c', label='Entusiasmado')
    ax.plot(x3, y3, color='g', label='Tranquilo')
    ax.plot(x1, y1, color='b', label='Aburrido')
 
    ax.set_facecolor('whitesmoke')
    ax.set_title("Evolución del rítmo cardíaco")
    ax.legend()
    plt.show()

if __name__ == "__main__":

  data = fetch()
  
  #Data analytics
  show(data)
  estadistica(data)
  regiones(data)