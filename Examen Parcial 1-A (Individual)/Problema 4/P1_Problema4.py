# Definimos dos conjuntos de ejemplo
A = {2, 4, 6}
B = {1, 2, 3, 4, 5, 6}

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")

# Verificamos si A es subconjunto de B
es_subconjunto_A_B = A.issubset(B)
if es_subconjunto_A_B:
    print(f"El conjunto A ({A}) es subconjunto del conjunto B ({B}).")
else:
    print(f"El conjunto A ({A}) NO es subconjunto del conjunto B ({B}).")

# Verificamos si B es subconjunto de A
es_subconjunto_B_A = B.issubset(A)
if es_subconjunto_B_A:
    print(f"El conjunto B ({B}) es subconjunto del conjunto A ({A}).")
else:
    print(f"El conjunto B ({B}) NO es subconjunto del conjunto A ({A}).")

# Verificamos si A y B son mutuamente subconjuntos (es decir, si son iguales)
son_iguales = A.issubset(B) and B.issubset(A)
if son_iguales:
    print("Los conjuntos A y B son iguales.")
else:
    print("Los conjuntos A y B NO son iguales.")