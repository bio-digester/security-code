import time
import datetime
import socket
import os
import subprocess
import sys

def error_log(message, command):
    error = message + ' error at ' + str(datetime.datetime.now()) + '\n'
    log = open('error.log', 'a')
    log.write(error)
    log.close()
    process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)
    sys.exit()

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", int(sys.argv[1])
    MAX_TIME =  10 # 60 segundos vezes 10 = 10 minutos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(10)
    
    last_pulse_temperature = time.time()
    last_pulse_pressure = time.time()
    last_pulse_gas = time.time()
    last_pulse_server = time.time()
    last_pulse_water = time.time()
    
    msg = None
    command = "shutdown -r now"

    while True:
        try:
            sock.setblocking(0)
            conn, addr = sock.accept()
            msg = conn.recv(1024)
        except IOError as e:  # and here it is handeled
            pass
            
        if(msg):
            if "TEMPERATURE" in str(msg):
                last_pulse_temperature = time.time()
            if "PRESSURE" in str(msg):
                last_pulse_pressure = time.time()
            if "GAS" in str(msg):
                last_pulse_gas = time.time()
            if "SERVER" in str(msg):                
                last_pulse_server = time.time()
            if "WATER" in str(msg):
                last_pulse_water = time.time()

        past_pulse_temperature = time.time() - last_pulse_temperature
        past_pulse_pressure = time.time() - last_pulse_pressure
        past_pulse_gas = time.time() - last_pulse_gas
        past_pulse_server = time.time() - last_pulse_server
        past_pulse_water = time.time() - last_pulse_water
        
        print("-----------------------------")  
        print("Temperatura: " + str(past_pulse_temperature))
        print("Pressão: " + str(past_pulse_pressure))
        print("Nível: " + str(past_pulse_gas))
        print("Servidor: " + str(past_pulse_server))
        print("Água: " + str(past_pulse_water))
        print("-----------------------------")
        
        if(past_pulse_temperature >= MAX_TIME):
            error_log('RESISTENCE', command)
        if(past_pulse_pressure >= MAX_TIME):
            error_log('PRESSURE', command)
        if(past_pulse_gas >= MAX_TIME):
            error_log('GAS', command)
        if(past_pulse_server >= MAX_TIME):
            error_log('SERVER', command)
        if(past_pulse_water >= MAX_TIME):
            error_log('WATER', command)
