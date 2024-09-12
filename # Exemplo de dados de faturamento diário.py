# Exemplo de dados de faturamento diário
faturamento_diario = [1000, 2000, 3000, 0, 1500, 4000, 0, 2500]  # Lista com alguns dias sem faturamento

# Filtrando dias com faturamento
faturamento_valido = [valor for valor in faturamento_diario if valor > 0]

# Calculando o menor e maior faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Calculando a média
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

# Contando dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_faturamento)

# Exibindo os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
