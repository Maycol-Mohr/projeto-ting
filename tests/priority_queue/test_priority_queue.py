from ting_file_management.priority_queue import PriorityQueue
import pytest

regular_priority = {
        "nome_do_arquivo": "arquivo_teste1.txt",
        "qtd_linhas": 33,
        "linhas_do_arquivo": [...]
    }

high_priority = {
        "nome_do_arquivo": "arquivo_teste3.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [...]
    }


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    priority_queue = PriorityQueue()

    priority_queue.enqueue(regular_priority)

    priority_queue.enqueue(high_priority)

    assert len(priority_queue) == 2

    assert priority_queue.search(0) == high_priority

    assert priority_queue.dequeue() == high_priority

    assert priority_queue.search(0) == regular_priority

    assert len(priority_queue) == 1

    with pytest.raises(IndexError):
        priority_queue.search(99)
