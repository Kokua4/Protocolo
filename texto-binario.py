def texto_a_binario(texto):
    try:
        binario = ' '.join(format(ord(char), '08b') for char in texto)
        return binario
    except Exception as e:
        return f"Error: {str(e)}"

# Solicitar al usuario que ingrese el texto
texto = input("Ingresa el texto a convertir a binario: ")

# Llamar a la función de conversión e imprimir el resultado
binario_resultante = texto_a_binario(texto)
print("Binario convertido:", binario_resultante)
