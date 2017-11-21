# !/usr/bin/python3.6
# -*- coding: utf-8 -*-

import MySQLdb

def readString(mensaje=""):
    string=""
    while not string:
        try:
            string=input(mensaje)
        except:
            print("No puede introducir cadenas vacías")
    return string

def imprimirDB(cursor):
    query="select * from Victimas where 1"
    cursor.execute(query)

    registers = cursor.fetchall()

    for register in registers:
        print(register)

def id_valido(cursor):
    query="select id from Victimas where 1;"
    cursor.execute(query)
    return cursor.rowcount+1

def readOption():
    print("¿Quiere introducir un nuevo registro?( S (Sí) N (No)): ")
    option=readString().upper()
    while option !="S" and option != "N":
        option=readString("Introduce una opción válida: ").upper()
    return option

def readNewRegister(cursor,option):

    print("Introduce los campos del registro: ")    

    if option=="S":    
        id_newRegister=id_valido(cursor)
        campo1=readString("Campo 1(Nombre): ")
        campo2=readString("Campo 2(Profesión): ")
        campo3=readString("Campo 3(Muerte): ")
    
    return [id_newRegister, campo1, campo2, campo3]

#Establecemos la conexión con la base de datos 'ejercicioDB'
connect = MySQLdb.connect(host='localhost', user='antonio', passwd='antonio', db='ejercicioDB')

#Creamos el cursor.
cursor = connect.cursor()

#Añadimos a la base de datos los primeros 10 registros.
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (1, \"Fenix\",\"Asador de pollos\",\"Ice Bucket Challenge\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (3, \"Dragon Dorado\",\"Avion\",\"Huelgas de controladores\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (4, \"Grifo\",\"Fontanero\",\"Goteo\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (5, \"Coatl\",\"Serpiente\",\"Espada\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (6, \"Licantropo\",\"Comer humanos\",\"Escopeta\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (7, \"Pegaso\",\"Volar\",\"Ballesta\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (8, \"Cerbero\",\"Comer humanos\",\"Hacha grande\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (9, \"Arcangel\",\"Castigar a infieles\",\"Satán\");"
cursor.execute(query)
query="insert into Victimas (id,Nombre,Profesion,Muerte) values (10, \"Poseidon\",\"Castigar marineros\",\"Espada sagrada\");"
cursor.execute(query)

#Hacemos un commit por si acaso.
connect.commit()


imprimirDB(cursor)

opt=readOption()

while(opt!= "N"):
    registro=readNewRegister(cursor,opt)
    query="insert into Victimas (id,Nombre,Profesion,Muerte) values (\""+str(registro[0])+"\",\""+registro[1]+"\",\""+registro[2]+"\",\""+registro[3]+"\");"
    cursor.execute(query)
    connect.commit()
    opt=readOption()


print("La base de datos actualmente contiene: ")
imprimirDB(cursor)


query="delete from Victimas where 1;"
cursor.execute(query)

connect.commit()

cursor.close()
connect.close()