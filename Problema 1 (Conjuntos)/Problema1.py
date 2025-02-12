talleres = [
    {"Ana", "Luis", "Carlos", "Marta"},
    {"Ana", "Carlos", "Jorge", "Pedro"},
    {"Luis", "Marta", "Pedro", "Ana"},
    {"Carlos", "Jorge", "Marta", "Ana"}
]

print("Participantes que asistieron a todos los talleres:", ", ".join(set.intersection(*talleres)) or "Ninguno")
print("Participantes que asistieron a al menos dos talleres:", ", ".join({p for p in set.union(*talleres) if sum(p in t for t in talleres) > 1}) or "Ninguno")
print("Participantes únicos (solo un taller):", ", ".join({p for p in set.union(*talleres) if sum(p in t for t in talleres) == 1}) or "Ninguno")
print("Participantes del Taller 2:", ", ".join(talleres[1]) or "Ninguno")
