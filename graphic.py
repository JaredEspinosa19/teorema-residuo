import matplotlib.pyplot as plt
import math
import complex_number as z

#se debe graficar 3 puntos 

def graphic_function(r,z0,z1,z2,circle): #graficar unico numero 

    radio=max(r,abs(z0.imaginary),abs(z1.real),abs(z2.imaginary))
    
    izda = min(-1, -abs(radio*2)-(abs(radio*2)*.3))
    dcha = max(1,abs(radio*2)+(abs(radio*2)*.3))
    abajo = min(-1, -abs(radio*2)-(abs(radio*2)*.3))
    arriba = max(1, abs(radio*2)+(abs(radio*2)*.3))
    
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((0, 0),r,fill=False)

    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    plt.plot(z0.real,z0.imaginary,marker="o",color="red")
    plt.plot(z1.real,z1.imaginary,marker="o",color="yellow")
    plt.plot(z2.real,z2.imaginary,marker="o",color="blue")
    # Pintamos lineas que pasan por el origen de coordenadas
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlim([izda,dcha])
    plt.ylim([abajo,arriba])
    plt.xlabel('Re(Z)')
    plt.ylabel('Im(Z)')
    title=(z.string_z("Z0=",z0)+"\n"+z.string_z("Z1=",z1)+"\n"+z.string_z("Z2=",z2)+"\n"+circle)
    plt.title(title)
    plt.show()