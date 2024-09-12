# Função para gerar a sequência de Fibonacci até um limite
def fibonacci_ate_n(limite):
    # Começamos a sequência com 0 e 1
    fib_seq = [0, 1]
    while fib_seq[-1] < limite:  # Enquanto o último número da lista for menor que o limite
        # Adicionamos a soma dos dois últimos números à sequência
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Número a ser verificado
n = int(input("Informe um número: "))

# Geramos a sequência de Fibonacci até o número n
fib_seq = fibonacci_ate_n(n)

# Verificamos se o número faz parte da sequência
if n in fib_seq:
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
