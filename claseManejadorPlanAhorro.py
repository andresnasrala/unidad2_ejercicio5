import csv
from clasePlanAhorro import planAhorro



class manejadorPlanAhorro:
    __lista_plan_ahorro = []

    def __str__(self):
        s = ""
        for i in range (len(self.__lista_plan_ahorro)):
            s += str(self.__lista_plan_ahorro[i].getCodigo()) + ',' + str(self.__lista_plan_ahorro[i].getModelo()) + ',' + str(self.__lista_plan_ahorro[i].getVersion()) + ',' + str(self.__lista_plan_ahorro[i].getValor()) + ',' + str(self.__lista_plan_ahorro[i].getCuotas()) + ',' + str(self.__lista_plan_ahorro[i].getLicitar()) + '\n'
        return s



    def calcularValorCuota(self, i):
        return int ((self.__lista_plan_ahorro[i].getValor() / self.__lista_plan_ahorro[i].getCuotas()) + self.__lista_plan_ahorro[i].getValor() * 0.10)



    def carga (self):
        path = './planes.csv'
        archivo = open (path, 'r')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            codigo = fila [0]
            modelo = fila[1]
            version = fila[2]
            valor = fila[3]
            pa = planAhorro(codigo, modelo, version, valor)
            self.__lista_plan_ahorro.append(pa)
        if len (self.__lista_plan_ahorro) > 0:
            print ('Carga Lista!')
            print ()
        else: print ('Error en la carga')



    def actualizarValor (self):
        for i in range (len(self.__lista_plan_ahorro)):

            print ('---------->Actualización de precios<----------')
            print(f'''
-> Código de plan: {self.__lista_plan_ahorro[i].getCodigo()}
-> Modelo vehículo: {self.__lista_plan_ahorro[i].getModelo()}
-> Version vehículo: {self.__lista_plan_ahorro[i].getVersion()}
''')
            valor = int (input ('-> Ingrese nuevo valor para el vehículo: '))
            self.__lista_plan_ahorro[i].setValor(valor)



    def verPlanesPorValor(self, val):

        for i in range (len(self.__lista_plan_ahorro)):   
            cuota = self.calcularValorCuota(i)

            if cuota < val:
                print (f'''
-> Código de plan: {self.__lista_plan_ahorro[i].getCodigo()}
-> Modelo vehículo: {self.__lista_plan_ahorro[i].getModelo()}
-> Version vehículo: {self.__lista_plan_ahorro[i].getVersion()}
-----------------------------------------------------------''')


    def mostarCantidadLicitar (self, val):

        for i in range (len (self.__lista_plan_ahorro)):

            if val == self.__lista_plan_ahorro[i].getCodigo():
                c = self.calcularValorCuota(i)
                print (f'El monto total a pagar para licitar "{self.__lista_plan_ahorro[i].getModelo()}, {self.__lista_plan_ahorro[i].getVersion()}" es: $ {c * self.__lista_plan_ahorro[i].getLicitar()}')


    def cambiarCuotas(self, cod): 

        for i in range (len (self.__lista_plan_ahorro)):

            if cod == self.__lista_plan_ahorro[i].getCodigo():
                
                aux = int (input ('Ingrese nuevo cantidad de cuotas para licitar: '))
                self.__lista_plan_ahorro[i].cambiarCuotasLicitar(aux)
                print (f'Se cambió la cantidad de cuotas con exito')