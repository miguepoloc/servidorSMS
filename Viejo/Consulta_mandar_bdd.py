# -*- coding: utf-8 -*-
#Importamos la librería de tiempo
import time
#Librería de MQTT para publicar
import paho.mqtt.publish as publish
#Conectar a la base de datos
import mysql.connector


def consulta_bdd(fecha_menor, fecha_mayor):
	"""Consulta la base de datos entre un intérvalo de fechas"""
	try:
		if fecha_mayor > fecha_menor:
			print (("Mandando los datos entre " + fecha_menor + " y " + fecha_mayor))
			query = ("SELECT * FROM datos WHERE fecha_sms BETWEEN %s AND %s;")
			datos = (fecha_menor, fecha_mayor)
			cursor_rpi.execute(query, datos)
			for (id, sensor, fecha, tipo, valor, bateria, fecha_sms) in cursor_rpi:
				consulta = ("{} {} {} {} {} {} {}".format(id, sensor,
					fecha, tipo, valor, bateria, fecha_sms))
				print (consulta)
				separado = consulta.split(' ')
				print ("Dividiendo el mensaje por espacios")
				idx, sensor, fecha, hora, tipo, valor, bat, fecha_sms, hora_sms = separado
				#2 prueba 2018-04-25 10:30:17 luz 1032.87 82 2018-04-25 11:00:56
				#'50','test',CURRENT_TIMESTAMP, 'ph', '"+msg.payload+"','90',CURRENT_TIMESTAMP)
				publicar = ("'" + idx + "', 'test', '" + fecha + " " + hora + "', '" + tipo
					+ "', '" + valor + "', '" + bat + "', '" + fecha_sms + " " + hora_sms + "'")
				print (publicar)
				publish.single("bdd", publicar, hostname="31.220.62.19")
				time.sleep(0.01)
	except UnboundLocalError:
		print ("No hay nada en la base de datos")


try:
	#Conecta al MySQL de la raspberry
	cnx_rpi = mysql.connector.connect(user='root', password='Contrasena1',
		host='127.0.0.1', database='riorancheria')
	#Crea la variable cursor
	cursor_rpi = cnx_rpi.cursor()
	print("Comienza")
	consulta_bdd("2018-04-25 18:00:00", "2018-04-25 20:00:00")
#Si hay un error de nombre de variable o no se puede dividir algún mensaje
except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
except (ValueError, NameError, AttributeError):
	print ("Hay un error al separar o en una variable o un atributo")
	print ("Fin del proceso")
#Si interrumpo con ctrl c
except KeyboardInterrupt:
	#cursor.close()
	cursor_rpi.close()
	#cnx.close()
	cnx_rpi.close()
	print ("Fin del proceso")
#Cuando finalice el ciclo try
finally:
	#GPIO.cleanup()
	print ("Fin del try")