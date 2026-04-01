import xmlrpc.client

while True:
    operacao = input('Selecione a operação:\n1. Somar\n2. Subtrair\n3. Multiplicar\n4. Dividir\n')

    if operacao == '1':
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        print('Resultado:', xmlrpc.client.ServerProxy('http://localhost:8000').somar(a, b))
    elif operacao == '2':
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        print('Resultado:', xmlrpc.client.ServerProxy('http://localhost:8000').subtrair(a, b))
    elif operacao == '3':
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        print('Resultado:', xmlrpc.client.ServerProxy('http://localhost:8000').multiplicar(a, b))
    elif operacao == '4':
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        print('Resultado:', xmlrpc.client.ServerProxy('http://localhost:8000').dividir(a, b))
    else:
        print('Operação inválida')