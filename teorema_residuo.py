import complex_number as z
import math


def sobreRegion(r,z):
    if math.sqrt(math.pow((z.real),2) + math.pow((z.imaginary),2)) == r:
        return 1
    else:
        return 0

def z_b(r,n,m,z0,z1,z2):
    if math.sqrt(math.pow((z1.real),2) + math.pow((z1.imaginary),2)) > r:
        return z.Complex_Number(0,0)
    else:
        aux=z.Complex_Number(0,0)
        aux.resta(z1,z0)
        auxm=z.Complex_Number(0,0)
        auxm.potencia(aux,m)
        
        aux2=z.Complex_Number(0,0)
        aux2.resta(z1,z2)
        aux2m=z.Complex_Number(0,0)
        aux2m.potencia(aux2,4)
        
        zdivisor=z.Complex_Number(0,0)
        zdivisor.multiplicar(auxm,aux2m)

        zdividendo=z.Complex_Number(0,0)
        zdividendo.potencia(z1,n)

        resultado=z.Complex_Number(0,0)
        resultado.division(zdividendo,zdivisor)

        return resultado

    pass