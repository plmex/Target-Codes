def fibonacci (n):
    sequenciaFibonacci = [0,1]

    while sequenciaFibonacci[-1] + sequenciaFibonacci[-2]  <= n:  #somando o último e o antepenúltimo valor da lista
        sequenciaFibonacci.append(sequenciaFibonacci[-1] + sequenciaFibonacci[-2])

        if n == sequenciaFibonacci[-1]:
            return f'{n} pertence a sequência de Fibonacci.'
            break 
        elif sequenciaFibonacci[-1] > n:
            return f'{n} não pertence a sequencia de fibonacci.'

numero = int(input('informe um número inteiro: '))
resposta = fibonacci(numero)
print(resposta)

