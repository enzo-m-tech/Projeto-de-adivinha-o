import random
#from random import randit

sorteio = random.randint(0, 5).strip()

palpite=int(input('Digite um número entre 0 e 5:'))

if palpite == sorteio:
 print('Você acertou')
else:
    print('Você errou, o número era {}'.format(sorteio))
