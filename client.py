import zmq

context = zmq.Context()

# Cria um socket para enviar a solicitação
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("\nBem vindo a calculadora distribuída simplificada :)!")

# Lê um número inteiro do usuário
numero = input("\nDeseja utilizar a calculadora? 1- Sim 2- Não\n=>")
# Envia a solicitação
socket.send_string(numero)

# Espera a resposta do servidor
operacoes = socket.recv_string()
print(operacoes)
expressao = input("=> ")
socket.send_string(expressao)

result = socket.recv_string()
print("resultado: ", result)

# Fecha o socket
socket.close()

#elif (numero == 2):
 #   print("Até breve :( !!!")
#else:
 #   print("Não reconheço esse comando!")