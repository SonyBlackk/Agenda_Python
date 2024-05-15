# Erros em tempo de compilação
# Erros em tempo de execição
# Erros de lógica
try:
    a = float(input('Digite um numero A: ')) #ValueError
    b = float(input('Digite um numero B: '))

    print(a/b) #ZeroDivisionError
except ValueError as error:
    print('Input invalido, digite apenas numeros')
except ZeroDivisionError as error:
    print('Não pode ser feita divisão por zero')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
finally:
    print('Fim do progama')