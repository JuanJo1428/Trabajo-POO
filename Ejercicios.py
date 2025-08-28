# Ejercicio Número 4

class Calculos:

    @staticmethod
    def CalcularAlberto(EdadJuan):
        EdadAlberto = (2/3)*EdadJuan
        
        return EdadAlberto

    @staticmethod
    def CalcularAna(EdadJuan):
        EdadAna = (4/3)*EdadJuan
        
        return EdadAna

    def CalcularMadre(EdadJuan, EdadAlberto, EdadAna):
        EdadMadre = EdadJuan + EdadAlberto + EdadAna
    
        return EdadMadre

def Edades():
    EdadJuan = float(input("¿Cuál es la edad de Juan?: "))
    EdadAlberto = Calculos.CalcularAlberto(EdadJuan)
    EdadAna = Calculos.CalcularAna(EdadJuan)
    EdadMadre = Calculos.CalcularMadre(EdadJuan, EdadAlberto, EdadAna)
    print(f"La Madre tiene {EdadMadre} años y sus hijos tienen:")
    print(f"Juan: {EdadJuan} años, Alberto: {EdadAlberto} años y Ana: {EdadAna} años.")

Edades()


#Ejercicio Número 5

Suma = 0
x = 20
Suma = Suma + x # Suma es igual a 20
y = 40
x = x + (y ** 2) # x va a ser igual 1620
Suma = Suma + (x/y) # Suma va a ser igual a "20 + (1620/40)" = 60.5
print(f"El valor de la suma es: {Suma}") 


# Ejercicio Número 12

class SR:
    
    @staticmethod
    def CalcularBruto(HorasTrabajadas):
        SalarioB = HorasTrabajadas * 5000
        return SalarioB
    
    @staticmethod
    def CalcularRetencion(SalarioBruto):
        Retencion = SalarioBruto * 0.125
        return Retencion
    
    @staticmethod
    def CalcularNeto(SalarioBruto, Retencion):
        SalarioN = SalarioBruto - Retencion
        return SalarioN
    

def Valores(HorasTrabajadas = 48 * 4):
    
    SalarioBruto = SR.CalcularBruto(HorasTrabajadas)
    RetencionFuente = SR.CalcularRetencion(SalarioBruto)
    SalarioNeto = SR.CalcularNeto(SalarioBruto, RetencionFuente)

    print(f"El Salario Bruto del trabajador es de ${SalarioBruto}.")
    print(f"Pero  al tener una Retención en la fuente de ${RetencionFuente}, en realidad su Salario Neto es de ${SalarioNeto}.")
    
Valores()


# Ejercicio Número 14

class CC:
    
    def CalcularCuadrado(Numero):
        Cuadrado = Numero ** 2
        return Cuadrado
    
    def CalcularCubo(Numero):
        Cubo = Numero ** 3
        return Cubo
    

def Leer_Calcular():
    
    Numero = float(input("Ingrese el Número del cual desea conocer su Cuadrado y su Cubo: "))
    Cuadrado = CC.CalcularCuadrado(Numero)
    Cubo = CC.CalcularCubo(Numero)
    
    print(f"El Cuadrado y el Cubo del número {Numero} son respectivamente: {Cuadrado}, {Cubo}.")

Leer_Calcular()


# Ejercicio Número 17

import math 

class AL:
    
    def CalcularArea(Radio):
        Area = math.pi * (Radio ** 2)
        return Area
    
    def CalcularLongitud(Radio):
        Longitud = 2 * math.pi * Radio 
        return Longitud
    

def Radio_Calcular():
    
    Radio = float(input("Ingrese el Radio del círuclo que desea calcular: "))
    AreaCirculo = AL.CalcularArea(Radio)
    Longitud = AL.CalcularLongitud(Radio)
    
    print(f"El Area del Círculo de radio {Radio} es de {AreaCirculo} y su longitud es de {Longitud}.")

Radio_Calcular()
