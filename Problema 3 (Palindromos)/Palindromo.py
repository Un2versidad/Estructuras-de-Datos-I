palabra = list(input("Ingresa una palabra: ").lower())
for i in range(len(palabra)):
    if palabra[0] == palabra[i-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
    break
