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


HorasTrabajadas = 48 * 4
SalarioBruto = SR.CalcularBruto(HorasTrabajadas)
RetencionFuente = SR.CalcularRetencion(SalarioBruto)
SalarioNeto = SR.CalcularNeto(SalarioBruto, RetencionFuente)

print(f"El Salario Bruto del trabajador es de ${SalarioBruto}.")
print(f"Pero  al tener una Retención en la fuente de ${RetencionFuente}, en realidad su Salario Neto es de ${SalarioNeto}.")
    



