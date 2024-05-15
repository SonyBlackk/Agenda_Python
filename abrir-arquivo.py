try:
    arquivo = open('arquivo.txt', 'b')
except FileNotFoundError:
    print('Arquivo não existe')