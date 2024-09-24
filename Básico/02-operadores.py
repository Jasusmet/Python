# Operadores

#* Operadores aritméticos

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 // 5)
print(10 ** 5)

print("Hola " + "Python" + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

#* Operadores comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" == "Python")
print("Hola" != "Python")

#* Operadores lógicos

print(3 > 4 and "Hola" > "Python") # En Python se utiliza 'and' y no &&
print(3 > 4 or "Hola" > "Python") # En Python se utiliza 'or' y no ||
print(not(3 > 4)) # En Python se utiliza 'not' y no !

print(not(3 < 4 or ("Hola" > "Python" and 4 == 4))) # Ejemplo usando los tres operadores lógicos