from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for process in instance._data:
        if process['nome_do_arquivo'] == path_file:
            return False
    print_process = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": txt_importer(path_file),
        }
    instance.enqueue(print_process)
    return sys.stdout.write(str(print_process))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
