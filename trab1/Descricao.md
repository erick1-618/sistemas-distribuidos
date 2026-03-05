# Trabalho 1

Executar uma simulação Cliente-Servidor, onde o Cliente envie uma mensagem ao Servidor e o Servidor responda com uma mensagem. Porém, com a condição de que o Servidor deve criar uma Thread para cada requisição de cliente.

### Requisitos para entrega:
- A resposta do servidor deve conter o nome da Thread que respondeu a requisição do cliente.

### Como executar

1. Execute o script do servidor:
```
python trab1/server.py
```
2. Execute o script do cliente:
```
python trab1/client.py
```

### Ferramentas
- Python, utilizando o pacote de threading e socket
