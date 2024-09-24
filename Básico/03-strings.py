# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # Con este caracter especial se puede hacer un salto de línea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # Con este caracter especial se puede hacer tabulación
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

#* Formateo

name, surname, age = "Jesús", "Clemente", 25

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Esta forma no está mal
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Esta es la mejor manera si estamos formateando y queremos ser estrictos con los datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Esta es la forma más sencilla y utilizada

#* Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

#* División
language_slice = language[1:3]
print(language_slice)

#* Reverse
reversed_language = language[::-1]
print(reversed_language)

#* Funciones
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))
print("Py" == "py")