#TODO Aqui vamos ver as assoiações.

#  Etendo que associação é usada para verificar se algo esta naquela lista de valores.



frutas = ["banana", "maçã", "laranja", "uva"]

print("banana" in frutas) # Aqui o resultado retorna True, pq a banana está na lista.

print("pera" in frutas) # Aqui o resultado retorna False, pq a pera não está na lista.

# Algo interessante é que se tiver letras maiusculas ou acentos ou minúsculas, o resultado retorna False.

print("Laranja" in frutas) # Aqui o resultado retorna False, pq o "L" de laranja está maiusculo, e na lista está minusculo.

print("laranja" not in frutas) # Aqui o resultado retorna False, pq a laranja está na lista, e o not inverte o valor.



