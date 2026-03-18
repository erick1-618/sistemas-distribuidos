# Trabalho 2

Executar uma simulação do problema Produtor-Consumidor explicado em aula, e responder as perguntas do slide.

[Explicação em Vídeo](https://youtu.be/XTEnL-SEf4Y)

### Requisitos para entrega:
- As seguintes perguntas precisam ser respondidas:
1. Por que precisamos do mutex?
2. Onde estão as regiões críticas?
3. Podemos ter mais de N threads bloqueadas em wait(empty)?
4. Quanto vale empty + full?
5.  Podemos trocar a ordem das chamadas de wait dos semáforos mutex e empty/full?

### Como executar
```
python trab2/produtor-consumidor.py
```

### Ferramentas
- Python, utilizando o pacote de threading
