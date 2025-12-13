from biblioteca.biblioteca import (
    cadastrar_livro,
    listar_livros,
    buscar_livro
)

def main():
    biblioteca = []

    while True:
        print("\n📚 Gerenciador de Biblioteca")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            cadastrar_livro(biblioteca, titulo, autor)

        elif opcao == "2":
            for livro in listar_livros(biblioteca):
                print(f"{livro['titulo']} - {livro['autor']}")

        elif opcao == "3":
            termo = input("Buscar título: ")
            resultados = buscar_livro(biblioteca, termo)
            for livro in resultados:
                print(f"{livro['titulo']} - {livro['autor']}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

