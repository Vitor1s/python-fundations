#TODO Aqui vamos ver os operadores logicos.

idade = 25

idade_minima = 18

limite = 18

# Aqui vou montar a logica de que eu preciso ter 18 anos ou menor para entrar na festa.

print(idade >= idade_minima and idade >= limite) # Aqui precisa que ambos sejam verdadeiros para retornar True.

print(idade <= idade_minima or idade <= limite) # Aqui nao precisa que ambso seja veradeiro, basta que um seja, pra retornar True.


print(not 1000 > 500, "cade") # Aqui o not inverte o valor, entao como 1000 é maior que 500, o resultado seria True, mas com o not ele inverte e retorna False.

console = []

print(not console)  # Aqui o not inverte o valor, entao como a lista está vazia, o resultado seria False, mas com o not ele inverte e retorna True.

print(not "saquei", "cade") # Aqui o not inverte o valor, entao como a string não está vazia, o resultado seria True, mas com o not ele inverte e retorna False.

print(not "") # Aqui o not inverte o valor, entao como a string está vazia, o resultado seria False, mas com o not ele inverte e retorna True.

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
print(not True) # False
print(not False) # True
print(True and True and False) # False
print(True or False or False) # True
