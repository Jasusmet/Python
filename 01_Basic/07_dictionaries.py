### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Jesús",
                 "Apellido": "Clemente", 
                 "Edad": 25, 
                 1: "Python"}

my_dict = {
    "Nombre": "Jesús",
    "Apellido": "Clemente",
    "Edad": 25,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.73
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Clemente" in my_dict)
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle Jasusmet"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Fran"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items()) # Esto imprime tanto las keys como los values
print(my_dict.keys()) # Esto solo imprime las keys
print(my_dict.values()) # Esto solo imprime los values

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) # Creamos un nuevo diccionario cogiendo como keys lo que tenemos en una lista
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Creamos un nuevo diccionario cogiendo como keys lo que le pasemos
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict) # Creamos un nuevo diccionario cogiendo como keys las que ya teníamos en otro diccionario
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Jasusmet") # Creamos un nuevo diccionario cogiendo las keys de otro diccionario y posteriormente le damos un value para todas
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))