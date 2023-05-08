class planAhorro:
    __codPLan: int
    __modelo: str
    __version: str
    __valor: float
    __cuotas = int (60) 
    __licitar = int (10) 


    def __init__ (self, codigo=0, modeloelo='', version='', valor=0):
        self.__codPLan = codigo
        self.__modelo = modeloelo
        self.__version = version
        self.__valor = valor




    def cambiarCuotasLicitar(cls, c):
        cls.__licitar = c


    def getCodigo (self):
        return int(self.__codPLan)
    
    def getmodeloelo (self):
        return self.__modelo

    def getversionsion (self):
        return self.__version
    
    def getValor (self):
        return int (self.__valor)
    
    def getCuotas (self):
        return int (self.__cuotas)
    
    def getLicitar (self):
        return int(self.__licitar)
    
    def setValor (self, valor):
        self.__valor = valor
        print ('Valor actualizado')