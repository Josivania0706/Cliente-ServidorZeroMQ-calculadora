import zmq

context = zmq.Context()

# Cria um socket para receber a solicitação
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:

    # Espera por uma solicitação do cliente
    solicitacao = socket.recv_string()

    if (solicitacao == "1"):

        socket.send_string("\nOperações:\n Soma => + \n Subtração => - \n Multiplicação => * \n Divisão => /\nDigite sua expressão:\n PADRÃO: Número Operador Número\n")

        expressao = socket.recv_string()

        # Lista para armazenar os números e operadores separados
        partes = []
        numero_atual = ''

        # Itera por cada caractere da expressão
        for caractere in expressao:
            if caractere.isdigit():
                # Se o caractere for um dígito, adiciona-o ao número atual
                numero_atual += caractere
            else:
                # Se o caractere for um operador, adiciona o número atual e o operador à lista de partes
                if numero_atual:
                    partes.append(int(numero_atual))
                    numero_atual = ''
                if (caractere != ' '):
                    partes.append(caractere)

        # Adiciona o último número à lista de partes
        if numero_atual:
            partes.append(int(numero_atual))

        num1 = int(partes[0])  
        op = partes[1]  
        num2 = int(partes[2]) 
        result = 0 

        if (op == "+"): result = num1 + num2
        elif (op == "-"): result = num1 - num2
        elif (op == "*"): result = num1 * num2
        elif (op == "/"): result = num1 / num2
        else: result = '[ERRO] Operação inválida! ;('
        
        socket.send_string(str(result))


        

'''# Envia a resposta ao cliente
resposta = "Olá, cliente!"
socket.send_string(resposta)'''