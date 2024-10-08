### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Jesús", "Clemente", 25}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("Jasusmet")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Jasusmet")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Clemente" in my_other_set)
print("Clementi" in my_other_set)

# Eliminación

my_other_set.remove("Clemente")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Jesús", "Clemente", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))