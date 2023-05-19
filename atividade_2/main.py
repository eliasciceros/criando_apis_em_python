"""
    Script para reconhecer faces em imagens.
        - Utiliza decoradores, Haar cascades e OpenCV.
    
    Modo de utilizacao:
        - Mova seu terminal para o diretorio atividades_2
        - execute da seguinte maneira:
            - python main.py --imagepath images\Lenna.png
        
"""
__author__ = "Elias Cícero Moreira Guedes"
__date__ = "19 de Setembro de 2021"
__credits__ = ["Igor Souza, ministrante do curso 'Criando APIs em Python'"]


import argparse
from reconhecimento_facial import detect_faces


if __name__ == "__main__":
    """ 
        Execute em linha de comando (command line interface).
    """
    
    # Define os comandos utilizaveis na interface
    parser = argparse.ArgumentParser(prog='Script de reconhecimento facial')
    parser.add_argument('--imagepath', type=str, required=True, help='caminho da imagem')

    # Espera o comando executado
    args = parser.parse_args()

    # Executa a funcao com base no que foi solicitado
    detect_faces(path=args.imagepath)