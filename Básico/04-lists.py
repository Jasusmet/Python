# Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(len(my_list))

my_other_list = [25, 1.73, "Jesús", "Clemente"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_other_list.append("Jasusmet") # Insertar un elemento a una lista al final de la misma
print(my_other_list)

my_other_list.insert(1, "Negro") # Insertar un elemento en la posición que designemos de la lista
print(my_other_list)

my_other_list.remove("Negro") # Eliminamos el elemento que indiquemos
print(my_other_list)

print(my_list.pop()) # Eliminamos el último elemento de la lista, salvo que le indiquemos uno en concreto, y nos lo devuelve
print(my_list)

my_list.clear() # Con esta propiedad limpiamos todo el contenido que tengamos en la lista
print(my_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))