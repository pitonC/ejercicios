sub1: float = 0
sub2: float = 0
sub3: float = 0
print("-----------------------------------------------------")
print("Restaurante la flor")
sub = float(input("Cuanto es el valor a pagar: "))
sub1 = sub*.18
sub2 = sub*.20
sub3 = sub*.25
subT1 = sub + sub1
subT2 = sub + sub2
subT3 = sub + sub3
print("propina con 18%: ", sub1)
print("total con 18%: ", subT1)

print("propina con 20%: ", sub2)
print("total con 20%: ", subT2)

print("propina con 25%: ", sub3)
print("total con 25%: ", subT3)

print("-----------------------------------------------------")