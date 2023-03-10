import os
import datetime

class Indices:
 #constructor
    def __init__(self):
        #Atributos de la clase
        self.__pot_d = 0
        self.__pot_t = 0
        self.__pot_a1 = 0
        self.__pot_a2 = 0
        self.__pot_b = 0
        self.__pot_g = 0

 # Propiedadades--> Metodos Get y set
    def verPot_D(self):
        return self.__pot_d
    def asignarPot_D(self,p):
        self.__pot_d = p

    def verPot_T(self):
        return self.__pot_t
    def asignarPot_T(self,p):
        self.__pot_t = p

    def verPot_A1(self):
        return self.__pot_a1
    def asignarPot_A1(self,p):
        self.__pot_a1 = p

    def verPot_A2(self):
        return self.__pot_a2
    def asignarPot_A2(self,p):
        self.__pot_a2 = p

    def verPot_B(self):
        return self.__pot_b
    def asignarPot_B(self,p):
        self.__pot_b = p

    def verPot_G(self):
        return self.__pot_g
    def asignarPot_G(self,p):
        self.__pot_g = p

class Visita:
    def __init__(self):
        #Atributos de la clase
        self.__fecha = datetime.datetime.now()
        self.__registro = ''
        self.__notas = ''
        #La visita tiene una clase indice que se inicializa vacia
        self.__indice = Indices() # SOlo se guarda un objeto tipo Indices

 #Propiedadades--> Metodos Get y set
    def verFecha(self):
        return self.__fecha
    def asignarFecha(self,f):
        self.__fecha = f

    def verRegistro(self):
        return self.__registro
    def asignarRegistro(self,r):
        self.__registro = r

    def verNotas(self):
        return self.__notas
    def asignarNotas(self,n):
        self.__notas = n

    def verIndice(self):
        return self.__indice
    def asignarIndice(self,i):
        self.__indice = i

class Paciente:
    def __init__(self):
        #Atributos de la clase
        self.__nombre = ''
        self.__cedula = 0
        self.__genero = ''
        #Un paciente tiene muchas visitas, en este ejemplo los trabajamos
        #como diccionarios
        self.__visitas = {} # Clave-->fecha, valor-->Visita

    def verNombre(self):
        return self.__nombre
    def AsignarNombre(self,n):
        self.__nombre = n

    def verCedula(self):
        return self.__cedula
    def asignarCedula(self,c):
        self.__cedula = c

    def verGenero(self):
        return self.__genero
    def asignarGenero(self,g):
        self.__genero = g

    def verVisita(self,f):
        return self.__visitas.get(f)
    def verListadoVisitas(self):
        return self.__visitas
    def ingresarVisitas(self,v):
        self.__visitas[v.verFecha()]=v

    def verificarExiste(self,f):
        return f in self.__visitas
    def eliminarVisita(self,f):
        del self.__visitas[f]    

class Sistema:
    def __init__(self):
        self.__pacientes = {} #la llave seria la cedula y el valor el paciente due??o de dicha cedula

    def verificarExiste(self,c):
        return c in self.__pacientes

    def ingresarPac(self,p):
        self.__pacientes[p.verCedula()]=p

    def eliminarPac(self,c):
        del self.__pacientes[c]
        return True

    def verPac(self,c):
        return self.__pacientes[c]

    def cargarGuardar(self):
        pass

def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Ingrese un dato num??rico...")
    return valor
def validarf(msj):
    while True:
        try:
            valor = float(input(msj))
            break
        except ValueError:
            print("Ingrese un dato num??rico...")
    return valor


