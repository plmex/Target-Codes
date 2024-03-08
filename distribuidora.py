import json

def ler_arquivo(nome_arquivo):
    with open('dados.json','r') as arquivo_json:
        return json.load(arquivo_json)


def menorFaturamento(data):
    menorValor = data[0]['valor']
    diaMenorFaturamento = data[0]['dia']
    diasFaturamentoZero = []

    for dias in data:
        if dias['valor'] == 0:
            diasFaturamentoZero.append(dias['dia'])

    for valores in data:
        if valores['valor'] <= menorValor and valores['dia'] not in diasFaturamentoZero:
            menorValor = valores['valor']
            diaMenorFaturamento = valores['dia']

    return menorValor, diaMenorFaturamento


def maiorFaturamento(data):
    maiorValor = data[0]['valor']
    diaMaiorFaturamento = data[0]['dia']

    for valores in data:
        if valores['valor'] >= maiorValor:
            maiorValor = valores['valor']
            diaMaiorFaturamento = valores['dia']

    return maiorValor, diaMaiorFaturamento

def mediaMensal(data):
    somaValores = sum(valores['valor'] for valores in data if valores['valor'] != 0)
    diasComFaturamento = sum(1 for valores in data if valores['valor'] != 0)

    return somaValores / diasComFaturamento

def diasAcimaMedia(data, media):
    return sum(1 for valores in data if valores['valor'] > media)

def main():
    data = ler_arquivo('dados.json')

    menor_valor, dia_menor = menorFaturamento(data)
    maior_valor, dia_maior = maiorFaturamento(data)
    media = mediaMensal(data)
    contador = diasAcimaMedia(data, media)


    print(25*'=', end=' ')
    print('Estatísticas de Faturamento',end=' ')
    print(25*'=')
    print(f'O maior valor de faturamento foi de R$ {maior_valor:.2f} no dia {dia_maior}.')
    print(f'O menor valor de faturamento foi de R$ {menor_valor:.2f} no dia {dia_menor}.')
    print(f'A média mensal foi de R$ {media:.2f}.')
    print(f'{contador} dias do mês tiveram um faturamento superior à média mensal.')

if __name__ == "__main__":
    main()
