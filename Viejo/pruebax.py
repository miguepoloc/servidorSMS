import serial
import time, sys

serie = serial.Serial("/dev/ttyS0",baudrate = 9600, timeout = 5)
serie.write(b"AT+CMGF=1\r\n") #Se coloca en modo recepción de mensajes
time.sleep(3)
print ("Borrando todo")
serie.write(b'AT+CMGDA="DEL ALL"\r\n') #Elimina todos los mensajes
time.sleep(3)
print ("Esperando un mensaje...")
while True:
    print("Número de bytes recibidos")
    print(serie.inWaiting())
    reply = serie.read(serie.inWaiting())   #Lee todos los bytes del bufer
    if reply != " ":    #Si no está vacío
        serie.write(b"AT+CMGR=1\r\n")   #Lee el único mensaje que hay
        time.sleep(3)
        reply = serie.readline(20)
        print ("Mensaje recibido")
        print (reply)

        time.sleep(3)
        #ser.write(b'AT+CMGDA="DEL ALL"\r') # delete all
        time.sleep(3)
    time.sleep(5)    