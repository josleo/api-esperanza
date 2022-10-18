from typing import Union
import json
from fastapi import FastAPI
import mysql.connector
app = FastAPI()

database_username = 'admin'
database_password = '123456789'
database_ip       = 'database-1.cmmt68xsoykx.us-east-1.rds.amazonaws.com'
database_name     = 'Tabla_prueba'

@app.get("/")
def read_root():
    list = ["pregunta 1 -- Año con más carreras-- https://henrry-n1.herokuapp.com/uno",
            "pregunta 2 -- Año con más carreras-- https://henrry-n1.herokuapp.com/dos"
            "pregunta 2 -- Año con más carreras-- https://henrry-n1.herokuapp.com/tres"]
    return (list)
    

#se crea un funcuion para mostrar los datos de la primera pregunta " Año con más carreras "
@app.get("/uno")
def  uno():
    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion"  )  
    cur = miConexion.cursor()
    cur.execute("select * from pregunta1" )
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)


#Piloto con mayor cantidad de primeros puestos
@app.get("/dos")
def  dos():
    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion" )     
    cur = miConexion.cursor()
    cur.execute("SELECT MAX(gan.driver) as ' carreras ganadas', gan.driverId as piloto, d.name as Nombre FROM (SELECT driverId, COUNT(driverId) as driver FROM results WHERE positionOrder='1' GROUP BY driverId) gan JOIN drivers d  ON (gan.driverId=d.driverId);" )
    datos2 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos2)


#Nombre del circuito más corrido
@app.get("/tres")
def  tres():

    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion"  )  
    cur = miConexion.cursor()
    cur.execute("select * from pregunta3")
    datos3 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos3)


#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
@app.get("/cuatro")
def  cuatro():
    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion"  )  
    cur = miConexion.cursor()
    cur.execute("select  * from pregunta4" )
    datos4 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos4)

@app.get("/europa")
def  uno():
    db = mysql.connector.connect(host='database-1.cmmt68xsoykx.us-east-1.rds.amazonaws.com',
                                        user='admin',
                                        passwd='123456789',
                                        db='sys',
                                        port=3306)

   
# This line is that you need
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM europa ")
    result = cursor.fetchall()
    datos= (f"europa: {json.dumps(result)}")
    db.close()
    return (datos)

@app.get("/paises")
def  uno():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_paises")
    pais = []
    datos  = cur.fetchall()
    for  fila  in datos :
        paises = {'id_paises':fila[0],'country':fila[1],'id_continente':fila[2]}
        pais.append(paises) 
    miConexion.close()

    return {"paises": pais}

@app.get("/continentes")
def  uno():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_continente")
    conti = []
    datos_cont  = cur.fetchall()
    for  fila  in datos_cont :
        continnente = {'id_continente':fila[0],'continente':fila[1]}
        conti.append(continnente) 
    miConexion.close()

    return {"continentes": conti}

@app.get("/year")
def  uno():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_year")
    años = []
    datos_años  = cur.fetchall()
    for  fila  in datos_años :
        años_ = {'year':fila[0]}
        años.append(años_) 
    miConexion.close()

    return {"year": años}


@app.get("/esperanza")
def  year():

    miConexion = mysql.connector.connect( host=database_ip, user= database_username, passwd=database_password, db=database_name )
    cur = miConexion.cursor()
    cur.execute("select * from tb_esperanza")
    esperanza = []
    datos_esperanza  = cur.fetchall()
    for  fila  in datos_esperanza :
        esperanza_ = {
        'index':fila[0],
        'country':fila[1],
        'year':fila[2],
        'Desempleo_mujeres':fila[3],
        'Desempleo_mujeres_jóvenes_14_24_años':fila[4],
        'Desempleo_varones_jovenes_15_24_años':fila[5],
        'Desempleo_Población_activa_total':fila[6],
        'esperanza_vida_nacer_Mujeres':fila[7],
        'esperanza_vida_nacer_Varones':fila[8],
        'esperanza_vida_nacer_total':fila[9],
        'poblacion_total_salud':fila[10],
        'fertilidad_mujeres':fila[11],
        'tasa_mortalidad_bebes':fila[12],
        'crecimiento_masa_monetaria_inflacion':fila[13],
        'tasa_mort_5anios_cada_mil':fila[14],
        'crecimiento_poblacion':fila[15],
        'esperanza_vida_mujeres_anios':fila[16],
        'esperanza_vida_hombres_anios':fila[17],
        'Tasa_fertilidad_mujeres':fila[18],
        'PBI_per_capita':fila[19],
        'desempleo_total':fila[20],
        'mortalidad_accidentes_transito':fila[21],
        'acceso_a_la_electricidad':fila[22],
        'producción_de_energía_eléctrica_renovable':fila[23],
        'id_continente':fila[24]}
        esperanza.append(esperanza_) 
    miConexion.close()

    return {"esperanza": esperanza}