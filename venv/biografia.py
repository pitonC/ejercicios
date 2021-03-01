import re
nom = input("Cual es tu nombre: ")
cum = input("cual es tu fecha de nacimiento: ")
dir= input("cual es tu dirreccion: ")
met=input("cuales son tus metas: ")

if not re.match("^[a-z]*$", nom):
    print ("Error: caracter no permitido")
    exit()

print("nombre: "  + nom)
print("fecha de nacimiento: "+cum)
print("dirreccion: "+dir)
print("metas: "+met)