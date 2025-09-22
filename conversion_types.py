#Em conversao dos tipos temos diversas formas de fazer isso em python.

#inteiro para float
preco = 10 
print(preco)

preco = float(preco)
print(preco)

#E possivel fazer com divisao tbm
preco = 10 / 1
print(preco)

#Float para inteiro
preco = 10.5
print(preco)

preco = int(preco)
print(preco)

#Conversao por divisao

preco = 10
print(preco)

print(preco / 2)

print(preco // 2)


#Converter numero para string
preco = 10.50
idade = 25

print(str(preco))
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

#Converter string para numero muito usado no dia a dia pois boa parte dos dados vem como string de formulários e precisam ser convertidos para o tipo correto.

preco = "50.5"
idade = "20"

preco = (float(preco), int(idade))
print(preco)