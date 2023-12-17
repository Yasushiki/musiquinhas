def remover_linhas_duplicadas(arquivo):
    with open(arquivo, 'r') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()

    linhas_sem_duplicatas = list(set(linhas))

    with open(arquivo, 'w') as arquivo_saida:
        for linha in linhas_sem_duplicatas:
            if linha.strip():  # Garante que linhas em branco não sejam adicionadas
                arquivo_saida.write(f"{linha}")

if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo para remover linhas duplicadas (com extensão): ")

    try:
        remover_linhas_duplicadas(arquivo)
        print(f"As linhas duplicadas foram removidas de '{arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

