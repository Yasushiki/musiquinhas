def extrair_caracteres_do_meio(url):
    inicio = url.find("youtu.be/") + len("youtu.be/")
    fim = url.find("?", inicio)
    return url[inicio:fim]

def processar_arquivo(input_arquivo, output_arquivo):
    with open(input_arquivo, 'r') as arquivo_entrada:
        urls = arquivo_entrada.readlines()

    caracteres_do_meio = [extrair_caracteres_do_meio(url.strip()) for url in urls]

    with open(output_arquivo, 'w') as arquivo_saida:
        for caracteres in caracteres_do_meio:
            arquivo_saida.write(f"{caracteres}\n")

if __name__ == "__main__":
    input_arquivo = input("Digite o nome do arquivo de entrada (com extensão): ")
    output_arquivo = input("Digite o nome do arquivo de saída (com extensão): ")

    try:
        processar_arquivo(input_arquivo, output_arquivo)
        print(f"Os caracteres do meio foram salvos no arquivo '{output_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

