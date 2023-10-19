import numpy as np
import random
import time
import matplotlib.pyplot as plt

w1_values = []
w2_values = []
bias_values = []
dbias_values = []
dw1_values = []
dw2_values = []

print("Perceptron")

passo = 0.1 # Velocidade de mudança

# w1 = float(input("W1: ")) # Peso para entradas
# w2 = float(input("W2: "))

# bias = float(input("Bias: ")) # Incremento da somatória

c = 99999

w1 = random.randint((c * -1), c)              
w2 = random.randint((c * -1), c)              
bias = random.randint((c * -1), c) 
             
            #    x1 x2 S
AND = np.array([[1, 1, 1],
                [1, 0, 1],
                [0, 1, 1],
                [0, 0, 0]])

def exibir_barra_progresso(atual, total, tamanho=25):
    progresso = atual / (total-1)
    arrow = '>' * int(round(progresso * tamanho) - 1)
    spaces = '=' * (tamanho - len(arrow))
    print(f"\r[{arrow}{spaces}] {progresso * 100:.2f}%", end='', flush=False)

print("\nTestando acerto")

acertos = 0
erros = 0

for b in range(1000):
    for i in range(4):
        x1 = AND[i][0]
        x2 = AND[i][1]

        calc = x1 * w1 + x2 * w2 + bias

        if(calc > 0):
            saida = 1
        else:
            saida = 0

        if(saida == AND[i][2]):
            acertos += 1
        else:
            erros += 1

        exibir_barra_progresso(b, 1000)

acuracia0 = acertos / (acertos + erros) * 100

print(f"\nTeste concluído.\n\nAcerto atual: {acuracia0:.2f}%\n\nPressione Enter para continuar...", end="")
input()

while True:
    print("\nTreinando")

    acertos = 0
    erros = 0

    for a in range(10000):
        dw1 = 0
        dw2 = 0
        dbias = 0

        for i in range(4):
            x1 = AND[i][0]
            x2 = AND[i][1]

            calc = x1 * w1 + x2 * w2 + bias

            if calc > 0:
                saida = 1
            else:
                saida = 0

            erro = AND[i][2] - saida
            dbias += erro * passo
            dw1 += erro * x1
            dw2 += erro * x2

            dbias_values.append(dbias)
            dw1_values.append(dw1)
            dw2_values.append(dw2)

            if(saida == AND[i][2]):
                acertos += 1
            else:
                erros += 1

            # print(f"({a}-{i})- Erro: {erro}")

        w1 += dw1
        w2 += dw2
        bias += dbias

        w1_values.append(w1)
        w2_values.append(w2)
        bias_values.append(bias)

        exibir_barra_progresso(a, 10000)

    acuracia1 = acertos / (acertos + erros) * 100

    print(f"\nTreino concluído.\n\nAcerto durante o treino: {acuracia1}%\n\nPressione Enter para continuar...", end="")
    input()

    print("\nTestando")

    acertos = 0
    erros = 0

    for b in range(1000):
        for i in range(4):
            x1 = AND[i][0]
            x2 = AND[i][1]

            calc = x1 * w1 + x2 * w2 + bias

            if calc > 0:
                saida = 1
            else:
                saida = 0

            if(saida == AND[i][2]):
                acertos += 1
            else:
                erros += 1

            # print(f"{x1}, {x2} -> {saida}")
        exibir_barra_progresso(b, 1000)

    acuracia = acertos / (acertos + erros) * 100

    print("\nResultados do treino\n")
    print(f"W1..........................{w1:.2f}")
    print(f"W2..........................{w2:.2f}")
    print(f"Bias........................{bias:.2f}")
    print(f"Acerto inicial..............{acuracia0:.2f}%")
    print(f"Acerto durante o treino.....{acuracia1:.2f}%")
    print(f"Acerto......................{acuracia:.2f}%")

    if(input("E-(Exit) T-(Try Again): ") == 'E'):
        break

print("\nTeste\n")

while True:
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))

    if x1 > 0:
        x1 = 1
    else:
        x1 = 0

    if x2 > 0:
        x2 = 1
    else:
        x2 = 0

    calc = x1 * w1 + x2 * w2 + bias

    if calc > 0:
        saida = 1
    else:
        saida = 0
    
    print(f"\n{x1} AND {x2} -> {saida}\n")

    if(input("E-(Exit) T-(Try Again): ") == 'E'):
        break

plt.figure(figsize=(10, 6))
plt.plot(w1_values, label='w1')
plt.plot(w2_values, label='w2')
plt.plot(bias_values, label='bias')
plt.plot(dbias_values, label='dbias')
plt.plot(dw1_values, label='dw1')
plt.plot(dw2_values, label='dw2')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Variation of Weights and Biases')
plt.legend()
plt.grid()
plt.show()

print("\nVariation of Weights and Biases:")
print("w1:")
print(asciichartpy.plot(w1_values))
print("\nw2:")
print(asciichartpy.plot(w2_values))
print("\nbias:")
print(asciichartpy.plot(bias_values))
print("\ndbias:")
print(asciichartpy.plot(dbias_values))
print("\ndw1:")
print(asciichartpy.plot(dw1_values))
print("\ndw2:")
print(asciichartpy.plot(dw2_values))

# 15040 465 015 