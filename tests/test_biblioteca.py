import sys
import os

sys.path.append(os.path.abspath("src"))

from biblioteca.biblioteca import (
    cadastrar_livro,
    listar_livros,
    buscar_livro
)

def test_cadastrar_livro():
    biblioteca = []
    cadastrar_livro(biblioteca, "Dom Casmurro", "Machado de Assis")

    assert len(biblioteca) == 1
    assert biblioteca[0]["titulo"] == "Dom Casmurro"
    assert biblioteca[0]["autor"] == "Machado de Assis"


def test_listar_livros():
    biblioteca = []
    cadastrar_livro(biblioteca, "Livro 1", "Autor 1")
    cadastrar_livro(biblioteca, "Livro 2", "Autor 2")

    livros = listar_livros(biblioteca)
    assert len(livros) == 2


def test_buscar_livro():
    biblioteca = []
    cadastrar_livro(biblioteca, "Python Básico", "Autor A")
    cadastrar_livro(biblioteca, "Python Avançado", "Autor B")
    cadastrar_livro(biblioteca, "Java Básico", "Autor C")

    resultados = buscar_livro(biblioteca, "Python")
    assert len(resultados) == 2
