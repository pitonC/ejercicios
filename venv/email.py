
correo = input("dame correo?: ").strip()

user_name = correo[:correo.index("@")]

domain_name = correo[correo.index("@")+1:]

output = "buenos dias  '{}' tu correo esta registrado en '{}'".format(user_name,domain_name)

print(output)