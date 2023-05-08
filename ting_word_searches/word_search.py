from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    """Aqui irá sua implementação"""
    lista_vazia = []

    for indice in range(len(instance)):
        arquivo = instance.search(indice)
        ocorrencias = []
        for index, linha in enumerate(arquivo['linhas_do_arquivo']):
            if word.lower() in linha.lower():
                ocorrencias.append({
                    'linha': index + 1
                })
        if ocorrencias:
            lista_vazia.append({
                "palavra": word,
                "arquivo": arquivo['nome_do_arquivo'],
                "ocorrencias": ocorrencias
            })

    return lista_vazia


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    lista_vazia = []

    for indice in range(len(instance)):
        arquivo = instance.search(indice)
        ocorrencias = []
        for index, linha in enumerate(arquivo['linhas_do_arquivo']):
            if word.lower() in linha.lower():
                ocorrencias.append({
                    'linha': index + 1,
                    'conteudo': linha
                })
        if ocorrencias:
            lista_vazia.append({
                "palavra": word,
                "arquivo": arquivo['nome_do_arquivo'],
                "ocorrencias": ocorrencias
            })

    return lista_vazia
