class Paciente:
    def __init__(self):
        self.__nombre= ""
        self.__cedula= 0
        self.__servicio= " "
        self.__genero= ""

    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerServicio(self):
        return self.__servicio
    def VerGenero(self):
        return self.__genero

    def AsignarNombre(self,n):
        self.__nombre= n
    def AsignarCedula(self,c):
        self.__cedula= c
    def AsignarServicio(self,s):
        self.__servicio= s
    def AsignarGenero(self,g):
        self.__genero= g

class Sistema:
    def __init__(self):
        self.__lista_pacientes= []
        self.__numero_pacientes=len(self.__lista_pacientes)
    
    def Verificar(self,c):
        for p in self.__lista_pacientes:
            if p.VerCedula()==c:
                return True
            else:
                return c

    def IngresarPaciente(self,pac):
        self.__lista_pacientes.append(p)
        self.__numero_pacientes=len(self.__lista_pacientes)

    def VerNumeroPacientes(self):
        print("En el sistema hay: "+ str(len(self.__lista_pacientes))+ " pacientes")

    def VerDatosPaciente(self,c):
        for p in self.__lista_pacientes:
            if c==p.verCedula:
                return p