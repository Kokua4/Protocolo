def binario_a_texto(binario):
    try:
        texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
        return texto
    except ValueError:
        return "Error: La cadena binaria ingresada no es válida."

# Solicitar al usuario que ingrese la cadena binaria
cadena_binaria = input("Ingresa la cadena binaria: ")

# Llamar a la función de conversión e imprimir el resultado
texto_resultante = binario_a_texto(cadena_binaria)
print("Texto convertido:", texto_resultante)
