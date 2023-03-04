import mysql.connector
import pymongo

class SistemaBD_MySql:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.conn = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )
        print(self.conn.get_server_info,self.conn.is_connected())
        self.cursor = self.conn.cursor()
    
    def createTable(self):
        sql= ('''CREATE TABLE IF NOT EXISTS PACIENTES 
                (ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                Nombre VARCHAR(50),
                Cedula INTEGER,
                Genero VARCHAR(20),
                Servicio VARCHAR(50))''')
        self.cursor.execute(sql)
        self.conn.commit()
    
    def create(self, table, data):    
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def read(self, table, condition=None):
        sql = f"SELECT * FROM {table}"
        if condition:
            sql += f" WHERE {condition}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
    
    def update(self, table, data, condition=None):
        if not condition:
            raise ValueError("No condition specified for update operation")
        set_values = ', '.join([f"{k} = %s" for k in data.keys()])
        sql = f"UPDATE {table} SET {set_values} WHERE {condition}"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()
        return self.cursor.rowcount
    
    def delete(self, table, condition=None):
        if not condition:
            raise ValueError("No condition specified for delete operation")
        sql = f"DELETE FROM {table} WHERE {condition}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount
    
    def close(self):
        self.cursor.close()
        self.conn.close()
            
class SistemaBD_Mongo:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.client = pymongo.MongoClient(host=self.host, port=self.port, username=self.username, password=self.password)
        self.db = self.client[self.database]
    
    def create(self, collection, data):
        result = self.db[collection].insert_one(data)
        return result.inserted_id
    
    def read(self, collection, query=None):
        cursor = self.db[collection].find(query)
        return [doc for doc in cursor]
    
    def update(self, collection, query, data):
        result = self.db[collection].update_one(query, {'$set': data})
        return result.modified_count
    
    def delete(self, collection, query):
        result = self.db[collection].delete_one(query)
        return result.deleted_count
    
    def close(self):
        self.client.close()


class Persona():
    # def __init__(self,a:str, *, p:str = "pro" ):
    def __init__(self ):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
#Propiedades
    # Setters
    def asignarNombre(self,nombre):
        self.__nombre = nombre
    def asignarCedula(self,cedula):
        self.__cedula = cedula
    def asignarGenero(self,genero):
        self.__genero = genero

    # getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    #deleters
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero
        
# Métodos adicionales segun la abstracción hecha 
    def caminar(self):        
        print(input("ingrese direccion: "))
    def comer(self):
        print(input("Ingrese la comida que desea: "))
        
class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self, servicio):
        return self.__servicio            
    
