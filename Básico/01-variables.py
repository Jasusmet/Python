# Variables

my_string_variable = "My String variable" # La variable es un string
print(my_string_variable)

my_int_variable = 5 # La variable es un int
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # Transformamos la variable 'int' en una variable 'string'
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable) # Imprimimos las tres variables
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea (cuidado con abusar de esta sintaxis)
name, surname, alias, age = "Jesús", "Clemente", "Jasusmet", 25
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es:", alias)

# Inputs
"""
name = input('¿Cómo te llamas? ')
age = input ('¿Cuántos años tienes? ')
print(name)
print(age)
"""

# Cambiamos su tipo
name = 25
age = "Jesús"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 32
address = 1.5
print(type(address))