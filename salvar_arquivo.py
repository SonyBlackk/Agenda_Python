
try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('joao\n')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)




# 'r' - abre para ler
# 'w' - abre para escrever / arquivo é sobrescrito
# 'a' - abre para escrever / novo conteudo é adicionado ao finaç
# '+'
# 'b'