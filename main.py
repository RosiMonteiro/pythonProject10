import random

class Carro:
    vencedor = ''

    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade

    def correr(self):
        return random.randint(1, self.velocidade)

def main():
    carro1 = Carro('Carro 1', 100)
    carro2 = Carro('Carro 2', 120)
    carro3 = Carro('Carro 3', 110)

    print('Escolha um dos carros para competir:')
    print('1. Carro 1')
    print('2. Carro 2')
    print('3. Carro 3')

    opcao = int(input('Digite o número do carro que deseja correr: '))

    if opcao == 1:
        carro_escolhido = carro1
    elif opcao == 2:
        carro_escolhido = carro2
    elif opcao == 3:
        carro_escolhido = carro3
    else:
        print('Opção inválida. Tente novamente.')
        return

    tempo_minimo = float('inf')
    for carro in [carro1, carro2, carro3]:
        if carro == carro_escolhido:
            continue
        tempo = carro.correr()
        if tempo < tempo_minimo:
            tempo_minimo = tempo
            Carro.vencedor = carro.nome

    print(f'O carro vencedor foi {Carro.vencedor} com um tempo de {tempo_minimo} segundos.')

if __name__ == '__main__':
    main()