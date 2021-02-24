import pymysql

class DB():

    def __init__(self):
        self.mi_conexion = pymysql.connect(host = 'localhost', user = 'root',passwd = '', db = 'Asterminator')
        self.cur = self.mi_conexion.cursor()

    def insert_score(self,consulta):
        self.cur.execute(consulta)
        self.mi_conexion.commit()
        