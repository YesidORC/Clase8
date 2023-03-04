from clases import *

def main():
    # mi_sistema = SistemaBD_MySql("127.0.0.1","root","","BaseSid")
    mi_sistema = SistemaBD_Mongo("localhost",27017,"","","POO2023")
    while True:
        menu = int(input("""1.Nuevo Paciente
                            2. Número de Pacientes
                            3. Datos Paciente
                            4. Salir
        > """))
        if menu == 1:
            nombre = input("Ingrese el Nombre: ")
            cedula =int(input("Ingrese la Cédula: "))
            genero =input("Ingrese el Género: ")
            servicio = input("Ingrese el Servicio: ")
            pac = {"Nombre":nombre,"Cedula":cedula,"Genero":genero,"Servicio":servicio}
            #Crear objeto Paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)
            # mi_sistema.createTable()
            mi_sistema.create("PACIENTES",pac)
        elif menu == 2:
            print("Número total de pacientes: " + str(mi_sistema.verNumeroPacientes()))
        elif menu == 3:
            mi_sistema.verDatosPacientes()
        elif menu == 4:
            break
        else: 
            print("Opción inválida")

if __name__ == '__main__':
    main()