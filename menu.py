import os

class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            0: self.salir
                        }
        


    def opcion(self,op, manager_PA):   
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op ==1 or op==2 or op==3 or op==4 or op==5:
            func(manager_PA)
        else:
            func()

    def opc1 (self, manager_PA):
        manager_PA.carga()
        print (str(manager_PA))

    def opc2(self, manager_PA):
        manager_PA.actualizarValor()
        os.system('cls')
        print ('---------->Nuevos Valores<----------\n')
        print (manager_PA)
    
    def opc3(self, manager_PA):
        os.system('cls')
        print ('---------->Ver planes menores a un valor de cuota<----------\n')
        aux = int (input ('ingrese valor de cuota: '))
        manager_PA.verPlanesPorValor(aux)

    def opc4(self, manager_PA):
        os.system('cls')
        print ('---------->Ver monto total para licitar vehiculo<----------\n')
        aux = int (input ('Ingrese código de plan: '))
        manager_PA.mostarCantidadLicitar(aux)
    
    def opc5(self, manager_PA):
        os.system('cls')
        print ('---------->Modificar la cantidad cuotas que debe tener pagas para licitar<----------\n')
        aux = int (input ('Ingrese codigo de plan: '))
        manager_PA.cambiarCuotas(aux)

    def salir(self):
        print('Saliendo...')