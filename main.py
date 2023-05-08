from menu import Menu
from claseManejadorPlanAhorro import manejadorPlanAhorro
import os

if __name__ == '__main__':
    
    manager_PA = manejadorPlanAhorro()
    bandera = False
    os.system('cls')
    while not bandera:
        print("""
---------->Menu Principal<----------
-> 1: Cargar datos (1)
-> 2: Actualizar valor de vehiculo de cada plan(2a)
-> 3: Mostrar código del plan, modelo y versión del vehículo por valor de cuota (2b)
-> 4: Mostrar el monto que se debe pagar para licitar el vehículo (2c)
-> 5: Modificar la cantidad cuotas que debe tener pagas para licitar (2d)
-> 0: Salir del programa
""")
        opcion = int (input("Su opcion: "))
        menu = Menu()
        menu.opcion(opcion, manager_PA)
        
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')