# Função para inverter uma string
def inverter_string(texto):
    texto_invertido = ""  # Inicialmente a string invertida é vazia
    for char in texto:    # Para cada caractere na string original
        texto_invertido = char + texto_invertido  # Adiciona o caractere no início da nova string
    return texto_invertido

# Entrada da string
texto = input("Digite uma string: ")

# Chamando a função e exibindo o resultado
print(f"String invertida: {inverter_string(texto)}")
