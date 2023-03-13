from math import e
import matplotlib.pyplot as plt
import numpy as np
import tkinter

#Interfaz
ventana = tkinter.Tk()
ventana.geometry("200x200")

x = [[-10],[-10]]
y = [[0],[10]]
z = [[10],[-10]]
last_point = [[5],[0]]

def draw_plane():
    plt.cla()
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)
    #Linea horizontal
    ax.axhline(y=0, color='black', lw=2)

    #Linea vertical
    ax.axvline(x=0, color='black', lw=2)

    plt.scatter(x[0],x[1] , color="black")
    plt.scatter(y[0],y[1], color="black")
    plt.scatter(z[0],z[1], color="black")
    plt.scatter(last_point[0],last_point[1], color="black")
    
    for i in range(1000):
        n = np.random.randint(1,4)
        if n == 1:
            last_point[0][0] = (last_point[0][0] + x[0][0])/2
            last_point[1][0] = (last_point[1][0] + x[1][0])/2
            plt.scatter(last_point[0],last_point[1], color="purple", s=10)

        elif n==2:
            last_point[0][0] = (last_point[0][0] + y[0][0])/2
            last_point[1][0] = (last_point[1][0] + y[1][0])/2
            plt.scatter(last_point[0],last_point[1], color="red", s=10)

        else:
            last_point[0][0] = (last_point[0][0] + z[0][0])/2
            last_point[1][0] = (last_point[1][0] + z[1][0])/2
            plt.scatter(last_point[0],last_point[1], color="green", s=10)

    plt.draw()

    plt.show()

entrada1  =tkinter.Button(ventana, text = "Filtrar",command = draw_plane, fg= "dark blue", background="#C4F9D1")
entrada1.pack()
entrada1.place(x=60, y=90, height= 40, width=80)
etiqueta = tkinter.Label(ventana, text="Adaline", fg="dark green", height=3).pack()

fig, ax = plt.subplots()
ax.set_xlim(-11, 11)
ax.set_ylim(-11, 11)

#Linea horizontal
ax.axhline(y=0, color='black', lw=2)

#Linea vertical
ax.axvline(x=0, color='black', lw=2)


plt.scatter(x[0],x[1] , color="black")
plt.scatter(y[0],y[1], color="black")
plt.scatter(z[0],z[1], color="black")
plt.scatter(last_point[0],last_point[1], color="black")

plt.show()
    
ventana.mainloop()