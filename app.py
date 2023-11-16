import random

input('Tecle enter para iniciar o jogo!')
print('-------------------------')
print('Iniciando jogo JokenPo...')
print('-------------------------')

nome = input('Digite o nome do jogador: ')
opcoes = ['pedra', 'papel', 'tesoura']

def venceu():
    print(f'{nome} você VENCEU! o Bot escolheu {bot}')

def perdeu():
    print(f'{nome} você PERDEU! o Bot escolheu {bot}')

def empate():
    print(f'EMPATOU! {nome} você e o Bot escolheram {bot}')

while True:
    bot = random.choice(opcoes)
    escolha = input(f'{nome} - Escolha uma opção - pedra|papel|tesoura: ')
    if escolha == bot:
        empate()
        continue
    elif escolha == 'pedra' and bot == 'tesoura':
        venceu()
        continue
    elif escolha == 'pedra' and bot == 'papel':
        perdeu()
        continue
    elif escolha == 'papel' and bot == 'pedra':
        venceu()
        continue
    elif escolha == 'papel' and bot == 'tesoura':
        perdeu()
        continue
    elif escolha == 'tesoura' and bot == 'papel':
        venceu()
        continue
    elif escolha == 'tesoura' and bot == 'pedra':
        perdeu()
        continue
    else:
        print(f'{nome} digite uma opção valida')
        continue
