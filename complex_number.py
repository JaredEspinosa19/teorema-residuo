import math

class Complex_Number:

    def __init__(self,r_p,i_p):
        self.real=r_p
        self.imaginary=i_p
        self.title=None

    def suma(self,z1,z2):
        self.real=z1.real + z2.real
        self.imaginary=z1.imaginary + z2.imaginary
        self.title=string_z("",self)


    def resta(self,z1,z2):
        self.real=z1.real-z2.real
        self.imaginary=z1.imaginary-z2.imaginary
        self.title=string_z("",self)
    
    def multiplicar(self,z1,z2):
        self.real=((z1.real*z2.real)-(z1.imaginary*z2.imaginary))
        self.imaginary=((z1.real*z2.imaginary)+(z1.imaginary*z2.real))
        self.title=string_z("",self)


    def division(self,z1,z2):
        if z2.real==0 and z2.imaginary==0:
            self.title="No existe solución"
        else:
            self.real=((z1.real*z2.real)+(z1.imaginary*z2.imaginary))/((z2.real**2)+(z2.imaginary**2))
            self.imaginary=((z1.imaginary*z2.real)-(z1.real*z2.imaginary))/((z2.real**2)+(z2.imaginary**2))
            self.title=string_z("",self)
        
    def potencia(self,z1,n):
        self.real=z1.real
        self.imaginary=z1.imaginary
        z_aux=Complex_Number(1,0)


        if n==0:
            self.real=1
            self.imaginary=0
        elif n<0:
            for n_2 in range(0,abs(n)):
                self.division(z_aux,z1)
                z_aux.real=self.real
                z_aux.imaginary=self.imaginary
        else:
            for n1 in range(1,n):
                real=self.real
                imaginary=self.imaginary
                self.real=((real*z1.real)-(imaginary*z1.imaginary))
                self.imaginary=((real*z1.imaginary)+(imaginary*z1.real))
        
        self.title=string_z("".format(n),self)


    def exponencial(self,z):
        self.real=(math.e**z.real)*(math.cos(z.imaginary))
        self.imaginary=(math.e**z.real)*(math.sin(z.imaginary))
        self.title=string_z("",self)


    def seno(self,z):
        z_aux=Complex_Number(0,0)
        z_aux2=Complex_Number(0,0)
        z_aux.real=(((math.e**(-(z.imaginary)))*(math.cos(z.real))) - ((math.e**(z.imaginary))*(math.cos(-z.real))))
        z_aux.imaginary=(((math.e**(-(z.imaginary)))*(math.sin(z.real))) - ((math.e**(z.imaginary))*(math.sin(-z.real))))
        z_aux2.imaginary=2
        self.division(z_aux,z_aux2)
        self.title=string_z("",self)

     
    def coseno(self,z):
        self.real=( ((math.e**(-(z.imaginary)))*(math.cos(z.real))) + ((math.e**(z.imaginary))*(math.cos(-z.real))) )/2
        self.imaginary=( ((math.e**(-(z.imaginary)))*(math.sin(z.real))) + ((math.e**(z.imaginary))*(math.sin(-z.real))) )/2
        self.title=string_z("", self)


    def tan(self,z):
        seno=Complex_Number(0,0)
        coseno=Complex_Number(0,0)
        seno.seno(z)
        coseno.coseno(z)
        self.division(seno,coseno)
        self.title=string_z("",self)
    
    def cosenoh(self,z):
        self.real=(((math.e**((z.real)))*(math.cos(z.imaginary))) + ((math.e**(-z.real))*(math.cos(-z.imaginary))))/2
        self.imaginary=( ((math.e**((z.real)))*(math.sin(z.imaginary))) + ((math.e**(-z.real))*(math.sin(-z.imaginary))) )/2
        self.title=string_z("",self)

    def senoh(self,z):
        self.real=(((math.e**((z.real)))*(math.cos(z.imaginary))) - ((math.e**(-z.real))*(math.cos(-z.imaginary))))/2
        self.imaginary=( ((math.e**((z.real)))*(math.sin(z.imaginary))) - ((math.e**(-z.real))*(math.sin(-z.imaginary))) )/2
        self.title=string_z("",self)

    #crear las funciones de coseno hiperobolico y seno hiperbolico

#functions

def raices(list,z2,m):

    if m==0:
        z=Complex_Number(0,0)
        list.append(z)
    elif m>0 or m<0:
        r=math.sqrt((z2.real**2)+(z2.imaginary**2))
        
        if z2.real<0 and z2.imaginary>0:
            angle=((180*math.pi)/180)-math.atan(z2.imaginary/z2.real)
        elif z2.real<0 and z2.imaginary<0:
            angle=math.atan(z2.imaginary/z2.real)-((180*math.pi)/180)
        elif z2.real>0 and z2.imaginary==0:
            angle=0
        elif z2.real==0 and z2.imaginary>0:
            angle=90
        elif z2.real<0 and z2.imaginary==0:
            angle=180
        elif z2.real==0 and z2.imaginary<0:
            angle=270
        else:
            angle=math.atan(z2.imaginary/z2.real)
        
        r_2=pow(r,(1/m))

        for n in range(0,m):
            z=Complex_Number(0,0)
            z.real=r_2*(math.cos((angle+(2*math.pi*n))/m))
            z.imaginary=r_2*(math.sin((angle+(2*math.pi*n))/m))
            list.insert(n,z)
    
def string_z(string,z):

    if z.real>=0 and z.imaginary>=0:
        return(string +" {} + {}i ".format(z.real,z.imaginary))
    elif z.real<0 and z.imaginary>=0:
        return(string +" {} + {}i ".format(z.real,z.imaginary))
    elif z.real>=0 and z.imaginary<0:
        return(string +" {} - {}i ".format(z.real,abs(z.imaginary)))
    else:
        return(string +" {} - {}i ".format(z.real,abs(z.imaginary)))

def entrada_usuario(cadena):    
    cadena.replace(" ",'')

    fin = len(cadena)
    real=0
    im=0

    auxP=cadena[1:fin].find('+')
    auxN=cadena[1:fin].find('-')

    if auxP>-1:
        
        if len(cadena[0:auxP+1])>0:
            real=float(cadena[0:auxP+1])
        else:
            real=0
    
        if cadena[auxP+2]=='i':
            im=1
        else:
            im=float(cadena[auxP+1:fin-1])

    elif auxN>-1:

        if len(cadena[0:auxN+1])>0:
            real=float(cadena[0:auxN+1])
        else:
            real=0

        if cadena[auxN+2]=='i':
            im=-1
        else:
            im=float(cadena[auxN+1:fin-1])

    else:
        if cadena[fin-1]=='i':
            real=0
            
            if cadena[0]=='i':
                im=1
            else:
                im=float(cadena[0:fin-1])
        else:
            im=0
            real=float(cadena[0:fin])
    
    return Complex_Number(real, im)