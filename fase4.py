import logging
from datetime import datetime

fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f" Fecha y hora: {fecha_actual}")
# 1. Archivo de logs
logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s",
)

class Carro:
    
    _valor_hora=2000
    
    def __init__(self,color,marca,placa,hora_ingreso,hora_salida):
        self._color=color
        self._marca=marca
        self._placa=placa
        self._hora_ingreso=hora_ingreso
        self._hora_salida=hora_salida
        
        
    def horas_a_pagar (self):
        valor_a_pagar=self._hora_salida-self._hora_ingreso
        return valor_a_pagar*self._valor_hora
        
    def mostrar_informacion(self):
        return (
            f"carro: {self._color}  marca {self._marca}  placa: {self._placa}" 
            f"  Ingreso a las: {self._hora_ingreso}"
            f"  Salio a las: {self._hora_salida}"
            
        )
lista_carros=[]

try:
    cantidad=int(input("Cuantos carros desea registrar: "))



    for i in range(cantidad):
        print(f"Datos del carro {i+1}:  ")
        color=input("ingrese el color:  ")
        marca=input("ingrese la marca:  ")
        placa=(input("ingrese la placa:  "))
        hora_ingreso=int(input("Digita la hora de ingreso en  numeros: "))
        hora_salida=int(input("Digita la hora de salida en numeros: "))
        
        
        nuevo_carro=Carro(color,marca,placa,hora_ingreso,hora_salida) 
        lista_carros.append(nuevo_carro)
except ValueError:
print("Error: Escribe solo números por favor\n")

      
    
        
else:
    print("\n" + "-" * 50)
    print(f"📊 Total de carros registrados: {len(lista_carros)}")
    print("        RESUMEN DEL DÍA")
    print("-" * 50)
    total_dia = 0

    for carro in lista_carros:
        valor = carro.horas_a_pagar()
        total_dia += valor
        print(f"{carro.mostrar_informacion()} → Paga: $ {valor:,} pesos")
    print("-" * 50)
    print(f"💰 TOTAL DEL DÍA: $ {total_dia:,} pesos")

    
    
finally:
    print("-" * 40)
    print("¡Gracias por usar nuestro sistema!")
    print("Proceso finalizado")
