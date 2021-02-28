
import sqlite3


class DB():

    def __init__(self):

        self.con = sqlite3.connect('Asterminator.db')
        self.cur = self.con.cursor()
        
        
        try: 
            print('base_de_datos_creada')
            self.cur.execute('''CREATE TABLE puntuaciones(id INTEGER PRIMARY KEY AUTOINCREMENT,puntos integer,nombre VARCRCHAR (100)) ''')
            self.cur.execute('''CREATE TABLE nombres(id INTEGER PRIMARY AUTOINCREMENT,nombre VARCRCHAR(50))''')
            self.con.commit()
        except:
            print('error') 

    def insert_score(self,consulta):
        #self.cur.execute(consulta)
        #self.mi_conexion.commit()
        self.cur.execute('''INSERT INTO puntuaciones(puntos, nombre)VALUES(?,?)''',consulta)
        self.con.commit()

    def insert_name(self,consulta):
        self.cur.execute('''INSERT INTO nombres(nombre)VALUES(?)''',consulta)
        self.con.commit()
        