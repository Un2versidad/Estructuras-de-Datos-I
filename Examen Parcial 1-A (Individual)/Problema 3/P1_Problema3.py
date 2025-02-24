# Definimos dos conjuntos de ejemplo: AAA y BBB
AAA = {1, 2, 3, 4, 5}
BBB = {4, 5, 6, 7, 8}

print(f"Conjunto AAA: {AAA}")
print(f"Conjunto BBB: {BBB}")

# Calculamos la unión
union_resultado = AAA.union(BBB)
print(f"Unión de AAA y BBB: {union_resultado}")

# Calculamos la intersección
interseccion_resultado = AAA.intersection(BBB)
print(f"Intersección de AAA y BBB: {interseccion_resultado}")

# Calculamos la diferencia A - B (A−BA - BA−B)
diferencia_resultado = AAA.difference(BBB)
print(f"A−BA - BA−B: {diferencia_resultado}")