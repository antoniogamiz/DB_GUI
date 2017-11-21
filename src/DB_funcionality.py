# !/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb



class DB_Handler():
    def openDB(self, **arg):
        if(len(arg)!=4):
            return -1
        try:
            self.connect = MySQLdb.connect(host=arg['host'], user=arg['user'], passwd=arg['passwd'], db=arg['db'])
            self.cursor = self.connect.cursor()
            self.host=arg['host']
            self.user=arg['user']
            self.passwd=arg['passwd']
            self.db=arg['db']
            return 1
        except:
            return -1

    def getRegisters(self):
        query="select * from FIELD where 1;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def addRegister(self, *arg):
        if len(arg) != 6:
            return -1
        query="insert into FIELD (id, field1, field2, field3, field4, field5) values (1,'WORKING','WORKING','WORKING','WORKING','WORKING')"
        self.cursor.execute(query)
        self.connect.commit()

# DB = DB_Handler()
# print(DB.openDB(host='localhost', user='antonio', passwd='antonio', db='ejercicioDB'))


connect = MySQLdb.connect(host='localhost', user='antonio', passwd='antonio', db='GUI')




# def id_valido(cursor):
#     query="select id from Victimas where 1;"
#     cursor.execute(query)
#     return cursor.rowcount+1


# #Establecemos la conexión con la base de datos 'ejercicioDB'
# connect = MySQLdb.connect(host='localhost', user='antonio', passwd='antonio', db='ejercicioDB')

# #Creamos el cursor.
# cursor = connect.cursor()

# #Añadimos a la base de datos los primeros 10 registros.
# query="insert into Victimas (id,Nombre,Profesion,Muerte) values (1, \"Fenix\",\"Asador de pollos\",\"Ice Bucket Challenge\");"
# cursor.execute(query)


# #Hacemos un commit por si acaso.
# connect.commit()
