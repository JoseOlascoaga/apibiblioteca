############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# initializations
app = Flask(__name__)
CORS(app)




# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'biblioteca'
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"




### ---------------------------------TABLA EDITORIALES----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DEL EDITORIAL DE LA TABLA 'editoriales' ####
@cross_origin()
@app.route('/add_contact2', methods=['POST'])
def add_contact2():
    if request.method == 'POST':
        codeditorial = request.json['codeditorial']  ## codigo editorial
        nombre = request.json['nombre']  ## nombre
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO editoriales (codeditorial, nombre) VALUES (%s,%s)", (codeditorial, nombre))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})

#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'editoriales' ####
@cross_origin()
@app.route('/getAll2', methods=['GET'])
def getAll2():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM editoriales')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdEditorial': result[0],'codeditorial': result[1], 'nombre': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'editoriales' ####
@cross_origin()
@app.route('/getAllById2/<IdEditorial>',methods=['GET'])
def getAllById2(IdEditorial):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM editoriales WHERE IdEditorial = %s', (IdEditorial))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdEditorial': result[0], 'nombre': result[1]}
       payload.append(content)
       content = {}
    return jsonify(payload)

### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'editoriales' ###
@cross_origin()
@app.route('/update2/<IdEditorial>', methods=['PUT'])
def update_contact2(IdEditorial):
    codeditorial = request.json['codeditorial']  ## codigo editorial
    nombre = request.json['nombre']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE editoriales
        SET codeditorial = %s,
            nombre = %s
        WHERE IdEditorial = %s
    """, (codeditorial, nombre, IdEditorial))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})

### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'editoriales' ###
@cross_origin()
@app.route('/delete2/<IdEditorial>', methods = ['DELETE'])
def delete_contact2(IdEditorial):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM editoriales WHERE IdEditorial = %s', (IdEditorial,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### ------------------------------------TABLA AUTORES-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO AUTOR DE LA TABLA 'autores' ####
@cross_origin()
@app.route('/add_contact3', methods=['POST'])
def add_contact3():
    if request.method == 'POST':
        codautor = request.json['codautor']  ## codautor
        nombre = request.json['nombre']  ## nombre
        apellido = request.json['apellido']  ## apellido
        nacionalidad = request.json['nacionalidad']  ## nacionalidad
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO autores (codautor, nombre, apellido, nacionalidad) VALUES (%s,%s,%s,%s)", (codautor, nombre, apellido, nacionalidad))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'autores' ####
@cross_origin()
@app.route('/getAll3', methods=['GET'])
def getAll3():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM autores')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdAutores': result[0],'codautor': result[1], 'nombre': result[2], 'apellido': result[3], 'nacionalidad': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'autores' ####
@cross_origin()
@app.route('/getAllById3/<IdAutores>',methods=['GET'])
def getAllById3(IdAutores):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM autores WHERE IdAutores = %s', (IdAutores))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdAutores': result[0], 'nombre': result[1], 'apellido': result[2], 'nacionalidad': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'autores' ###
@cross_origin()
@app.route('/update3/<IdAutores>', methods=['PUT'])
def update_contact3(IdAutores):
    codautor = request.json['codautor']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    nacionalidad = request.json['nacionalidad']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE autores
        SET codautor = %s,
            nombre = %s,
            apellido = %s,
            nacionalidad = %s
        WHERE IdAutores = %s
    """, (codautor, nombre, apellido, nacionalidad, IdAutores))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'autores' ###

@cross_origin()
@app.route('/delete3/<IdAutores>', methods = ['DELETE'])
def delete_contact3(IdAutores):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM autores WHERE IdAutores = %s', (IdAutores,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -------------------------------------TABLA LIBRO------------------------------------###


#### RUTA PARA CREAR UN REGISTRO LIBRO DE LA TABLA 'libro' ####
@cross_origin()
@app.route('/add_contact4', methods=['POST'])
def add_contact4():
    if request.method == 'POST':
        codlibro = request.json['codlibro']  ## codigo libro
        nombrelibro = request.json['nombrelibro']  ## nombre
        Idautor = request.json['Idautor'] ## Idautor
        Ideditorial = request.json['Ideditorial']    ## Ideditorial  
        FechaLanzamiento = request.json['FechaLanzamiento'] ## FechaLanzamiento
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO libro (codlibro,nombrelibro,Idautor,Ideditorial,FechaLanzamiento) VALUES (%s,%s,%s,%s,%s)", (codlibro,nombrelibro,Idautor,Ideditorial,FechaLanzamiento))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'libro' ####
@cross_origin()
@app.route('/getAll4', methods=['GET'])
def getAll4():
    cur = mysql.connection.cursor()
    cur.execute('SELECT libro.*,autores.IdAutores,editoriales.Ideditorial FROM libro INNER JOIN autores ON autores.IdAutores = libro.Idautor INNER JOIN editoriales ON editoriales.IdEditorial = libro.Ideditorial')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'Idlibro': result[0],'codlibro': result[1], 'nombrelibro': result[2], 'Idautor': result[6], 'Ideditorial': result[7], 'FechaLanzamiento': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)