def main():
    sis = Sistema()
    while True:
        print("Ingrese:\n 1 Nuevo paciente\n 2 Editar paciente\n 3 Eliminar un paciente\n 4- Cargar y guardar paciente\n 5- Ver cantidad de visitas de pacientes\n 6-Salir del sistema")
        valor = validar("Valor: ")
        if valor == 1: 
            cedula = validar("Ingrese la cedula: ")
            if sis.verificarExiste(cedula) == True:
                print(f"Paciente ya esta en el sistema...verifique la cedula ingresada {cedula}")
                continue
            else:
                p = Paciente()
                p.AsignarNombre(input("Nombre: "))
                p.asignarCedula(cedula)
                p.asignarGenero(input("G??nero: "))
                numVis =  validar (f"Ingrese la cantidad de visitas que va ingresar del paciente {p.verNombre()}: ")
                for i in range(0,numVis):
                    dia = validar("Ingrese dia:")
                    mes = validar("Ingrese mes:")
                    a??o = validar("Ingrese a??o:")
                    f = datetime.datetime(a??o, mes, dia)
                    if p.verificarExiste(f):
                        print("Ya existe  visita, ingrese otra porfavor")
                    v = Visita()
                    v.asignarFecha(f)
                    v.asignarRegistro(os.getcwd()+f'\Pacientes_{p.verCedula()}')
                    v.asignarNotas(input("Ingrese Observaciones: "))
                    ind = v.verIndice()
                    ind.asignarPot_A1(validarf("Ingrese a1= "))
                    ind.asignarPot_A2(validarf("Ingrese a2= "))
                    ind.asignarPot_B(validarf("Ingrese b= "))
                    ind.asignarPot_D(validarf("Ingrese d= "))
                    ind.asignarPot_G(validarf("Ingrese g= "))
                    ind.asignarPot_T(validarf("Ingrese t= "))                    
                    # v.asignarIndice(ind) # Reasigno el objeto indice a la visita
                    p.ingresarVisitas(v) # Ingreso el objeto visita al paciente

                sis.ingresarPac(p) # Ingreso el objeto paciente al sistema

        elif valor == 2: #Edici??n de Paciente
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula):
                pac = sis.verPac(cedula)
                opcion = validar("Ingresar parar editar:\n1- Nombre\n2- C??dula\n3- G??nero\n4- Visita\n5- Salir\n Opci??n:  ")
                if opcion == 1:
                    pac.AsignarNombre(input("Ingrese nuevo nombre: "))
                elif opcion == 2:
                    pac.asignarCedula(validar("Ingrese nueva c??dula: "))
                    sis.eliminarPac(cedula)
                    sis.ingresarPac(pac)
                elif opcion == 3:
                    pac.asignarGenero(input("Ingrese nuevo g??nero: "))   
                elif opcion == 4:
                    dia = validar("Ingrese dia:")
                    mes = validar("Ingrese mes:")
                    a??o = validar("Ingrese a??o:")
                    f = datetime.datetime(a??o, mes, dia)
                    if pac.verificarExiste(f) == True:
                        visi = pac.verVisita(f)
                        menu = validar("Ingrese para editar: \n1- Fecha \n2- Registro \n3- Nota \n4- Indice\n 5- Eliminar vista\n Opcion : ")
                        if menu == 1:
                            dia = validar("Ingrese nuevo dia: ")
                            mes = validar("Ingrese nuevo mes: ")
                            a??o = validar("Ingrese nuevo a??o: ")
                            f = datetime.datetime(a??o, mes, dia)
                            visi.asignarFecha(f)
                            pac.ingresarVisitas(visi)
                            pac.eliminarVisita(f)
                        elif menu == 2:
                            visi.asignarRegistro("Ingrese nueva Registro: ") 
                        elif menu == 3:
                            notaExistente = visi.verNotas()
                            visi.asignarNotas(input("Ingrese nueva Nota complementaria: ")+notaExistente) 
                        elif menu == 4: 
                            I = visi.verIndice()
                            I.asignarPot_A1(validarf("a1= "))
                            I.asignarPot_A2(validarf("a1= "))
                            I.asignarPot_B(validarf("b= "))
                            I.asignarPot_G(validarf("g= "))
                            I.asignarPot_D(validarf("d= "))
                            I.asignarPot_T(validarf("t= "))
                        elif menu == 5:
                            pac.eliminarVisita(visi.verFecha())
                            
            else:
                print(f"Paciente con cedula {cedula}")

        elif valor == 3: # Elimiar Paciente
            cedula = validar("Ingrese la cedula: ")
            if sis.verificarExiste(cedula) == False:
                print("Paciente no existe ...")
            elif sis.eliminarPac(cedula):
                print("Paciente eliminado exitosamente")

        elif valor ==  4: # Cargar y guardar inforamacion a archivo txt
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula) == True:
                p = sis.verPac(cedula)
                archivo = open(f"Paciente {p.verNombre()}.txt",'w')
                archivo.write(p.verNombre()+ "\n" )
                archivo.write(str(p.verCedula())+ "\n" )
                archivo.write(p.verGenero()+ "\n" )
                for i in p.verListadoVisitas():
                    archivo.write(p.verVisita(i).verFecha()+ "\n" )
                    archivo.write(p.verVisita(i).verRegistro()+ "\n" )
                    archivo.write(p.verVisita(i).verNotas()+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_A1())+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_A2())+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_B()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_D()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_G()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_T()) + "\n") 

        elif valor == 5:
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula) == True:
                p = sis.verPac(cedula)
                cv = len(p.verListadoVisitas())
                print(f"El paciente {p.verNombre()} tiene {cv} visitas")

        elif valor == 6:
            break

        else:
            print("Opci??n no v??lida, intentelo nuevamente....")

if __name__ == '__main__':
    main()
