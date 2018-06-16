import time
import socket

if __name__ == "__main__":
	HOST, PORT = "0.0.0.0", 7000
	MAX_TIME = 60 * 10 # 60 segundos vezes 10 = 10 minutos
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((HOST, PORT))
	sock.listen()

	ultima_mensagem_temperatura = time.time()
	ultima_mensagem_pressao = time.time()
	ultima_mensagem_nivel = time.time()
	ultima_mensagem_servidor = time.time()
	ultima_mensagem_agua = time.time()

	conn, addr = sock.accept()

	while True:
		msg = conn.recv(1024)
		if (msg):
			if "temperatura" in str(msg):
				ultima_mensagem_temperatura = time.time()
			if "pressao" in str(msg):
				ultima_mensagem_pressao = time.time()
			if "nivel" in str(msg):
				ultima_mensagem_nivel = time.time()
			if "servidor" in str(msg):				
				ultima_mensagem_servidor = time.time()
			if "agua" in str(msg):
				ultima_mensagem_agua = time.time()


		tempo_passado_temperatura = time.time() - ultima_mensagem_temperatura
		tempo_passado_pressao = time.time() - ultima_mensagem_pressao
		tempo_passado_nivel = time.time() - ultima_mensagem_nivel
		tempo_passado_servidor = time.time() - ultima_mensagem_servidor
		tempo_passado_agua = time.time() - ultima_mensagem_agua
		
		print("-----------------------------")	
		print("Temperatura: " + str(tempo_passado_temperatura))
		print("Pressão: " + str(tempo_passado_pressao))
		print("Nível: " + str(tempo_passado_nivel))
		print("Servidor: " + str(tempo_passado_servidor))
		print("Água: " + str(tempo_passado_agua))
		print("-----------------------------")

		if(tempo_passado_temperatura >= MAX_TIME):
			print("Tempo de temperatura foi atingido")
		if(tempo_passado_pressao >= MAX_TIME):
			print("Tempo de pressão foi atingido")
		if(tempo_passado_nivel >= MAX_TIME):
			print("Tempo de nível foi atingido")
		if(tempo_passado_servidor >= MAX_TIME):
			print("Tempo de servidor foi atingido")
		if(tempo_passado_agua >= MAX_TIME):
			print("Tempo de água foi atingido")
