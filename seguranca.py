import time
import datetime
import socket

def error_log(message):
    error = message + ' error at ' + str(datetime.datetime.now()) + '\n'
    log = open('error.log', 'a')
    log.write(error)
    log.close()

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 7000
    MAX_TIME =  60 * 10 # 60 segundos vezes 10 = 10 minutos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(10)
    
    last_pulse_temperature = time.time()
    last_pulse_pressure = time.time()
    last_pulse_gas = time.time()
    last_pulse_server = time.time()
    last_pulse_water = time.time()
    
    
    while True:
        conn, addr = sock.accept()
        sock.setblocking(False)

        try:
            msg = conn.recv(1024)
        except IOError as e:  # and here it is handeled
            if e.errno == errno.EWOULDBLOCK:
                print("passou no if")
                pass
            else:
                print("passou no else")
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
            error_log('RESISTENCE')
        if(past_pulse_pressure >= MAX_TIME):
            error_log('PRESSURE')
        if(past_pulse_gas >= MAX_TIME):
            error_log('GAS')
        if(past_pulse_server >= MAX_TIME):
            error_log('SERVER')
        if(past_pulse_water >= MAX_TIME):
            error_log('WATER')
