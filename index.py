import complex_number as z
import graphic as gp
import teorema_residuo as tr

#Calculadora del teorema del residuo

def main():

    print("Calculadora del teorema del residuo de numero complejos")
    #Solicitar datos
    r=float(input("Introduzca el radio de la circunferencia con centro (0,0)= "))
    n=int(input("Introduzca la potencia a la cual estará elevado Z^n= "))
    a=int(input("Introduzca el valor de a para (Z-ai)^m= "))
    m=int(input("Introduzca el valor de m= "))
    b=int(input("Introduzca el valor de b para (Z-b)= "))
    c=int(input("Introduzca el valor de c para (Z+ci)^4= "))

    #crear los elementos    
    circle="λ=(x-{})^2 + (y-{})^2 = {}".format(0,0,r)
    z0=z.Complex_Number(0,(a))
    z1=z.Complex_Number((b),0)
    z2=z.Complex_Number(0,(c)*(-1))

    #imprimir teorema
    print("          Z^{}           ".format(n))
    print("-------------------------")
    print("(Z-({})i)^{}(Z-({}))(Z+({})i)^4".format(a,m,b,c))
    
    #evaluar si algun numero esta sobre el contorno

    if tr.sobreRegion(r,z0)==1 | tr.sobreRegion(r,z1)==1 | tr.sobreRegion(r,z2)==1:
        print("La suma de los residuos se indetermina ya que uno de los puntos esta sobre el contorno de la región")
        gp.graphic_function(r,z0,z1,z2,circle)
    

    #realizar evaluacion

    print(z.string_z("",tr.z_b(r,n,m,z0,z1,z2)))
    gp.graphic_function(r,z0,z1,z2,circle)
    


if __name__ == "__main__":
    main()