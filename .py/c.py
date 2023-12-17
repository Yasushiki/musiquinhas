def append_arquivo(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, 'r') as origem:
        conteudo_origem = origem.read()

    with open(arquivo_destino, 'a') as destino:
        destino.write(conteudo_origem)

if __name__ == "__main__":
    arquivo_origem = input("Digite o nome do arquivo de origem para append (com extensão): ")
    arquivo_destino = input("Digite o nome do arquivo de destino (com extensão): ")

    try:
        append_arquivo(arquivo_origem, arquivo_destino)
        print(f"O conteúdo de '{arquivo_origem}' foi adicionado ao final de '{arquivo_destino}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

