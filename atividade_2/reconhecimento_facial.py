"""
    Aplica Haar cascades para deteccao de faces.
        - Utiliza-se para o treinamento o OpenCV, que contem muitos classificadores pre-treinados para faces, olhos e sorrisos.
"""


import cv2
from decorators.decorator_exec_time import decorator_exec_time


@decorator_exec_time
def detect_faces(path: str):
    """
        Dada uma imagem especificada por seu caminho, detecta faces e as exibe.
    """
    image = load_image(path=path)
    draw_rectangles(image=image)
    display_image(image=image)
    

def load_image(path: str) -> list[list[int]]:
    """
        Carrega e retorna uma imagem na memoria.
    """
    return cv2.imread(path)


def draw_rectangles(image: list[list[int]]):
    """
        Dada uma imagem carregada na memoria e representada por uma matrix de pixels,
        desenha retangulos em cada face detectada na imagem.
    """

    black_color = (0, 0, 0)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    detected_faces = face_cascade_classifier.detectMultiScale(gray_scale, 1.1, 4)
    for (x, y, w, h) in detected_faces:
        cv2.rectangle(img=image, pt1=(x, y), pt2=(x+w, y+h), color=black_color, thickness=3)


def display_image(image: list[list[int]]):
    """
        Exibe uma imagem carregada em memoria.
    """
    cv2.imshow('Rectangles das faces reconhecidas', image)
    cv2.waitKey()