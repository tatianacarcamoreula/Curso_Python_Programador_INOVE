# IMPORTANTE: NO borrar los comentarios
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Arreglar el código a continuación para que funcione
    # en el editor de código:

    # X representa nuḿeros del 1 al 5
    # Y es cada número de X multiplicado por 10 --> y = x * 10
    x = [1, 2, 3, 4 , 5]
    y = []
    for i in x:
        y.append(i * 10)

    # Realizaremos un gráfico "plot" con:
    # years como "x"
    # poblacion como "y"
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y, c= "barnred" )
    plt.show()

    print("terminamos")