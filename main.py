from clases import *
def main():
 sis=Sistema()
 while True:
    opcion=(int(input("ingrese la opción que desea realizar: \n 1. ingresar nuevo paciente \n 2.Ver Paciente \n 3.Salir")))
    if opcion == 1:
        print("A continuacion se pediran los datos")
        c=int(input("Ingrese la cedula del paciente: ")) 
        condicion=sis.Verificar(c)
        if condicion== True:
           print("El paciente ya se encuentra registrado")
        else:
            n=input("Ingrese el nombre del paciente: ")
            g=input("ingrese el genero del paciente: ")
            s=input("Ingrese el servicio del paciente: ")
            pac=Paciente()
            pac.AsignarNombre(n)
            pac.AsignarCedula(c)
            pac.AsignarGenero(g)
            pac.AsignarServicio(s)
            sis.IngresarPaciente(pac)


    elif opcion==2:
        c=int(input("Ingrese la cedula del paciente a buscar: "))
        p=sis.VerDatosPaciente(c)
        print("Nombre: "+ p.verNombre())
        print("Cedula: "+ p.verCedula())
        print("Genero: "+ p.verGenero())
        print("Servicio: "+ p.verServicio())
    elif opcion==3:
        break
    else:
        print("Ingrese una opcion de las indicadas")

if __name__== "__main__":
   main()