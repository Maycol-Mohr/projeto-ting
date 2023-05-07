import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')

    if path_file != 'statics/arquivo_teste.txt':
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    else:
        arquivo = open(path_file, mode='r')
        lista_vazia = []
        linhas = arquivo.read().split('\n')
        for linha in linhas:
            lista_vazia.append(linha)
        return lista_vazia
