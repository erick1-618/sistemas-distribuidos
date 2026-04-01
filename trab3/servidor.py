from xmlrpc.server import SimpleXMLRPCServer

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(somar, "somar")
server.register_function(subtrair, "subtrair")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")

print("Servidor rodando...")
server.serve_forever()