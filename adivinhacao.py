def jogar():
    print('------------------------------')
    print('     Jogo da adivinhação      ')
    print('------------------------------')

print('Fique a vontade para jogar!')

#Entrada de dados:

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativas {} de {}'.format(rodada, total_de_tentativas))


    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

chute = int(input('Digite um número: '))
print('Você digitou', chute)
acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto
chute_str = input('Digite o seu número: ')
print('Você digitou: ', chute_str)
chute = int(chute_str)

if (acertou):
         print('Você acertou!')
elif (maior):
         print('Você errou! O seu chute foi maior que o número secreto')
elif (menor):
         print('Você errou! O seu chute foi menor que o número secreto')

         rodada = rodada +1

         total_de_tentativas = total_de_tentativas - 1

print('Fim de Jogo!')
