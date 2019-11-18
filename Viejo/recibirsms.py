# -*- coding: utf-8 -*-
#Importamos la librería serial
import serial
#Importamos la librería de tiempo
import time
print("Abriendo puerto serie")
serie = serial.Serial('/dev/ttyS0', 38400)
serie.close()
serie.open()
print("#escribiendo =1")
serie.write("AT+CMGF=1\r\n")
time.sleep(1)
print("Escribiendo 2,2")
serie.write("AT+CNMI=2,2,0,0,0\r\n")
time.sleep(1)
print("Ciclo infinito")
while 1:
	primera = serie.readline()
	if "+CMT" in primera:
		print ("Primera parte")
		print (primera)
		segunda = serie.readline()
		print ("Segunda parte")
		print (segunda)