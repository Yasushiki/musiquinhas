import youtube_dl

def obter_links_playlist(url_playlist):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url_playlist, download=False)
        if 'entries' in info:
            return [entry['url'] for entry in info['entries']]
        else:
            return []

def salvar_links_em_arquivo(links, nome_arquivo='links_playlist.txt'):
    with open(nome_arquivo, 'w') as arquivo:
        for link in links:
            arquivo.write(f"{link}\n")

if __name__ == "__main__":
    url_playlist = input("Digite a URL da playlist do YouTube: ")
    
    links = obter_links_playlist(url_playlist)

    if links:
        salvar_links_em_arquivo(links)
        print(f"Os links foram salvos no arquivo 'links_playlist.txt'.")
    else:
        print("Não foi possível obter os links da playlist.")

