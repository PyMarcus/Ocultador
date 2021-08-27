# oculta arquivos ou diretórios inteiros
import os


def ocult(*args):
    """Oculta arquivos ou diretórios"""
    for arquivos in args:
        try:
            os.rename(f'./{arquivos}', f'./.{arquivos}')
        except FileNotFoundError:
            print('O arquivo deve estar no diretório atual')
        else:
            print('Ocultado')

if __name__ == '__main__':
    file = input('informe o nome do arquivo: ')
    ocult(file)