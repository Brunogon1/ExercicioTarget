# Definindo as variáveis
INDICE = 13  # Até onde vamos somar
SOMA = 0     # Começamos com SOMA valendo 0
K = 0        # Variável de controle do loop

# Enquanto K for menor que INDICE
while K < INDICE:
    K += 1          # Incrementamos K em 1
    SOMA += K       # Somamos K ao valor de SOMA

# Após o loop, imprimimos o resultado de SOMA
print(SOMA)
