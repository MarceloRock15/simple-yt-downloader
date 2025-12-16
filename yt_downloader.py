# Importa as bibliotecas necessárias
import pytubefix as pt
from pytubefix.cli import on_progress 
import inquirer

# Função que define o que o programa vai fazer de acordo com a escolha do usuário
def escolha(esco, yt):
    # Se escolhida a opção vídeo, o vídeo é baixado
    if "Vídeo" in esco['Escolha']:
        ys = yt.streams.get_highest_resolution()
    # Se escolhida a opção áudio, o áudio é baixado
    elif "Áudio" in esco['Escolha']:
        ys = yt.streams.get_audio_only()
    return ys


def main():
    # Usa a biblioteca inquirer para fornecer 2 opções para o usuário
    perguntas = [
        inquirer.List(
            'Escolha',
            message="Você quer baixar o áudio ou vídeo ? (Use Enter para confirmar)",
            choices=["Vídeo", "Áudio"],
        ),
    ]
    # Pede ao usuário as informações necessárias
    esco = inquirer.prompt(perguntas)
    url = input("Digite a url do áudio ou vídeo: ")
    pasta = input("Digite o caminho para salvar o áudio ou vídeo: ")
    # Mostra o progresso do download
    yt = pt.YouTube(url, on_progress_callback=on_progress)

    yts = escolha(esco, yt)

    # Mostra o título do vídeo e o salva na pasta escolhida
    print(yt.title)
    yts.download(output_path=pasta)

main()
