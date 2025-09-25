#TODO Aqui vamos ver os operadores de identidade.


# Etendi que quando um objeto é nomeado, ele é armazenado na memória e recebe um endereço único.
# Os operadores de identidade em Python são usados para comparar a identidade de dois objetos, ou seja
# , verificar se ambos os objetos referenciam o mesmo local na memória.


curso = "Curso de Culinaria"

nome_do_curso = curso # Aqui 'nome_do_curso' referencia o mesmo objeto que 'curso'.

saldo, limite = 500, 500 # Aqui 'saldo' e 'limite' são dois objetos distintos, mesmo que tenham o mesmo valor.

print(curso is nome_do_curso) 

print(curso is not nome_do_curso) # Aqui o resultado retorna False, pq quando colocamos o not, ele inverte o valor que deveria ser True.

print(saldo is limite) # Aqui o resultado retorna False, pq 'saldo' e 'limite' são dois objetos distintos, mesmo que tenham o mesmo valor.

print(saldo is not limite) # Aqui o resultado retorna True, pq quando colocamos o not, ele inverte o valor que deveria ser False.