#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'libro' ####
@cross_origin()
@app.route('/getAllById4/<Idlibro>',methods=['GET'])
def getAllById4(Idlibro ):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libro WHERE Idlibro  = %s', (Idlibro ))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'Idlibro ': result[0], 'nombre': result[1], 'Idautor': result[2], 'Ideditorial': result[3], 'FechaLanzamiento': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'libro' ###
@cross_origin()
@app.route('/update4/<Idlibro>', methods=['PUT'])
def update_contact4(Idlibro):
    codlibro = request.json['codlibro']  
    nombrelibro = request.json['nombrelibro']
    Idautor  = request.json['Idautor']
    Ideditorial   = request.json['Ideditorial']
    FechaLanzamiento = request.json['FechaLanzamiento']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE libro
        SET codlibro = %s,
            nombrelibro = %s,
            Idautor = %s,
            Ideditorial = %s,
            FechaLanzamiento = %s
        WHERE Idlibro = %s
    """, (codlibro, nombrelibro, Idautor, Ideditorial, FechaLanzamiento, Idlibro))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'libro' ###
@cross_origin()
@app.route('/delete4/<Idlibro>', methods = ['DELETE'])
def delete_contact4(Idlibro):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM libro WHERE Idlibro = %s', (Idlibro,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -----------------------------------TABLA PRESTAMOS----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE PRESTAMO DE LA TABLA 'prestamos' ####
@cross_origin()
@app.route('/add_contact5', methods=['POST'])
def add_contact5():
    if request.method == 'POST':
        codprestamo = request.json['codprestamo']
        IdContacts = request.json['IdContacts']  ## IdContacts
        IdLibro = request.json['IdLibro']  ## IdLibro
        fecha = request.json['fecha']  ## fecha
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO prestamos (codprestamo, IdContacts, IdLibro, fecha) VALUES (%s,%s,%s,%s)", (codprestamo, IdContacts, IdLibro, fecha))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'prestamos' ####
@cross_origin()
@app.route('/getAll5', methods=['GET'])
def getAll5():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM prestamos')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'codprestamo ': result[1], 'IdContacts ': result[2], 'IdLibro ': result[3], 'fecha': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'prestamos' ####
@cross_origin()
@app.route('/getAllById5/<IdPrestamo>',methods=['GET'])
def getAllById5(IdPrestamo ):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM prestamos WHERE IdPrestamo  = %s', (IdPrestamo ))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdPrestamo ': result[0], 'IdContacts ': result[1], 'IdLibro ': result[2], 'fecha': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'prestamos' ###
@cross_origin()
@app.route('/update5/<IdPrestamo>', methods=['PUT'])
def update_contact5(IdPrestamo):
    codprestamo = request.json['codprestamo']
    IdContacts = request.json['IdContacts']
    IdLibro = request.json['IdLibro']
    fecha = request.json['fecha']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE prestamos
        SET codprestamo = %s,
            IdContacts  = %s,
            IdLibro = %s,
            fecha = %s
        WHERE IdPrestamo = %s
    """, (codprestamo, IdContacts, IdLibro, fecha, IdPrestamo ))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'prestamos' ###
@cross_origin()
@app.route('/delete5/<IdPrestamo>', methods = ['DELETE'])
def delete_contact5(IdPrestamo):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM prestamos WHERE IdPrestamo = %s', (IdPrestamo,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -----------------------------------TABLA CONTACTS-----------------------------------###

## LA TABLA CONTACTS SERVIRÁ PARA LLEVAR EL REGISTRO DE LAS PERSONAS QUE ADQUIERAN UN LIBRO
## DE LA BIBLIOTECA

#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'contacts' ####
@cross_origin()
@app.route('/getAll', methods=['GET'])
def getAll():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id': result[0], 'identificacion': result[1],  'fullname': result[2], 'phone': result[3], 'email': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'contacts' ####
@cross_origin()
@app.route('/getAllById/<id>',methods=['GET'])
def getAllById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id LIKE %s', (id,))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id': result[0], 'fullname': result[1], 'phone': result[2], 'email': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CREAR UN REGISTRO DE PRESTAMO DE LA TABLA 'contacts' ####
@cross_origin()
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        identificacion = request.json['identificacion'] 
        fullname = request.json['fullname']  ## nombre
        phone = request.json['phone']        ## telefono
        email = request.json['email']        ## email
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (identificacion, fullname, phone, email) VALUES (%s,%s,%s,%s)", (identificacion, fullname, phone, email))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'contacts' ###
@cross_origin()
@app.route('/update/<id>', methods=['PUT'])
def update_contact(id):
    identificacion = request.json['identificacion'] 
    fullname = request.json['fullname']
    phone = request.json['phone']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE contacts
        SET identificacion = %s,
            fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
    """, (identificacion,fullname, email, phone, id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'contacts' ###
@cross_origin()
@app.route('/delete/<id>', methods = ['DELETE'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = %s', (id,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


### ------------------------------------------------------------------------------------###

###*************************************************************************************###


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
