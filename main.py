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
    list = ["[bienvenidos al  api de esperanza de vida , aqui encontrara todos los datos relcionados al tema --->/esperanza,/year,/paises,/continentes]",
            "continentes -- https://esperanzadevida.herokuapp.com/esperanzas"
            "años -- https://esperanzadevida.herokuapp.com/year"
            "paises  -- https://esperanzadevida.herokuapp.com/paises"
            "continentes -- https://esperanzadevida.herokuapp.com/continentes"]
    return (list)
    

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