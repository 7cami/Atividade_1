import numpy as np

caminho_arquivo = 'temperaturas.txt'

with open(caminho_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    temperaturas = np.array([list(map(int, linha.strip().split())) for linha in linhas])

print(f"{temperaturas}\n")

media_periodos = np.mean(temperaturas, axis = 1)
media_diarias = np.mean(temperaturas, axis = 0)
media_dias = np.mean(temperaturas)


print (f"Temperatura média do período: {media_dias:.2f}\n")
print(f"Média matutina:{media_periodos[0]:.2f}, média vespertina:{media_periodos[1]:.2f}, média noturna:{media_periodos[2]:.2f}\n")
print (f"Média do 1º dia: {media_diarias[0]:.2f}, média do 2º dia: {media_diarias[1]:.2f}, média do 3º dia: {media_diarias[2]:.2f} \n")

transposta_1 = temperaturas.T
print (f"{transposta_1}\n")
temperaturas_aquecimento = transposta_1 + 3
print (f"{temperaturas_aquecimento}\n")

produto_escalar = np.dot(temperaturas_aquecimento, temperaturas)
print(f"{produto_escalar}\n")

temperaturas_30 = temperaturas[temperaturas >= 30]
print(f"{temperaturas_30}\n")

temperaturas_30 -= 10
print(f"{temperaturas_30}\n")



